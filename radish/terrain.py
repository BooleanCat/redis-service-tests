import os

from radish import before, after, world
from sshtunnel import SSHTunnelForwarder


TARANTINO_ADDRESS = (
    os.environ['SSH_GATEWAY_ADDRESS'],
    int(os.environ['SSH_GATEWAY_PORT']),
)

TUNNEL_KWARGS = {
    'ssh_username': os.environ['SSH_GATEWAY_USER'],
    'ssh_pkey': os.environ['SSH_GATEWAY_PKEY'],
    'remote_bind_address': (os.environ['REMOTE_BIND_IP'], int(os.environ['REMOTE_BIND_PORT'])),
}


@before.all
def create_ssh_tunnel(features, marker):
    world.ssh_tunnel = SSHTunnelForwarder(TARANTINO_ADDRESS, **TUNNEL_KWARGS)
    world.ssh_tunnel.__enter__()


@after.all
def destroy_ssh_tunnel(features, marker):
    world.ssh_tunnel.__exit__()
