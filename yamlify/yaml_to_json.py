import json
import yaml


def yaml_to_json(yaml_data, indent=4, sort_keys=True):
    try:
        json_data = json.dumps(yaml.safe_load(
            yaml_data), indent=indent, sort_keys=sort_keys)
    except Exception as e:
        raise ValueError(f"Error converting YAML data to JSON: {e}")
    return json_data


def yaml_to_json_from_file(filename, indent=4, sort_keys=True):
    with open(filename, 'r') as f:
        yaml_data = ''
        for line in f:
            yaml_data += line
    return yaml_to_json(yaml_data, indent, sort_keys)


def yaml_to_json_from_url(url, indent=4, sort_keys=True):
    import requests

    if '\t' in url:
        raise ValueError(
            'URL contains tab characters, which are not allowed in YAML data.')

    response = requests.get(url)
    yaml_data = response.content
    return yaml_to_json(yaml_data, indent, sort_keys)


def yaml_to_json_to_file(filename, yaml_data, indent=4, sort_keys=True):
    json_data = yaml_to_json(yaml_data, indent, sort_keys)
    with open(filename, 'w') as f:
        f.write(json_data)


def yaml_to_json_to_url(url, yaml_data, indent=4, sort_keys=True):
    import requests
    json_data = yaml_to_json(yaml_data, indent, sort_keys)
    response = requests.post(url, data=json_data)
    return response.content
