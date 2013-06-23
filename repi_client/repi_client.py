import json
import pip_utils


class RepiClient(object):
    def __init__(self, r, name, namespace='repi:', info_channel='cluster'):
        self.redis = r
        self.name = name
        self.namespace = namespace
        self.info_channel = info_channel

        self.pubsub = self.redis.pubsub()
        self.subscribe(self.info_channel)
        self.subscribe(self.name)


    def publish(self, command, data=None):
        channel = self._prefixChannel(self.info_channel)
        message = {
            'client': self.name,
            'command': command,
            'data': data
        }
        json_message = json.dumps(message)
        self.redis.publish(channel, json_message)


    def subscribe(self, channel):
        channel = self._prefixChannel(channel)
        self.pubsub.subscribe(channel)

    def unsubscribe(self, channel):
        channel = self._prefixChannel(channel)
        self.pubsub.unsubscribe(channel)


    def run(self):
        for item in self.pubsub.listen():
            if item['type'] != 'message':
                continue

            # Decode JSON
            channel, json_message = item['channel'], item['data']
            try:
                message = json.loads(json_message)
            except ValueError, err:
                print 'Invalid JSON.'
                continue

            # Sanity check
            if not {'client', 'command', 'data'}.issubset(message):
                print 'Invalid protocol.'
                continue

            # Handle incoming request
            if message['command'] == 'PING':
                self.publish('PONG')
            elif message['command'] == 'PACKAGE_LIST':
                self.publish('MY_PACKAGE_LIST', pip_utils.get_package_information())
            elif message['command'] == 'INSTALL':
                data = message['data']
                self.publish('INSTALLING', data)
                try:
                    pip_utils.install_package(data['package'], data['version'])
                    self.publish('INSTALLED', data)
                except Exception, err:
                    self.publish('ERROR', {'error': str(err)})

    def stop(self):
        self.unsubscribe(self.info_channel)
        self.unsubscribe(self.name)


    def _prefixChannel(self, channel):
        return '{}{}'.format(self.namespace, channel)
