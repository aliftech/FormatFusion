import json
import csv
import io


def json_to_csv(json_data):
    try:
        if isinstance(json_data, list):
            data = json_data
        else:  # Assume a single dictionary
            data = [json_data]

        headers = list(data[0].keys())

        output = io.StringIO()  # Create an in-memory file-like object
        csv_writer = csv.DictWriter(output, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(data)

        return output.getvalue()  # Return the CSV data as a string

    except json.JSONDecodeError:
        return None
    except csv.Error as e:
        return None
