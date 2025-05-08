import socket
import threading

def scan(ip, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"[+] مفتوح: {ip}:{port}")
    except:
        pass
    s.close()

def main():
    ip = input("IP الهدف: ")
    for port in range(1, 1025):
        t = threading.Thread(target=scan, args=(ip, port))
        t.start()

if __name__ == "__main__":
    main()
