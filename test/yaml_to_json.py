import unittest
import yamlify as yf


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
        json_data = yf.yaml_to_json(yaml_data)
        return json_data

    def test_yaml_to_json_with_indent(self):
        yaml_data = "name: John Doe\nage: 30\ncity: Seattle"
        json_data = yf.yaml_to_json(yaml_data, indent=2)
        return json_data

    def test_yaml_to_json_with_sort_keys(self):
        yaml_data = "city: Seattle\nage: 30\nname: John Doe"
        json_data = yf.yaml_to_json(yaml_data, sort_keys=True)
        return json_data

    def test_yaml_to_json_from_file(self):
        with open('test.yaml', 'r') as f:
            yaml_data = f.read()
        actual_json = yf.yaml_to_json(yaml_data)
        return actual_json

    def test_yaml_to_json_from_url(self):
        url = 'https://github.com/aliftech/YAMLify/raw/master/test.yaml'
        json_data = yf.yaml_to_json_from_url(url)
        return json_data


if __name__ == '__main__':
    unittest.main()
