import os
from flask import Flask, flash, request, render_template
from vault import Vault
from postgres import Postgresql

app = Flask(__name__)
app.secret_key = "38b9f9e4e597f22afd5b711e23e99387"

vault = Vault()
vault.connect()

encryption_key = "aes256-gcm96-key"
database_vault_role = "encryptah"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cipher_text = vault.encrypt_data(
            request.form["email"], encryption_key=encryption_key
        )

        psql = db_connect()

        psql.insert_data(
            "users", ("name", "email"), (request.form["name"], cipher_text)
        )
        flash("Data inserted successfully into table users")

    return render_template("index.html")


@app.route("/records", methods=["GET"])
def view_records():
    psql = db_connect()

    return render_template("records.html", records=psql.retrieve_data("users"))


@app.route("/health", methods=["GET"])
def health():
    return "OK"


def db_connect():
    db_creds = vault.generate_database_credentials(database_vault_role)
    psql = Postgresql(username=db_creds["username"], password=db_creds["password"])

    psql.connect()

    return psql


def main():
    app.run(
        host=os.environ.get("FLASK_HOST", "127.0.0.1"),
        port=os.environ.get("FLASK_PORT", 5000),
    )


if __name__ == "__main__":
    main()
