import yaml
import csv
import io


def yaml_to_csv(data):
    """Convert YAML data to CSV."""
    try:
        yaml_data = list(yaml.safe_load_all(data))  # Load all YAML documents
        # Extract headers from first document
        headers = list(yaml_data[0].keys())

        output = io.StringIO()   # Create in-memory file-like object
        csv_writer = csv.DictWriter(output, fieldnames=headers)
        csv_writer.writeheader()  # Write CSV header
        # Write each YAML document as a CSV row
        csv_writer.writerows(yaml_data)

        return output.getvalue()  # Return CSV content as string
    except Exception as e:
        return None
