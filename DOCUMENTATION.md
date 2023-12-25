# Usage

**Import the necessary modules from FormatFusion**

```python
import FormatFusion as ff
```

**Convert YAML to JSON**

```python
yaml_data = """
   name: John Doe
   age: 30
   city: New York
"""

json_data = ff.yaml_to_json(yaml_data)
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

yaml_data = ff.json_to_yaml(json_data)
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
result = ff.yaml_to_xml(yaml_data)
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

result = ff.json_to_xml(json_data)
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
yaml_data = ff.yaml_to_xml(xml_data)
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
json_data = ff.json_to_xml(xml_data)
return json_data
```

## **IO Function**

The `io` module provides functions for reading data from file or url and save data in expected format

### **read_file function**

This function is used to read data from file. Here is the example of using `read_file` function:

```python
import FormatFusion as ff

filename = 'test.yaml'
data = ff.read_file(filename)
print(data)
```

### **scan_url function**

This function is used to scan URL content, it will return a data with any format, based on its original format. Here is the example how to use `scan_url` function:

```python
import FormatFusion as ff

url = 'example.url.com'
data = ff.scan_url(url)
print(data)
```

### **save_file function**

This function is used to save data into a specific file with specified format (txt, md, html, yml, yaml, json). Here is the example of using `save_file` function:

```python
import FormatFusion as ff

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

# CSV Data Conversion

This function is used to convert yaml, json, and xml data to csv or vice versa.
