import yaml
import xmltodict
import xml.dom.minidom
from yaml import FullLoader


def yaml_to_xml(data):
    try:
        yaml_data = yaml.load(data, Loader=FullLoader)

        # Wrap the YAML data with a root element if it has multiple keys
        if isinstance(yaml_data, dict) and len(yaml_data) > 1:
            yaml_data = {"root": yaml_data}

        result = xmltodict.unparse(yaml_data)

        xml_dom = xml.dom.minidom.parseString(result)
        # Adjust the indentation as needed
        prettified_xml = xml_dom.toprettyxml(indent="    ")
    
    except Exception as e:
        raise ValueError(f"Error converting YAML data to XML: {e}")
    return prettified_xml
