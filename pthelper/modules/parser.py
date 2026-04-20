import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    tree = ET.fromstring(xml_string)

    ports = []
    for port in tree.findall('.//port'):
        service = port.find('service')
        service_name = service.get('name') if service is not None else 'unknown'
        if port.find('state').get('state') == 'open': 
            ports.append({'port': port.get('portid'), 'service': service_name})
    return ports