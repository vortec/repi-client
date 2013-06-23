import argparse
import redis
from repi_client import RepiClient

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name of Repi client', type=str)
    parser.add_argument('-H', '--host', help='Redis host (default: localhost)', type=str, default='localhost')
    parser.add_argument('-p', '--port', help='Redis port (default: 6379)', type=int, default=6379)
    parser.add_argument('-n', '--namespace', help='Redis namespace (default: repi)', type=str, default='repi')
    parser.add_argument('-i', '--info-channel', help='Redis general PubSub channel (default: cluster)', type=str, default='cluster')
    args = parser.parse_args()
    
    name = args.name
    host = args.host
    port = args.port
    namespace = args.namespace
    info_channel = args.info_channel

    if not namespace.endswith(':'):
        namespace = '{}:'.format(namespace)

    r = redis.Redis(host=host, port=port)
    repi_client = RepiClient(r, name, namespace=namespace, info_channel=info_channel)
    try:
        repi_client.run()
    except KeyboardInterrupt, err:
        repi_client.stop()



if __name__ == '__main__':
    main()
