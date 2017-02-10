Feature: a redis-service deployment
    In order to interact with a redis database
    As a software engineer
    I need a Redis server to be deployed

    Scenario: redis is running
        Given redis credentials 0.0.0.0:8009
        When I ping redis
        Then I expect the response PONG
