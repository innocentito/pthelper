import argparse
from modules.scanner import run_scan
from modules.parser import parse_xml

def main():
    parser = argparse.ArgumentParser(description='A pentest helper tool.')
    subparsers = parser.add_subparsers(dest='command')
    scan_parser = subparsers.add_parser('scan')
    scan_parser.add_argument('target', type=str, help='The target to scan.')
    scan_parser.add_argument('--port', type=int)
    args = parser.parse_args()

    if args.command == 'scan':
        xml_output = run_scan(args.target, port=args.port)
        print(f'DEBUG: {xml_output[:200]}')  # erste 200 zeichen
        ports = parse_xml(xml_output)
        print(f'DEBUG ports: {ports}')

if __name__ == '__main__':
    main()