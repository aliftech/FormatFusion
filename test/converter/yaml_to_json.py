import unittest
import FormatFusion as ff


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
        json_data = ff.yaml_to_json(yaml_data)
        return json_data


if __name__ == '__main__':
    unittest.main()
