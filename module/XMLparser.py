import xml.etree.ElementTree as ET
from xmldiff import main, formatting

def write_to_xml(data, file_name):
    xml_data = ET.tostring(data)
    myfile = open(file_name, "w")
    myfile.write(xml_data)

def create_xml_data(data, file_name):
    data_tag = ET.Element("data")
    items_tag = ET.SubElement(data_tag, "items")

    for x in data:
        tag = ET.SubElement(items_tag, "item")
        sub_tag = ET.SubElement(tag, "tag")
        sub_tag.text = x["tag"]
        attr_obj = x['attributes']

        for z in attr_obj:
            attr_tag = ET.SubElement(tag, "attributes")
            attr_tag.set("name", z[0])
            attr_tag.text = z[1]

    write_to_xml(data_tag, file_name)

def xml_difference(original, to_compare):
    diff = main.diff_files(original, to_compare, formatter=formatting.XMLFormatter())

    return diff
