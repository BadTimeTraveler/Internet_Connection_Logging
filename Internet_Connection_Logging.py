# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:43:25 2021

@author: jdoyl
"""

import socket
import logging
from time import sleep


def internet(host="8.8.8.8", port=53, timeout=2):
    """
	https://stackoverflow.com/questions/3764291/checking-network-connection
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
#        logging.info('Connected')
        return True
    except socket.error as ex:
#        logging.error(ex)
        logging.error('Could not connect to 8.8.8.8 (google.com)- No Internet Connection')
        return False


logging.basicConfig(filename='InternetConnection.log',
                    format='[%(levelname)s] - %(asctime)s - %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    level=logging.INFO)


print("Starting log, querying Google's public dns server (8.8.8.8) every 15 seconds")
print('To exit, press "crtl+C"')
logging.info('Starting log')

while True:
    try:
        internet()
        sleep(15)
    except KeyboardInterrupt:
        logging.info('Exit via KeyboardInterrupt')
        print('Exiting')
        break