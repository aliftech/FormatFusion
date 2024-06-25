import unittest
import json
import yaml
import pandas as pd
import xmltodict
from FormatFusion import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()

    def test_from_json(self):
        json_data = '{"name": "John", "age": 30}'
        result = self.converter.from_json(json_data).data
        self.assertEqual(result, {"name": "John", "age": 30})

    def test_from_yaml(self):
        yaml_data = "name: John\nage: 30"
        result = self.converter.from_yaml(yaml_data).data
        self.assertEqual(result, {"name": "John", "age": 30})

    def test_from_csv(self):
        csv_data = "name,age\nJohn,30"
        result = self.converter.from_csv(csv_data).data
        expected = [{"name": "John", "age": "30"}]
        self.assertEqual(result, expected)

    def test_from_xml(self):
        xml_data = "<root><name>John</name><age>30</age></root>"
        result = self.converter.from_xml(xml_data).data
        self.assertEqual(result, {"root": {"name": "John", "age": "30"}})

    def test_to_json(self):
        data = {"name": "John", "age": 30}
        result = self.converter.to_json().data
        expected = json.dumps(data, indent=4, sort_keys=True)
        self.assertEqual(result, expected)

    def test_to_yaml(self):
        data = {"name": "John", "age": 30}
        self.converter.data = data
        result = self.converter.to_yaml().data
        expected = yaml.safe_dump(data, sort_keys=False)
        self.assertEqual(result, expected)

    def test_to_csv(self):
        data = [{"name": "John", "age": 30}]
        self.converter.data = data
        result = self.converter.to_csv().data
        expected = "name,age\nJohn,30\n"
        self.assertEqual(result, expected)

    def test_to_xml(self):
        data = {"name": "John", "age": 30}
        self.converter.data = data
        result = self.converter.to_xml(root_tag='root').data
        expected = xmltodict.unparse({"root": data}, pretty=True)
        self.assertEqual(result, expected)

    def test_to_dataframe(self):
        data = [{"name": "John", "age": 30}]
        self.converter.data = data
        result = self.converter.to_dataframe()
        expected = pd.DataFrame(data)
        pd.testing.assert_frame_equal(result, expected)

    def test_from_dataframe(self):
        df = pd.DataFrame([{"name": "John", "age": 30}])
        result = self.converter.from_dataframe(df).data
        expected = [{"name": "John", "age": 30}]
        self.assertEqual(result, expected)

    def test_invalid_json(self):
        with self.assertRaises(ValueError):
            self.converter.from_json("invalid json")

    def test_invalid_yaml(self):
        with self.assertRaises(ValueError):
            self.converter.from_yaml("invalid: yaml: data")

    def test_invalid_csv(self):
        with self.assertRaises(ValueError):
            self.converter.from_csv("name;age\nJohn;30")  # Invalid CSV

    def test_invalid_xml(self):
        with self.assertRaises(ValueError):
            self.converter.from_xml(
                "<root><name>John<age>30</age></root>")  # Invalid XML

    def test_empty_data(self):
        self.converter.data = None
        with self.assertRaises(ValueError):
            self.converter.to_csv()


if __name__ == "__main__":
    unittest.main()
