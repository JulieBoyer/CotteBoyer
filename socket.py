def read_args():
    # Define parser
    parser = argparse.ArgumentParser(
            description='An implementation of Socket.',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # Define all the arguments
    parser.add_argument('-nc', help='To set the number of clients.', default=1, type = int)
    parser.add_argument('-f', help='Client or server ?', action='store_true')
    parser.add_argument('-p', help='The port.', default=42999)
    # Parse arguments
    args = parser.parse_args()

    # Enable debug
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Number of clients : " + args.nc)
        logger.debug("Status : " + args.nc)
    return args