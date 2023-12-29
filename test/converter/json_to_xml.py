import unittest
import FormatFusion.json_to_xml as ff


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

        result = ff.json_to_xml(json_data)
        return result


if __name__ == '__main__':
    unittest.main()
