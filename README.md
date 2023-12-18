# **YAMLify**

## About YAMLify

Effortlessly Convert Between Data Formats with YAMLify
YAMLify is your one-stop solution for seamless conversion between YAML, JSON, and XML formats. This user-friendly tool empowers developers, data analysts, and anyone working with data to:

**Effortlessly Transform Data:**

- **YAML to JSON:** Preserve data integrity and structure with ease.
- **JSON to YAML:** Maintain accuracy and adhere to YAML syntax flawlessly.
- **XML to JSON:** Transform data from diverse sources into JSON for analysis.
- **XML to YAML:** Convert XML documents into YAML format for configuration or manipulation.
- **YAML to XML:** Export YAML data as structured XML documents.
- **JSON to XML:** Share data effortlessly using standardized XML format.
  Boost Productivity and Data Integrity:

Save time and effort: Automate data conversion tasks and focus on what matters most.
Minimize errors: Robust error handling identifies and reports discrepancies for efficient troubleshooting.
Simplify data manipulation: Seamlessly convert between formats to use the tools and languages you love.
Streamline data exchange: Share data effortlessly between applications and systems that utilize different formats.
Who benefits from YAMLify?

- **Developers:** Convert configuration files and application data between formats with ease.
- **Data Analysts:** Transform data from various sources into JSON for seamless analysis and visualization.
- **Technical Professionals:** Work with data in different formats smoothly and confidently.

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

**Convert YAML to XML**

```python
yaml_data = """
   name: John Doe
   age: 30
   address:
      street: Jalan Merdeka
      city: Jakarta
      province: DKI Jakarta
"""
result = yf.yaml_to_xml(yaml_data)
return result
```

**Convert JSON to XML**

```python
json_data = """{
   "name": "John Doe",
   "age": 30,
   "address": {
         "street": "Jalan Merdeka",
         "city": "Jakarta",
         "province": "DKI Jakarta"
   }
}"""

result = yf.json_to_xml(json_data)
return result
```

**Convert XML to YAML**

```python
xml_data = """
   <?xml version="1.0" ?>
   <root>
      <name>John Doe</name>
      <age>30</age>
      <address>
         <street>Jalan Merdeka</street>
         <city>Jakarta</city>
         <province>DKI Jakarta</province>
      </address>
   </root>
"""
yaml_data = yf.yaml_to_xml(xml_data)
return yaml_data
```

**Convert XML to JSON**

```python
xml_data = """
   <?xml version="1.0" ?>
   <root>
      <name>John Doe</name>
      <age>30</age>
      <address>
         <street>Jalan Merdeka</street>
         <city>Jakarta</city>
         <province>DKI Jakarta</province>
      </address>
   </root>
"""
json_data = yf.json_to_xml(xml_data)
return json_data
```

## **IO Function**

The `io` module provides functions for reading data from file or url and save data in expected format

### **read_file function**

This function is used to read data from file. Here is the example of using `read_file` function:

```python
import yamlify as yf

filename = 'test.yaml'
data = yf.read_file(filename)
print(data)
```

### **scan_url function**

This function is used to scan URL content, it will return a data with any format, based on its original format. Here is the example how to use `scan_url` function:

```python
import yamlify as yf

url = 'example.url.com'
data = yf.scan_url(url)
print(data)
```

### **save_file function**

This function is used to save data into a specific file with specified format (txt, md, html, yml, yaml, json). Here is the example of using `save_file` function:

```python
import yamlify as yf

data = """name: John Doe
age: 30
address:
  street: Jalan Merdeka
  city: Jakarta
  province: DKI Jakarta
"""

filename = "testing.yaml"
save_file(filename, data)
```

## Our Community

**Blog**: <a href="https://yamlify.blogspot.com/">https://yamlify.blogspot.com</a>
