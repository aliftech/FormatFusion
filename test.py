import unittest
from yaml_converter.yaml_to_json import *
from json_converter.json_to_yaml import *


class YAMLToJSONTests(unittest.TestCase):

    def test_simple_yaml_to_json(self):
        yaml_data = """
        name: John Doe
        age: 30
        address:
            street: Jalan Merdeka
            city: Jakarta
            province: DKI Jakarta
        """
        json_data = yaml_to_json(yaml_data)
        return json_data

    def test_yaml_to_json_with_indent(self):
        yaml_data = "name: John Doe\nage: 30\ncity: Seattle"
        json_data = yaml_to_json(yaml_data, indent=2)
        return json_data

    def test_yaml_to_json_with_sort_keys(self):
        yaml_data = "city: Seattle\nage: 30\nname: John Doe"
        json_data = yaml_to_json(yaml_data, sort_keys=True)
        return json_data

    def test_yaml_to_json_from_file(self):
        with open('test.yaml', 'r') as f:
            yaml_data = f.read()
        actual_json = yaml_to_json(yaml_data)
        return actual_json

    def test_yaml_to_json_from_url(self):
        url = 'https://github.com/aliftech/YAMLify/blob/master/test.yaml'
        json_data = yaml_to_json_from_url(url)
        return json_data


class JSONToYAMLTests(unittest.TestCase):

    def test_simple_json_to_yaml(self):
        json_data = '''
        {
            "name": "John Doe",
            "age": 30,
            "city": "Seattle"
        }
        '''

        yaml_data = json_to_yaml(json_data)
        return yaml_data


if __name__ == '__main__':
    unittest.main()
