import argparse
from modules.scanner import run_scan

def main():
    parser = argparse.ArgumentParser(description='A pentest helper tool.')
    subparsers = parser.add_subparsers(dest='command')
    scan_parser = subparsers.add_parser('scan')
    scan_parser.add_argument('target', type=str, help='The target to scan.')
    scan_parser.add_argument('--port', type=int)
    args = parser.parse_args()

    if args.command == 'scan':
        result = run_scan(args.target, port=args.port)
        print(result)

if __name__ == '__main__':
    main()