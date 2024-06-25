import requests


class IO:
    def __init__(self):
        self.data = None

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.data = file.read()
            return self
        except Exception as e:
            raise ValueError(f"Error reading file '{filename}': {e}")

    def scan_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for bad status codes (4xx and 5xx)
            self.data = response.text
            return self.data
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error reading URL '{url}': {e}")

    def save_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write(str(self.data))
        except Exception as e:
            raise ValueError(f"Error saving data to file '{filename}': {e}")
