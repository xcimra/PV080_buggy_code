import sys
import os
import yaml
import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)

        
CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person(object):
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


from urllib.parse import urlparse
import urllib.request
import ipaddress
import socket


ALLOWED_HOSTS = {"example.com", "www.example.com"}

def fetch_website(urllib_version, url):
    if urllib_version not in {"2", "3"}:
        raise ValueError("Unsupported urllib version")

    parsed = urlparse(url)

    # Allow only http/https
    if parsed.scheme not in {"http", "https"}:
        raise ValueError("Invalid scheme")

    # Allow only trusted domains
    if parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError("Host not allowed")

    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.read()
    except Exception:
        return "Exception"

def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data
    
def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice  = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)

