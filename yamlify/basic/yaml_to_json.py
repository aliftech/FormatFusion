import json
import yaml


def yaml_to_json(yaml_data, indent=4, sort_keys=True):
    try:
        json_data = json.dumps(yaml.safe_load(
            yaml_data), indent=indent, sort_keys=sort_keys)
    except Exception as e:
        raise ValueError(f"Error converting YAML data to JSON: {e}")
    return json_data
