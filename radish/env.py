import os
import yaml
from functools import lru_cache

from manifest import Manifest


class Env:
    SSH_GATEWAY_HOST = os.environ['SSH_GATEWAY_HOST']
    SSH_GATEWAY_PORT = int(os.environ['SSH_GATEWAY_PORT'])
    SSH_GATEWAY_USER = os.environ['SSH_GATEWAY_USER']
    SSH_GATEWAY_PKEY = os.environ['SSH_GATEWAY_PKEY']
    REMOTE_BIND_HOST = os.environ['REMOTE_BIND_HOST']
    REMOTE_BIND_PORT = 6379
    DEPLOYMENT_MANIFEST = os.environ['DEPLOYMENT_MANIFEST']

    @property
    def REDIS_AUTH(self):
        properties = self._manifest.get_properties_for('redis', 'redis')
        return properties['redis']['requirepass']

    @property
    def SSH_GATEWAY_ADDRESS(self):
        return (self.SSH_GATEWAY_HOST, self.SSH_GATEWAY_PORT)

    @property
    def REMOTE_BIND_ADDRESS(self):
        return (self.REMOTE_BIND_HOST, self.REMOTE_BIND_PORT)

    @property
    @lru_cache(None)
    def _manifest(self):
        return Manifest(self.DEPLOYMENT_MANIFEST)


env = Env()
