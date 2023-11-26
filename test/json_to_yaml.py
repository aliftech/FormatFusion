import unittest
import yamlify as yf


class JSONToYAMLTests(unittest.TestCase):

    def test_simple_json_to_yaml(self):
        json_data = {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "Jalan Merdeka",
                "city": "Jakarta",
                "province": "DKI Jakarta"
            }
        }
        yaml_data = yf.json_to_yaml(json_data)
        return yaml_data

    def test_json_to_yaml_with_indent(self):
        json_data = {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "Jalan Merdeka",
                "city": "Jakarta",
                "province": "DKI Jakarta"
            }
        }
        yaml_data = yf.json_to_yaml(json_data, indent=2)
        return yaml_data

    def test_json_to_yaml_with_sort_keys(self):
        json_data = {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "Jalan Merdeka",
                "city": "Jakarta",
                "province": "DKI Jakarta"
            }
        }
        yaml_data = yf.json_to_yaml(json_data, sort_keys=True)
        return yaml_data

    def test_json_to_yaml_from_file(self):
        with open('test.json', 'r') as f:
            json_data = f.read()
        actual_yaml = yf.json_to_yaml(json_data)
        return actual_yaml

    def test_json_to_yaml_from_url(self):
        url = 'https://github.com/aliftech/YAMLify/blob/master/test.json'
        yaml_data = yf.yaml_to_json_from_url(url)
        return yaml_data


if __name__ == '__main__':
    unittest.main()
