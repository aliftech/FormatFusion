import unittest
import FormatFusion.json_to_yaml as ff


class JSONToYAMLTests(unittest.TestCase):

    def test_simple_json_to_yaml(self):
        json_data = """{
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "Jalan Merdeka",
                "city": "Jakarta",
                "province": "DKI Jakarta"
            }
        }"""
        yaml_data = ff.json_to_yaml(json_data)
        return yaml_data


if __name__ == '__main__':
    unittest.main()
