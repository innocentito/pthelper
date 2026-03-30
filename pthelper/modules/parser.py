import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    tree = ET.fromstring(xml_string)

    ports = []
    for port in tree.findall('.//port'):
        if port.get('state') == 'open':
            ports.append({'port': port.get('portid'), 'service': port.find('service').get('name')})
    return ports
            