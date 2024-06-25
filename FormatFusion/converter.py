import json
import csv
import yaml
import xmltodict
import io
import pandas as pd


class Converter:
    def __init__(self):
        self.data = None

    def from_json(self, data):
        try:
            self.data = json.loads(data)
            return self
        except Exception as e:
            raise ValueError(f"Error converting from JSON: {e}")

    def from_yaml(self, data):
        try:
            self.data = yaml.safe_load(data)
            return self
        except Exception as e:
            raise ValueError(f"Error converting from YAML: {e}")

    def from_csv(self, data):
        try:
            input = io.StringIO(data)
            parse = csv.DictReader(input)
            self.data = list(parse)
            return self
        except Exception as e:
            raise ValueError(f"Error converting from CSV: {e}")

    def from_xml(self, data):
        try:
            self.data = xmltodict.parse(data)
            return self
        except Exception as e:
            raise ValueError(f"Error converting from XML: {e}")

    def to_json(self, indent=4, sort_keys=True):
        try:
            return json.dumps(self.data, indent=indent, sort_keys=sort_keys)
        except Exception as e:
            raise ValueError(f"Error converting to JSON: {e}")

    def to_yaml(self):
        try:
            return yaml.safe_dump(self.data, sort_keys=False)
        except Exception as e:
            raise ValueError(f"Error converting to YAML: {e}")

    def to_csv(self):
        try:
            if not self.data:
                raise ValueError("No data to convert")

            output = io.StringIO()
            csv_writer = csv.writer(output)

            if isinstance(self.data, list) and all(isinstance(d, dict) for d in self.data):
                # Case 1: List of dictionaries (each dictionary is a row)
                headers = list(self.data[0].keys()) if self.data else []
                csv_dict_writer = csv.DictWriter(output, fieldnames=headers)
                csv_dict_writer.writeheader()
                csv_dict_writer.writerows(self.data)
            else:
                # Case 2: List of lists or other iterables (each iterable is a row)
                csv_writer.writerows(self.data)

            return output.getvalue()

        except Exception as e:
            raise ValueError(f"Error converting to CSV: {e}")

    def to_xml(self, root_tag='root'):
        try:
            return xmltodict.unparse({root_tag: self.data}, pretty=True)
        except Exception as e:
            raise ValueError(f"Error converting to XML: {e}")

    def to_dataframe(self):
        try:
            if isinstance(self.data, list) and all(isinstance(i, dict) for i in self.data):
                return pd.DataFrame(self.data)
            elif isinstance(self.data, dict):
                return pd.DataFrame([self.data])
            else:
                raise ValueError(
                    "Data is not in a format that can be converted to a DataFrame")
        except Exception as e:
            raise ValueError(f"Error converting to DataFrame: {e}")

    def from_dataframe(self, data):
        try:
            self.data = data.to_dict(orient='records')
            return self
        except Exception as e:
            raise ValueError(f"Error converting from DataFrame: {e}")
