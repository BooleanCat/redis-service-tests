import os
from functools import partial

from radish import before, after
from sshtunnel import SSHTunnelForwarder


SSH_TUNNEL = None

TARANTINO_ADDRESS = (
    os.environ['SSH_GATEWAY_ADDRESS'],
    int(os.environ['SSH_GATEWAY_PORT']),
)

TUNNEL_KWARGS = {
    'ssh_username': os.environ['SSH_GATEWAY_USER'],
    'ssh_pkey': os.environ['SSH_GATEWAY_PKEY'],
    'remote_bind_address': (os.environ['REMOTE_BIND_IP'], int(os.environ['REMOTE_BIND_PORT'])),
    'local_bind_address': ('0.0.0.0', 8009),
}


@before.all
def create_ssh_tunnel(features, marker):
    global SSH_TUNNEL
    SSH_TUNNEL = SSHTunnelForwarder(TARANTINO_ADDRESS, **TUNNEL_KWARGS)
    SSH_TUNNEL.__enter__()


@after.all
def destroy_ssh_tunnel(features, marker):
    global SSH_TUNNEL
    SSH_TUNNEL.__exit__()
