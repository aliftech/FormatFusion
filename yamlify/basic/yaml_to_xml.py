import yaml
from xml.etree import ElementTree as ET


def yaml_to_xml(data):
    """
    Converts a simple YAML dictionary to XML string.

    Args:
      data: A dictionary representing the YAML data.

    Returns:
      A string containing the generated XML data.
    """
    root = ET.Element("Bard")

    for key, value in data.items():
        child = ET.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                sub_child = ET.SubElement(child, "item")
                sub_child.text = str(item)
        else:
            child.text = str(value)

    return ET.tostring(root, encoding="utf-8")
