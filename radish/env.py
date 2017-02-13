import os
import yaml
from functools import lru_cache


class Env:
    SSH_GATEWAY_HOST = os.environ['SSH_GATEWAY_HOST']
    SSH_GATEWAY_PORT = int(os.environ['SSH_GATEWAY_PORT'])
    SSH_GATEWAY_USER = os.environ['SSH_GATEWAY_USER']
    SSH_GATEWAY_PKEY = os.environ['SSH_GATEWAY_PKEY']
    REMOTE_BIND_HOST = os.environ['REMOTE_BIND_HOST']
    REMOTE_BIND_PORT = int(os.environ['REMOTE_BIND_PORT'])
    DEPLOYMENT_MANIFEST = os.environ['DEPLOYMENT_MANIFEST']

    @property
    def REDIS_AUTH(self):
        return self._get_redis_job_properties()['redis']['requirepass']

    @property
    def SSH_GATEWAY_ADDRESS(self):
        return (self.SSH_GATEWAY_HOST, self.SSH_GATEWAY_PORT)

    @property
    def REMOTE_BIND_ADDRESS(self):
        return (self.REMOTE_BIND_HOST, self.REMOTE_BIND_PORT)

    @lru_cache(None)
    def _get_manifest(self):
        with open(self.DEPLOYMENT_MANIFEST) as raw_manifest:
            return yaml.load(raw_manifest)

    def _get_deployment_name(self):
        return self._get_manifest()['name']

    def _get_redis_job_properties(self):
        is_redis = lambda job: job['name'] == 'redis'
        jobs = self._get_redis_instance_group()['jobs']
        return next(filter(is_redis, jobs))['properties']

    def _get_redis_instance_group(self):
        is_redis = lambda group: group['name'] == 'redis'
        return next(filter(is_redis, self._get_manifest()['instance_groups']))


env = Env()
