Feature: a redis-service deployment
    In order to interact with a redis database
    As a software engineer
    I need a Redis server to be deployed

    Scenario: redis is running
        Given a redis connection
        When I ping redis
        Then I expect the response PONG

      Scenario Outline: configured with defaults
        Given a redis connection
        When I get the config <config>
        Then I expect the response <response>

      Examples:
        | config    | response                    |
        | port      | 6379                        |
        | daemonize | yes                         |
        | pidfile   | /var/vcap/sys/run/redis.pid |
