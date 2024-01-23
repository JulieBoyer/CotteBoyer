import logging
import argparse
import socket

HANDSHAKE_MSG = b"Hello"
HANDSHAKE_REPLY = b"Hi"
END_TAG = b'__END__'

def read_args():
    # Define parser
    parser = argparse.ArgumentParser(
            description='An implementation of Socket.',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # Define all the arguments
    parser.add_argument('-nc', help='To set the number of clients.', default=1, type = int)
    parser.add_argument('-i', help='Path for input file.')
    parser.add_argument('-s', help='Run as server', action='store_true')
    parser.add_argument('-p', help='The port.', default=34000)
    # Parse arguments
    args = parser.parse_args()

    # Enable debug
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug("Number of clients : " +str( args.nc))
    if args.s:
        logger.debug("Status : server" )
    else:
        logger.debug("Status : client")
    logger.debug("Port : " + str(args.p))
    return args

args = read_args()

def run_as_client():
    
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    server = ("localhost", args.p)
    s.connect(server)
    sent = s.send(HANDSHAKE_MSG)
    if sent == 0 :
        raise RuntimeError("Impossible to send")
    reply = s.recv(len(HANDSHAKE_REPLY))
    if reply != HANDSHAKE_REPLY:
        raise RuntimeError("bad hanshake")
    print(reply)
    

def run_as_server():
    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind(("", args.p))
    # become a server socket
    serversocket.listen()
    (client_socket,addr)=serversocket.accept()
    text=client_socket.recv(len(HANDSHAKE_MSG))
    client_socket.send(HANDSHAKE_REPLY)
    print(text)

if args.s:
    run_as_server()
else:
    run_as_client()