import socket
import sys


def usage():
    print("usage: \n python portscan.py local => for local port scan \n \
python portscan.py <website.com> => for scanning the site\n")


def portScan(host, startPort, endPort):
    openports = 0
    for port in range(startPort, endPort + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                service = socket.getservbyport(port, 'tcp')
                openports += 1
                print(f"host: {host}")
                print(f"Port: {port}")
                print("Protocol: TCP")
                print(f"Service: {service}")
                print("Status: Open \n")

        except socket.error:
            pass

        finally:
            sock.close()
    return openports


def getLocalIP():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(('8.8.8.8', 80))
        localIP = sock.getsockname()[0]
    except socket.error:
        localIP = '127.0.0.1'
    finally:
        sock.close()
    return localIP


localIP = getLocalIP()

startPort = 1
endPort = 100

if len(sys.argv) <= 1:
    usage()
else:
    if sys.argv[1] == "local":
        open_ports = portScan(localIP, startPort, endPort)
        print(f"{open_ports} ports open and {100 - open_ports} ports closed")
    else:
        host = sys.argv[1]
        print(f"scanning {host} started wait a minute...\n")
        open_ports = portScan(sys.argv[1], startPort, endPort)
        print(f"{open_ports} ports open and {100 - open_ports} ports closed")
