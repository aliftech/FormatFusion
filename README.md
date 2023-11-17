# **YAMLify**

## About YAMLify

YAMLify is a versatile and user-friendly tool that facilitates seamless conversion between YAML and JSON data formats. It offers a comprehensive set of features that cater to diverse needs, making it an invaluable asset for developers, data analysts, and anyone working with these data formats.

**Core Functionalities:**

- YAML to JSON Conversion: YAMLify effortlessly transforms YAML data into JSON format, ensuring data integrity and preserving the original structure.

- JSON to YAML Conversion: Conversely, YAMLify adeptly converts JSON data into YAML format, maintaining data accuracy and adhering to YAML syntax.

- Error Handling: YAMLify employs robust error handling mechanisms to identify and report parsing errors, providing valuable insights into data discrepancies.

- Customization Options: YAMLify empowers users to customize the conversion process by tailoring indentation levels, sorting keys, and adjusting other parameters to suit specific requirements.

- Data Input/Output Flexibility: YAMLify supports a variety of data input and output options, enabling users to convert data from and to files, URLs, and strings.

**Benefits of Using YAMLify:**

- Enhanced Productivity: YAMLify streamlines data conversion tasks, saving time and effort, allowing users to focus on core development and analysis activities.

- Improved Data Integrity: YAMLify ensures the accuracy and consistency of data throughout the conversion process, minimizing the risk of data corruption.

- Simplified Data Manipulation: YAMLify facilitates data manipulation by enabling seamless conversion between YAML and JSON formats, catering to various programming languages and data analysis tools.

- Streamlined Data Exchange: YAMLify promotes seamless data exchange between different systems and applications that utilize YAML and JSON formats.

**Target Audience:**

- YAMLify is designed for a broad range of users, including:

  - Developers: YAMLify empowers developers to effortlessly convert configuration files and application data between YAML and JSON formats, enhancing development efficiency.

  - Data Analysts: Data analysts can utilize YAMLify to seamlessly transform data from various sources into JSON format for further analysis and visualization.

  - Technical Professionals: YAMLify serves as a valuable tool for technical professionals working with data in different formats, ensuring smooth data exchange and manipulation.

Overall, YAMLify stands out as a powerful and versatile tool that simplifies data conversion tasks, promotes data integrity, and enhances productivity for a wide range of users.

# YAMLify Setup Instructions

## Prerequisites

- A computer with Python installed
- pip installed

## Installation

1. Open a terminal or command prompt.
2. Run the following command:
   ```bash
   pip install yamlify
   ```

## Usage

**Import the necessary modules from yamlify**

```python
import yamlify as yf
```


**Convert YAML to JSON**
```python
yaml_data = """
   name: John Doe
   age: 30
   city: New York
"""

json_data = yf.yaml_to_json(yaml_data)
print(json_data)
```


**Convert YAML to JSON from file**

```python
yaml_file = 'test.yaml'
json_data = yaml_to_json_from_file(yaml_file)
print(json_data)
```


**Convert YAML to JSON from URL**

```python
url = "https://raw.githubusercontent.com/jamiew/yamlify/master/tests/test.yaml"
json_data = yaml_to_json_from_url(url)
print(json_data)
```


**Convert YAML to JSON File**

```python
file_name_ = 'test.json'
yaml_data = """
   name: John Doe
   age: 30
   city: New York
"""

yaml_to_json_to_file(file_name, yaml_data)
```


**Convert JSON to YAML**

```python
json_data = 
{
   "name": "John Doe",
   "age": 30,
   "city": "New York"
}

yaml_data = yf.json_to_yaml(json_data)
print(yaml_data)
```
