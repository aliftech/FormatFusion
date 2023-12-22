import json
import xmltodict


def xml_to_json(data, indent=4, sort_keys=True):
    try:
        data = data.strip()

        xml_data = xmltodict.parse(data)
        result = json.dumps(xml_data, indent=indent, sort_keys=sort_keys)
        return result

    except Exception as e:
        return None
