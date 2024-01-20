"""
This module provides a class for connecting to HashiCorp Vault
and performing various operations.

Classes:
- Vault: A class representing a connection to HashiCorp Vault.

Functions:
- connect: Connects to the Vault server using the provided role ID and secret ID.
- generate_database_credentials: Generates database credentials for the specified role.
- encrypt_data: Encrypts the provided plaintext using the specified encryption key.
- decrypt_data: Decrypts the provided ciphertext using the specified decryption key.
"""
import sys
import base64
import os
from hvac import Client, exceptions


class Vault:
    """
    A class representing a connection to HashiCorp Vault.
    """

    def __init__(
        self,
        host: str = os.environ.get("VAULT_ADDR", "127.0.0.1:8200"),
        namespace: str = os.environ.get("VAULT_NAMESPACE", "default"),
        role_id: str = os.environ.get("VAULT_ROLE_ID", None),
        secret_id: str = os.environ.get("VAULT_SECRET_ID", None),
    ) -> None:
        """
        Initializes a new instance of the Vault class.

        Parameters:
        - host (str): The address of Vault. Default is the "VAULT_ADDR" env variable.
        - namespace (str): The namespace to use. Default is the "VAULT_NAMESPACE" env variable.
        - role_id (str): Role ID for Vault. Default is the "VAULT_ROLE_ID" env variable.
        - secret_id (str): Secret ID for Vault. Default is the "VAULT_SECRET_ID" env variable.
        """
        self.host = host
        self.role_id = role_id
        self.secret_id = secret_id
        self.namespace = namespace
        self.client = Client(url=self.host, namespace=self.namespace)

    def connect(self) -> None:
        """
        Connects to the Vault server using the provided role ID and secret ID.

        Raises:
        - exceptions.InvalidRequest: If the authentication request is invalid.
        """
        try:
            self.client.auth.approle.login(
                role_id=self.role_id, secret_id=self.secret_id
            )

            assert self.client.is_authenticated()
            print("Successfully authenticated with Vault")
        except exceptions.InvalidRequest as error:
            print(f"Unable to authenticate to Vault {error}")
            sys.exit(1)

    def generate_database_credentials(
        self, role: str, mount_point: str = "database"
    ) -> dict:
        """
        Generates database credentials for the specified role.

        Args:
        - role (str): The name of the role for which to generate credentials.
        - mount_point (str): The mount point of the database secrets engine. Defaults to "database".

        Returns:
        - dict: A dictionary containing the generated credentials.

        Raises:
        - exceptions.Forbidden: If the request to generate credentials is forbidden.
        """
        try:
            credentials = self.client.secrets.database.generate_credentials(
                name=role, mount_point=mount_point
            )
            print(f"Successfully generated database credentials for {role}")
            return {
                "username": credentials["data"]["username"],
                "password": credentials["data"]["password"],
            }
        except exceptions.Forbidden as error:
            print(f"Unable to generate database credentials {error}")
            sys.exit(1)

    def encrypt_data(
        self,
        plaintext: str,
        context: dict = None,
        encryption_key: str = None,
        mount_point: str = "transit",
    ) -> str:
        """
        Encrypts the provided plaintext using the specified encryption key.

        Args:
        - plaintext (str): The plaintext to encrypt.
        - context (dict): Additional context information for encryption. Defaults to None.
        - encryption_key (str): The name of the encryption key. Defaults to None.
        - mount_point (str): The mount point of the transit secrets engine. Defaults to "transit".

        Returns:
        - str: The ciphertext.

        Raises:
        - exceptions.Forbidden: If the request to encrypt data is forbidden.
        """
        encoded_plaintext = base64.b64encode(plaintext.encode("utf-8"))

        try:
            ciphertext = self.client.secrets.transit.encrypt_data(
                name=encryption_key,
                plaintext=str(encoded_plaintext, "utf-8"),
                context=context,
                mount_point=mount_point,
            )
            return ciphertext["data"]["ciphertext"]
        except exceptions.Forbidden as error:
            print(f"Unable to encrypt data {error}")
            sys.exit(1)

    def decrypt_data(
        self,
        ciphertext: str,
        context: dict = None,
        decryption_key: str = None,
        mount_point: str = "transit",
    ) -> str:
        """
        Decrypts the provided ciphertext using the specified decryption key.

        Args:
        - ciphertext (str): The ciphertext to decrypt.
        - context (dict): Additional context information for decryption. Defaults to None.
        - decryption_key (str): The name of the decryption key. Defaults to None.
        - mount_point (str): The mount point of the transit secrets engine. Defaults to "transit".

        Returns:
        - str: The decrypted plaintext.

        Raises:
        - exceptions.Forbidden: If the request to decrypt data is forbidden.
        """
        try:
            decrypted_plaintext = self.client.secrets.transit.decrypt_data(
                name=decryption_key,
                ciphertext=ciphertext,
                context=context,
                mount_point=mount_point,
            )
            return str(
                base64.b64decode(decrypted_plaintext["data"]["plaintext"]), "utf-8"
            )
        except exceptions.Forbidden as error:
            print(f"Unable to decrypt data {error}")
            sys.exit(1)
