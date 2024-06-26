from FormatFusion.converter import Converter

converter = Converter()
data_json = '''
{
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "Jalan Merdeka",
        "city": "Jakarta",
        "province": "DKI Jakarta"
    }
}
'''

yaml_result = converter.to_dataframe(data_json)
print(yaml_result)
