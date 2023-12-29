import unittest
import FormatFusion.xml_to_json as ff


class XMLToJSONTests(unittest.TestCase):

    def test_simple_xml_to_json(self):
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
        json_data = ff.json_to_xml(xml_data)
        return json_data


if __name__ == '__main__':
    unittest.main()
