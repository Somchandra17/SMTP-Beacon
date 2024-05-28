import smtplib
import socket

def check_smtp(ip, port=25):
    try:
        server = smtplib.SMTP(ip, port, timeout=10)
        server.quit()
        return True
    except (smtplib.SMTPConnectError, socket.timeout, socket.error):
        return False

def check_ips_from_file(file_path):
    with open(file_path, 'r') as file:
        ips = file.readlines()
    
    results = {}
    for ip in ips:
        ip = ip.strip()
        if not ip:
            continue
        is_open = check_smtp(ip)
        results[ip] = is_open
        print(f"{ip}: {'Open' if is_open else 'Closed'}")
    
    return results

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Check SMTP port 25 on a list of IPs.')
    parser.add_argument('file', type=str, help='Path to the text file containing IP addresses')
    
    args = parser.parse_args()
    check_ips_from_file(args.file)
