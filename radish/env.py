import os
from functools import lru_cache

import yaml

from bosh import Bosh
from manifest import Manifest


class Env:
    SSH_GATEWAY_HOST = os.environ['SSH_GATEWAY_HOST']
    SSH_GATEWAY_PORT = int(os.environ['SSH_GATEWAY_PORT'])
    SSH_GATEWAY_USER = os.environ['SSH_GATEWAY_USER']
    SSH_GATEWAY_PKEY = os.environ['SSH_GATEWAY_PKEY']
    REMOTE_BIND_PORT = 6379
    DEPLOYMENT_MANIFEST = os.environ['DEPLOYMENT_MANIFEST']
    BOSH_PATH = os.getenv('BOSH_PATH', 'bosh')
    BOSH_CA_CERT = os.environ['BOSH_CA_CERT']
    BOSH_CLIENT = os.environ['BOSH_CLIENT']
    BOSH_CLIENT_SECRET = os.environ['BOSH_CLIENT_SECRET']
    BOSH_ENVIRONMENT = os.environ['BOSH_ENVIRONMENT']

    @property
    def REDIS_AUTH(self):
        properties = self._manifest.get_properties_for('redis', 'redis')
        return properties['redis']['requirepass']

    @property
    def SSH_GATEWAY_ADDRESS(self):
        return (self.SSH_GATEWAY_HOST, self.SSH_GATEWAY_PORT)

    @property
    def REMOTE_BIND_HOST(self):
        return self._bosh.get_vm_ips()[0]

    @property
    def REMOTE_BIND_ADDRESS(self):
        return (self.REMOTE_BIND_HOST, self.REMOTE_BIND_PORT)

    @property
    @lru_cache(None)
    def _manifest(self):
        return Manifest(self.DEPLOYMENT_MANIFEST)

    @property
    def _bosh(self):
        return Bosh({
            'path': self.BOSH_PATH,
            'ca-cert': self.BOSH_CA_CERT,
            'username': self.BOSH_CLIENT,
            'password': self.BOSH_CLIENT_SECRET,
            'url': self.BOSH_ENVIRONMENT,
            'deployment': self._manifest.get_name(),
        })


env = Env()
