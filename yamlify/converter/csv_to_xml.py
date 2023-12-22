import csv
import io
import xml.dom.minidom
import xml.etree.ElementTree as ET


def csv_to_xml(csv_data):
    try:
        root = ET.Element("root")  # Create a placeholder root

        input_file = io.StringIO(csv_data)
        csv_reader = csv.DictReader(input_file)
        for row in csv_reader:
            item = ET.Element("item")  # Create a separate root for each item
            for key, value in row.items():
                ET.SubElement(item, key).text = value
            root.append(item)  # Append each item as a top-level element

        xml_str = ET.tostring(root, encoding="unicode")

        # Prettify the XML
        xml_dom = xml.dom.minidom.parseString(xml_str)
        prettified_xml = xml_dom.toprettyxml(indent="  ")

        return prettified_xml
    except Exception as e:
        return None
