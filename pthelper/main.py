import argparse
from modules.parser import parse_xml
from modules.scanner import run_scan

def main():
    parser = argparse.ArgumentParser(description='A pentest helper tool.')
    subparsers = parser.add_subparsers(dest='command')
    scan_parser = subparsers.add_parser('scan')
    scan_parser.add_argument('target', type=str, help='The target to scan.')
    scan_parser.add_argument('--port', type=int)
    args = parser.parse_args()

    if args.command == 'scan':
        xml_output = run_scan(args.target, port=args.port)
        ports = parse_xml(xml_output)
        for port in ports:
            print(f"[+] Port {port['port']} - {port['service']}")

if __name__ == '__main__':
    main()