import csv
import io
import json


def csv_to_json(csv_data):
    try:
        json_data = []
        # Create file-like object from string
        input_file = io.StringIO(csv_data)
        csv_reader = csv.DictReader(input_file)
        list_csv = list(csv_reader)
        for row in list_csv:
            json_data.append(row)

        return json.dumps(json_data)

    except csv.Error as e:
        return None


csv_data = "name,age,city\nAlice,30,New York\nBruce,45,Detroit"
xml_data = csv_to_json(csv_data)
print(xml_data)
