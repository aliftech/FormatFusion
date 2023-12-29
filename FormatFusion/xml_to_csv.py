import csv
import xmltodict
import io


def xml_to_csv(data, tag='root', subtag='item'):
    """Convert XML data to CSV, handling both single and multiple items."""
    try:
        data = data.strip()

        # Parse XML data into a Python dictionary
        xml_data = xmltodict.parse(data)

        # Extract the items (either a list or a single dictionary)
        items = xml_data[tag].get(subtag)
        if not isinstance(items, list):
            items = [items]  # Convert single item to a list

        # Create a CSV writer object
        output = io.StringIO()
        csv_writer = csv.writer(output)

        # Write the header row using keys from the first item
        headers = list(items[0].keys())
        csv_writer.writerow(headers)

        # Write the data rows
        for item in items:
            row = [item[key] for key in headers]
            csv_writer.writerow(row)

        return output.getvalue()  # Return CSV content as string

    except Exception as e:
        return None
