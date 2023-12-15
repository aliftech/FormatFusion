import unittest
import yamlify as yf


class YAMLToXMLTests(unittest.TestCase):

    def test_simple_yaml_to_xml(self):
        yaml_data = """
        name: John Doe
        age: 30
        address:
            street: Jalan Merdeka
            city: Jakarta
            province: DKI Jakarta
        """
        json_data = yf.yaml_to_xml(yaml_data)
        return json_data


if __name__ == '__main__':
    unittest.main()
