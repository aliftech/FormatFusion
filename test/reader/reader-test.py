import unittest
from FormatFusion import reader


class ReaderTests(unittest.TestCase):

    def test_read_file(self):
        filename = "../../test/test.json"

        result = reader.read_file(filename)
        return result

    def test_scan_url(self):
        url = 'https://github.com/aliftech/FormatFusion/raw/master/test/test.yaml'
        # This will raise an exception if the URL is not valid or can't be accessed.
        response = reader.scan_url(url)
        return response

    def save_file(self):
        data = self.test_read_file()
        filename = "temp.yaml"
        reader.save_file(data, filename)


if __name__ == '__main__':
    unittest.main()
