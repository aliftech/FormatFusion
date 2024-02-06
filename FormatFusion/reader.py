import requests
import os


def read_file(filename):
    if validate_format(filename) is not False:
        with open(filename, 'r') as file:
            result = file.read()
        return result
    else:
        return False


def scan_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error reading JSON from URL: {response.status_code}"


def save_file(filename, data):
    with open(filename, 'w') as file:
        file.write(str(data))


def validate_format(filename):
    """
    Memeriksa apakah format file yang diberikan cocok dengan format yang didukung dan mengembalikan formatnya jika valid, False jika tidak.

    Args:
        filename (str): Nama file yang akan divalidasi.

    Returns:
        str: Format file (".json", ".yaml", dll.) jika valid, False jika tidak.
    """

    supported_formats = {
        "JSON": ".json",
        "YAML": ".yaml",
        "XML": ".xml",
        "CSV": ".csv",
        # Tambahkan format lainnya di sini, pastikan konsistensi casing dengan key yang sudah ada
    }

    _, extension = os.path.splitext(filename.lower())

    if extension in supported_formats.values():
        # Case-insensitive match: Temukan key yang cocok berdasarkan value
        format_name = max(format_name for format_name,
                          format_ext in supported_formats.items() if format_ext == extension)
        return format_name.lower()  # Kembalikan format string yang sesuai
    else:
        return False
