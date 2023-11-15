import json
import yaml


def json_to_yaml(json_data):
    try:
        yaml_data = yaml.safe_dump(json.loads(
            json_data), default_flow_style=False)
    except Exception as e:
        raise ValueError(f"Error converting JSON data to YAML: {e}")
    return yaml_data
