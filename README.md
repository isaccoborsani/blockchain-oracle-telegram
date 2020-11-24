# Blockchain Oracle Telegram

FIRSTLY:

## PLEASE REPLACE "{$YOUR_PATH}" WITH YOUR LOCAL PROJECT FOLDER PATH IN utils.py AND bot.py!

Here below you can download latest Takamaka-Blockchain jar resources

https://downloads.takamaka.dev/FILES/takamakachain-1.0-SNAPSHOT-jar-with-dependencies.jar

Place this file in the project root folder

Have a nice code :)


## Working VENV - Linux

### 1° Create an empty venv folder
```bash
python<version> -m venv env
source env/bin/activate
```
### 2° Install project dependencies


```bash

pip install wheel

```

```bash

pip install Babel Click Flask Flask-Babel Flask-Login Flask-Migrate Flask-SQLAlchemy Jinja2 Mako MarkupSafe SQLAlchemy Werkzeug

pip install alembic attrdict attrs base58 certifi cffi chardet cryptography cytoolz eth-abi eth-account eth-hash eth-keyfile eth-keys eth-rlp eth-typing eth-utils fpdf hexbytes idna importlib-metadata ipfshttpclient itsdangerous jsonschema lru-dict multiaddr mysql-connector-python 

pip install netaddr parsimonious paypalrestsdk pip protobuf pyOpenSSL pycparser pycryptodome  pyrsistent python-dateutil python-editor pytz requests rlp setuptools six toolz typing-extensions urllib3 varint web3 websockets zipp 

pip install schwifty

pip install flaskhmac

pip install tweepy

pip install python-telegram-bot --upgrade

```


```bash

pip install wheel Babel Click Flask Flask-Babel Flask-Login Flask-Migrate Flask-SQLAlchemy Jinja2 Mako MarkupSafe SQLAlchemy Werkzeug alembic attrdict attrs base58 certifi cffi chardet cryptography cytoolz eth-abi eth-account eth-hash eth-keyfile eth-keys eth-rlp eth-typing eth-utils fpdf hexbytes idna importlib-metadata ipfshttpclient itsdangerous jsonschema lru-dict multiaddr mysql-connector-python netaddr parsimonious paypalrestsdk pip protobuf pyOpenSSL pycparser pycryptodome  pyrsistent python-dateutil python-editor pytz requests rlp setuptools six toolz typing-extensions urllib3 varint web3 websockets zipp schwifty

```


### 3° Start local server
```bash
export FLASK_APP=app.py
flask run
```


