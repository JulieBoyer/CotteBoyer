import logging
import argparse
import socket

def read_args():
    # Define parser
    parser = argparse.ArgumentParser(
            description='An implementation of Socket.',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # Define all the arguments
    parser.add_argument('-nc', help='To set the number of clients.', default=1, type = int)
    parser.add_argument('-f', help='Client or server ?', action='store_true')
    parser.add_argument('-p', help='The port.', default=34000)
    # Parse arguments
    args = parser.parse_args()

    # Enable debug
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Number of clients : " + args.nc)
        logger.debug("Status : " + args.nc)
        logger.debug("Port : " + args.p)
    return args

def main():
    args = read_args()
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    s.connect(("local host", args.p))
    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind((socket.gethostname(), 80))
    # become a server socket
    serversocket.listen(5)