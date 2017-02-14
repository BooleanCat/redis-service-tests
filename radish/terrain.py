from collections import namedtuple

from radish import before, after, world
from sshtunnel import SSHTunnelForwarder

from env import env


Address = namedtuple('Address', ['host', 'port'])


@before.all
def create_ssh_tunnel(features, marker):
    world.ssh_tunnel = SSHTunnelForwarder(
        env.SSH_GATEWAY_ADDRESS,
        ssh_username=env.SSH_GATEWAY_USER,
        ssh_pkey=env.SSH_GATEWAY_PKEY,
        remote_bind_address=env.REMOTE_BIND_ADDRESS,
    )
    world.ssh_tunnel.__enter__()
    world.redis_credentials = get_redis_credentials()


@after.all
def destroy_ssh_tunnel(features, marker):
    world.ssh_tunnel.__exit__()


def get_redis_credentials():
    redis_address = Address(*world.ssh_tunnel.local_bind_address)
    return {
        'host': redis_address.host,
        'port': redis_address.port,
        'password': env.REDIS_AUTH,
    }
