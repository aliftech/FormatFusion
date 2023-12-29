# Usage

**Import the necessary modules from FormatFusion**

```python
import FormatFusion as ff
```

**Convert YAML to JSON**

```python
from FormatFusion.yaml_to_json import yaml_to_json

yaml_data = """
   name: John Doe
   age: 30
   city: New York
"""

json_data = yaml_to_json(yaml_data)
print(json_data)

```

The code above will returned

```json
{
  "age": 30,
  "city": "New York",
  "name": "John Doe"
}
```

**Convert JSON to YAML**

```python
from FormatFusion.json_to_yaml import json_to_yaml

json_data = """{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}"""

yaml_data = json_to_yaml(json_data)
print(yaml_data)

```

The code above will returned

```yaml
age: 30
city: New York
name: John Doe
```

**Convert YAML to XML**

```python
from FormatFusion.yaml_to_xml import yaml_to_xml

yaml_data = """
   name: John Doe
   age: 30
   address:
      street: Jalan Merdeka
      city: Jakarta
      province: DKI Jakarta
"""
xml = yaml_to_xml(yaml_data)
print(xml)
```

The code above will returned

```xml
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
```

**Convert JSON to XML**

```python
from FormatFusion.json_to_xml import json_to_xml

json_data = """{
   "name": "John Doe",
   "age": 30,
   "address": {
         "street": "Jalan Merdeka",
         "city": "Jakarta",
         "province": "DKI Jakarta"
   }
}"""
xml = json_to_xml(json_data)
print(xml)
```

The code above will returned

```xml
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
```

**Convert XML to YAML**

```python
from FormatFusion.xml_to_yaml import xml_to_yaml

xml_data = """
   <?xml version="1.0" ?>
   <user>
      <name>John Doe</name>
      <age>30</age>
      <address>
         <street>Jalan Merdeka</street>
         <city>Jakarta</city>
         <province>DKI Jakarta</province>
      </address>
   </user>
"""
yaml_data = xml_to_yaml(xml_data)
print(yaml_data)
```

The code above will returned

```yaml
user:
  address:
    city: Jakarta
    province: DKI Jakarta
    street: Jalan Merdeka
  age: "30"
  name: John Doe
```

**Convert XML to JSON**

```python
from FormatFusion.xml_to_json import xml_to_json

xml_data = """
   <?xml version="1.0" ?>
   <user>
      <name>John Doe</name>
      <age>30</age>
      <address>
         <street>Jalan Merdeka</street>
         <city>Jakarta</city>
         <province>DKI Jakarta</province>
      </address>
   </user>
"""
json_data = xml_to_json(xml_data)
print(json_data)
```

The code above will returned

```json
{
  "user": {
    "address": {
      "city": "Jakarta",
      "province": "DKI Jakarta",
      "street": "Jalan Merdeka"
    },
    "age": "30",
    "name": "John Doe"
  }
}
```

## **IO Function**

The `io` module provides functions for reading data from file or url and save data in expected format

### **read_file function**

This function is used to read data from file. Here is the example of using `read_file` function:

```python
from FormatFusion import reader

data = reader.read_file('data.yaml')
print(data)

```

### **scan_url function**

This function is used to scan URL content, it will return a data with any format, based on its original format. Here is the example how to use `scan_url` function:

```python
from FormatFusion import reader

yaml_data = reader.scan_url(
    "https://github.com/aliftech/FormatFusion/raw/master/test/test.yaml")

print(yaml_data)
```

### **save_file function**

This function is used to save data into a specific file with specified format (txt, md, html, yml, yaml, json). Here is the example of using `save_file` function:

```python
from FormatFusion import reader

yaml_data = reader.scan_url(
    "https://github.com/aliftech/FormatFusion/raw/master/test/test.yaml")

reader.save_file('data.yaml', yaml_data)
```

# CSV Data Conversion

This function is used to convert yaml, json, and xml data to csv or vice versa.

Here is an example how you can use this functionality:

### **YAML To CSV**

This function is used to convert yaml data to csv format. Here is the example of using this function.

```python
from FormatFusion.yaml_to_csv import yaml_to_csv

yaml_data = """
   name: John Doe
   age: 30
   address:
      street: Jalan Merdeka
      city: Jakarta
      province: DKI Jakarta
"""
csv_data = yaml_to_csv(yaml_data)
print(csv_data)
```

The code above will returned

```csv
name,age,address
John Doe,30,"{'street': 'Jalan Merdeka', 'city': 'Jakarta', 'province': 'DKI Jakarta'}"
```

### **JSON To CSV**

This function is used to convert json data into csv format.

```python
from FormatFusion.json_to_csv import json_to_csv

json_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
csv_data = json_to_csv(json_data)
print(csv_data)
```

The code above will returned

```csv
name,age,city
John Doe,30,New York
```

### **XML To CSV**

This function is used to convert xml data into csv format.

```python
from FormatFusion.xml_to_csv import xml_to_csv

xml_data = """
   <?xml version="1.0" ?>
   <user>
      <item>
        <name>John Doe</name>
        <age>30</age>
        <address>
            <street>Jalan Merdeka</street>
            <city>Jakarta</city>
            <province>DKI Jakarta</province>
        </address>
      </item>
   </user>
"""
csv_data = xml_to_csv(xml_data, "user", "item")
print(csv_data)
```

The code above will returned

```csv
name,age,address
John Doe,30,"{'street': 'Jalan Merdeka', 'city': 'Jakarta', 'province': 'DKI Jakarta'}"
```

Here is the explanation of the code above:

- in the `csv_data = xml_to_csv(xml_data, "user", "item")` - the xml_data is the data that will be converted to cvs data.
- "user" - this is the tag name that will be used as a targeted data.
- "item" - this is the child tag name inside "user" which contains individual user information.

### **CSV To YAML**

This function is used to convert csv data into yaml format.

```python
from FormatFusion.csv_to_yaml import csv_to_yaml

csv_data = """name,age,city
John Doe,30,New York
"""
yaml_data = csv_to_yaml(csv_data)
print(yaml_data)
```

The code above will returned

```yaml
age: "30"
city: New York
name: John Doe
```

### **CSV To JSON**

This function is used to convert csv data into json format.

```python
from FormatFusion.csv_to_json import csv_to_json

csv_data = """name,age,city
John Doe,30,New York
Alice,25,Jakarta
"""
json_data = csv_to_json(csv_data)
print(json_data)
```

The code above will returned

```json
[
  { "name": "John Doe", "age": "30", "city": "New York" },
  { "name": "Alice", "age": "25", "city": "Jakarta" }
]
```

### **CSV To XML**

This function is used to convert csv data into xml format.

```python
from FormatFusion.csv_to_xml import csv_to_xml

csv_data = """name,age,city
John Doe,30,New York
Alice,25,Jakarta
"""
xml_data = csv_to_xml(csv_data)
print(xml_data)
```

The code above will returned

```xml
<?xml version="1.0" ?>
<root>
  <item>
    <name>John Doe</name>
    <age>30</age>
    <city>New York</city>
  </item>
  <item>
    <name>Alice</name>
    <age>25</age>
    <city>Jakarta</city>
  </item>
</root>
```
