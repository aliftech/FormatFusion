import requests
import os


def read_file(filename):
    with open(filename, 'r') as file:
        result = file.read()
    return result


def scan_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error reading JSON from URL: {response.status_code}"


def save_file(filename, data):
    with open(filename, 'w') as file:
        file.write(str(data))
