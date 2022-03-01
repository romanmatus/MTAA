import sipfullproxy #SOURCE : https://github.com/tirfil/PySipFullProxy
import time
import socket
import logging
import socketserver


def log():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    logging.info(sipfullproxy.hostname)
    logging.info(sipfullproxy.ipaddress)


def info():
    print("proxy server beží na IP: <%s:%s>" % (sipfullproxy.ipaddress, sipfullproxy.PORT))

if __name__ == "__main__":
    sipfullproxy.hostname = socket.gethostname()
    sipfullproxy.ipaddress = socket.gethostbyname(sipfullproxy.hostname)
    # log()
    info()
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipfullproxy.ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "SIP 2.0 UDP %s:%d" % (sipfullproxy.ipaddress, sipfullproxy.PORT)
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()
