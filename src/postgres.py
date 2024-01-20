"""
This module provides a class for connecting to a PostgreSQL database
and performing various operations.

Classes:
- Postgresql: A class representing a connection to a PostgreSQL database.

Functions:
- connect: Connects to the PostgreSQL database using the provided credentials.
- create_table: Creates a new table in the database.
- insert_data: Inserts data into a table in the database.
- retrieve_data: Retrieves data from a table in the database.
"""
import sys
from typing import List
from psycopg2 import Error as PostgresError, connect


class Postgresql:
    """
    A class representing a connection to a PostgreSQL database.
    """

    def __init__(self, host: str, database: str, username: str, password: str) -> None:
        """
        Initializes a new instance of the Postgresql class.

        Parameters:
        - host (str): The host address of the database.
        - database (str): The name of the database.
        - username (str): The username for authentication.
        - password (str): The password for authentication.
        """
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def connect(self) -> None:
        """
        Connects to the PostgreSQL database using the provided credentials.

        Raises:
        - PostgresError: If the connection fails.
        """
        print(
            f"Connecting to database {self.database} on host {self.host} as user {self.username}"
        )

        try:
            self.connection = connect(
                host=self.host,
                database=self.database,
                user=self.username,
                password=self.password,
            )
            print(f"Connection established successfully as user {self.username}")
        except PostgresError as error:
            print(f"Error while connecting to PostgreSQL: {error}")
            sys.exit(1)

    def create_table(self, table_name: str, columns: tuple) -> None:
        """
        Creates a new table in the database.

        Args:
        - table_name (str): The name of the table.
        - columns (tuple): A tuple of column names and their data types.

        Raises:
        - PostgresError: If the table creation fails.

        Example:
        psql.create_table("users", ("name varchar(255)", "email varchar(255)"))
        """
        column_names = ", ".join(columns)

        sql_statement = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_names});"

        try:
            cursor = self.connection.cursor()

            cursor.execute(sql_statement)

            self.connection.commit()

            print(f"Table {table_name} created successfully")
        except PostgresError as error:
            print(f"Error while creating table {table_name}: {error}")
            sys.exit(1)

    def insert_data(self, table: str, columns: tuple, values: tuple) -> None:
        """
        Inserts data into a table in the database.

        Parameters:
        - table (str): The name of the table.
        - columns (tuple): A tuple of column names.
        - values (tuple): A tuple of values to be inserted.

        Example:
        psql.insert_data("users", ("name", "email"), ("John", "test@test.com"))
        """
        column_names = ", ".join(columns)
        value_placeholders = ", ".join(["%s"] * len(columns))

        sql_statement = (
            f"INSERT INTO {table} ({column_names}) VALUES ({value_placeholders});"
        )

        try:
            cursor = self.connection.cursor()

            cursor.execute(sql_statement, values)

            self.connection.commit()

            print(f"Data inserted successfully into table {table}")
        except PostgresError as error:
            print(f"Error while inserting data into table {table}: {error}")
            sys.exit(1)

    def retrieve_data(self, table: str, column: str, value: str) -> List:
        """
        Retrieves data from a table in the database.

        Parameters:
        - table (str): The name of the table.
        - column (str): The name of the column to filter by.
        - value (str): The value to filter by.

        Returns:
        - List: A list of tuples representing the retrieved data.

        Example:
        psql.retrieve_data("users", "name", "John")
        """
        sql_statement = f"SELECT * FROM {table} WHERE {column}='{value}';"

        try:
            cursor = self.connection.cursor()

            cursor.execute(sql_statement)

            self.connection.commit()

            print(
                f"Successfully retrieved data from table {table} with {column}={value}"
            )

            return cursor.fetchall()

        except PostgresError as error:
            print(f"Error while retrieving data from table {table}: {error}")
            sys.exit(1)
