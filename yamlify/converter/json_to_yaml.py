import json
import yaml


def json_to_yaml(json_data):
    try:
        yaml_data = yaml.safe_dump(json.loads(
            json_data), default_flow_style=False)
        return yaml_data
    except Exception as e:
        return None
