import csv
import yaml
import io


def csv_to_yaml(csv_data):
    try:
        yaml_data = []
        input_file = io.StringIO(csv_data)
        csv_reader = csv.DictReader(input_file)
        list_csv = list(csv_reader)
        for row in list_csv:
            yaml_data.append(row)
        return yaml.safe_dump_all(yaml_data)
    except Exception as e:
        return None
