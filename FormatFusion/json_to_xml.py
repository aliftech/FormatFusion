import json
import xmltodict
import xml.dom.minidom


def json_to_xml(data):
    """Converts a JSON object to a prettified XML string."""
    try:
        data_json = json.loads(data)
        xml_str = xmltodict.unparse({"root": data_json})

        # Prettify the XML
        xml_dom = xml.dom.minidom.parseString(xml_str)
        # Adjust the indentation as needed
        prettified_xml = xml_dom.toprettyxml(indent="    ")
        return prettified_xml

    except Exception as e:
        return None
