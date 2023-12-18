import unittest
import yamlify as yf


class ReaderTests(unittest.TestCase):

    def test_read_file(self):
        filename = "../../test/test.json"

        result = yf.read_file(filename)
        return result

    def test_scan_url(self):
        url = 'https://api.github.com'
        # This will raise an exception if the URL is not valid or can't be accessed.
        response = yf.scan_url(url)
        return response

    def save_file(self):
        data = self.test_read_file()
        filename = "temp.yaml"
        yf.save_file(data, filename)


if __name__ == '__main__':
    unittest.main()
