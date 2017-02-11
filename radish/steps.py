import redis
from expects import *
from radish import given, when, then, world


@given('a redis connection')
def redis_credentials(step):
    step.context.connection = redis.StrictRedis(**world.redis_credentials)


@when('I ping redis')
def ping_redis(step):
    step.context.response = step.context.connection.ping()


@then('I expect the response {response:w}')
def response_of_pong(step, response):
    if response == "PONG":
        expect(step.context.response).to(be_true)
    else:
        expect(step.context.response).to(equal(response))
