import xmltodict
import yaml


def xml_to_yaml(data):
    try:
        # Remove leading whitespace or newline characters
        data = data.strip()

        xml = xmltodict.parse(data)
        yaml_data = yaml.dump(xml, default_flow_style=False)
        return yaml_data

    except Exception as e:
        return None
