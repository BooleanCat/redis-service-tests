import os


SSH_GATEWAY_ADDRESS = (
    os.environ['SSH_GATEWAY_HOST'],
    int(os.environ['SSH_GATEWAY_PORT']),
)

TUNNEL_KWARGS = {
    'ssh_username': os.environ['SSH_GATEWAY_USER'],
    'ssh_pkey': os.environ['SSH_GATEWAY_PKEY'],
    'remote_bind_address': (os.environ['REMOTE_BIND_IP'], int(os.environ['REMOTE_BIND_PORT'])),
}

REDIS_AUTH = os.environ['REDIS_AUTH']
