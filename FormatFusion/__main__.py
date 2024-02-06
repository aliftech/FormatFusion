import os
import reader
import csv_to_json
import csv_to_xml
import csv_to_yaml
import json_to_csv
import json_to_xml
import json_to_yaml
import xml_to_csv
import xml_to_json
import xml_to_yaml
import yaml_to_csv
import yaml_to_json
import yaml_to_xml


import os
import argparse


banner = """
.--.._       _..--.
/   _.-'''-.  `-._   \\
|          |       |
|  F O R M A T  |  F U S I O N  |
|          |       |
\\   `-._.-'   `-._/ /
 `.-----.---...---.-----'
"""


def convert_file(input_file, output_file):
    """
    Mengubah file dari format input ke format output.

    Args:
        input_file (str): Jalur file input.
        output_file (str): Jalur file output.

    Returns:
        None.
    """

    if not os.path.exists(input_file):
        print(f"File input '{input_file}' not found.")

    content = reader.read_file(input_file)
    if content is False:
        print("Unsupported file input format.")

    input_format = reader.validate_format(input_file)
    if input_format is False:
        print("Unsupported file input format.")
    else:
        output_format = reader.validate_format(output_file)
        if output_format is False:
            print("Unsupported file output format.")
        else:
            if input_format == "csv" and output_format == "json":
                converted_data = csv_to_json.csv_to_json(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "csv" and output_format == "xml":
                converted_data = csv_to_xml.csv_to_xml(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "csv" and output_format == "yaml":
                converted_data = csv_to_yaml.csv_to_yaml(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "json" and output_format == "csv":
                converted_data = json_to_csv.json_to_csv(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "json" and output_format == "xml":
                converted_data = json_to_xml.json_to_xml(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "json" and output_format == "yaml":
                converted_data = json_to_yaml.json_to_yaml(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "xml" and output_format == "csv":
                converted_data = xml_to_csv.xml_to_csv(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "xml" and output_format == "json":
                converted_data = xml_to_json.xml_to_json(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "xml" and output_format == "yaml":
                converted_data = xml_to_yaml.xml_to_yaml(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "yaml" and output_format == "csv":
                converted_data = yaml_to_csv.yaml_to_csv(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "yaml" and output_format == "json":
                converted_data = yaml_to_json.yaml_to_json(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            elif input_format == "yaml" and output_format == "xml":
                converted_data = yaml_to_xml.yaml_to_xml(content)
                reader.save_file(output_file, converted_data)
                print(f"Converting {input_file} into {output_file} is success")
            else:
                print(
                    f"The {input_file} format or {output_file} format is not supported.")


def main():
    """
    Fungsi utama CLI.
    """
    print(banner)

    parser = argparse.ArgumentParser(
        description="Convert files to another file format.")
    parser.add_argument("input_file", help="path input file.")
    parser.add_argument("output_file", help="path output file.")

    args = parser.parse_args()

    convert_file(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
