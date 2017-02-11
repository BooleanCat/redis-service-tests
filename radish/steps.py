import os
from collections import namedtuple

import redis
from expects import *
from radish import given, when, then, world


Address = namedtuple('Address', ['host', 'port'])


@given('redis credentials')
def redis_credentials(step):
    address = Address(*world.ssh_tunnel.local_bind_address)

    step.context.credentials = {
        'host': address.host,
        'port': address.port,
        'password': os.environ['REDIS_AUTH'],
    }


@when('I ping redis')
def ping_redis(step):
    client = redis.StrictRedis(**step.context.credentials)
    step.context.response = client.ping()


@then('I expect the response {response:w}')
def response_of_pong(step, response):
    if response == "PONG":
        expect(step.context.response).to(be_true)
    else:
        expect(step.context.response).to(equal(response))
