import socket


# TODO: make it for both ; open host and
# local host/machine : read args and depend on that


def portScan(host, startPort, endPort):
    for port in range(startPort, endPort + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                service = socket.getservbyport(port, 'tcp')
                print(f"Port: {port}")
                # TODO:here why the protocol is tcp what if udp
                print("Protocol: TCP")
                print(f"Service: {service}")
                print("Status: Open \n")

        except socket.error:
            pass

        finally:
            sock.close()


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

# Scan the local machine's ports
startPort = 1
endPort = 100

portScan(localIP, startPort, endPort)

host = 'website.com'
startPort = 1
endPort = 100

#portScan(host, startPort, endPort)

