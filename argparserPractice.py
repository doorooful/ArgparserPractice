import argparse

def myFunction(args):
    print(args.host)
    print(args.port)

def main():
    argparser = argparse.ArgumentParser(
        description='Test app'
    )
    argparser.add_argument(
        '--host',
        metavar='H',
        default='localhost',
        help='Test host input (default: 127.0.0.1)'
    )
    argparser.add_argument(
        '-p',
        '--port',
        metavar='P',
        default=2000,
        type=int,
        help='Test port input (default:8080)'
    )
    args = argparser.parse_args()

    myFunction(args)

    
if __name__ == "__main__":
    main()