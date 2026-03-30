import subprocess

def run_scan(target, port=None):
    command = ['nmap', '-oX', '-', target]
    if port:
        command.extend(['-p', str(port)])
    else:
        print(f'Scanning {target} on all ports...')
    result = subprocess.run(command, capture_output=True, text=True)
    print(f'Debug stdout: {repr(result.stdout)}')
    print(f'Debug stderr: {repr(result.stderr)}')
    
    return result.stdout
