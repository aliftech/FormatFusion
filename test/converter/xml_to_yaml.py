import unittest
import FormatFusion as ff


class XMLToYAMLTests(unittest.TestCase):

    def test_simple_xml_to_yaml(self):
        xml_data = """
        <?xml version="1.0" ?>
        <root>
            <name>John Doe</name>
            <age>30</age>
            <address>
                <street>Jalan Merdeka</street>
                <city>Jakarta</city>
                <province>DKI Jakarta</province>
            </address>
        </root>
        """
        yaml_data = ff.yaml_to_xml(xml_data)
        return yaml_data


if __name__ == '__main__':
    unittest.main()
