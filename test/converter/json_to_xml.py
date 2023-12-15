import unittest
import yamlify as yf


class JSONToXMLTests(unittest.TestCase):

    def test_simple_json_to_xml(self):
        json_data = """{
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "Jalan Merdeka",
                "city": "Jakarta",
                "province": "DKI Jakarta"
            }
        }"""

        result = yf.json_to_xml(json_data)
        return result


if __name__ == '__main__':
    unittest.main()
