import redis
from expects import *
from radish import given, when, then, world


@given('a redis connection')
def redis_credentials(step):
    step.context.connection = redis.StrictRedis(**world.redis_credentials)


@when('I ping redis')
def ping_redis(step):
    step.context.response = step.context.connection.ping()


@when('I get the config {config:w}')
def config_get(step, config):
    config_command = world.config_alias or 'CONFIG'

    raw_respone = step.context.connection.execute_command(f"{config_command} GET {config}")
    step.context.response = raw_respone[1].decode('utf-8')


@then('I expect the response {response:S}')
def response_of_pong(step, response):
    if response == "PONG":
        expect(step.context.response).to(be_true)
    else:
        expect(step.context.response).to(equal(response))
