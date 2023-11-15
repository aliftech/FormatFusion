from yaml_converter.yaml_to_json import yaml_to_json

yaml_data = """
    name: John Doe
    age: 30
    address:
        street: Jalan Merdeka
        city: Jakarta
        province: DKI Jakarta
    """

json_data = yaml_to_json(yaml_data)

print(json_data)
