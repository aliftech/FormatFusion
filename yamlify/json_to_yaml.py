import json
import yaml


def json_to_yaml(json_data):
    try:
        yaml_data = yaml.safe_dump(json.loads(
            json_data), default_flow_style=False)
    except Exception as e:
        raise ValueError(f"Error converting JSON data to YAML: {e}")
    return yaml_data


def json_to_yaml_from_file(filename, indent=4, sort_keys=True):
    with open(filename, 'r') as file:
        json_data = file.read()
    return json_to_yaml(json_data, indent, sort_keys)


def json_to_yaml_from_url(url, indent=4, sort_keys=True):
    import requests

    if '\t' in url:
        raise ValueError("URL cannot contain tabs")
    response = requests.get(url)
    if not response.ok:
        raise ValueError(
            'Failed to fetch URL. HTTP status code: {}'.format(response.status_code))
    return json_to_yaml(response.content, indent, sort_keys)


def json_to_yaml_to_file(filename, json_data, indent=4, sort_keys=True):
    yaml_data = json_to_yaml(json_data, indent, sort_keys)
    with open(filename, 'w') as file:
        file.write(yaml_data)
