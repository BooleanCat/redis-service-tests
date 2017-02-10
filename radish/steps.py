import os

import redis
from expects import *
from radish import given, when, then, arg_expr


@arg_expr("ip_address", r'\d{1,3}(\.\d{1,3}){3}')
def user_argument_expression(text):
    return text


@given('redis credentials {host:ip_address}:{port:w}')
def redis_credentials(step, host, port):
    step.context.credentials = {
        'host': host,
        'port': int(port),
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
        expect(step.context.response).to(response)
