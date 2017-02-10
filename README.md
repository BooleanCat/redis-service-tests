Redis Service Release System Tests
==================================

Herein are system tests to be run against a deployed [`redis-service-release`](http://github.com/pivotal-cf/redis-service-release)

Requirements
------------
1. Python `3.6.0` - other versions may work
1. Install Python dependencies: `pip install -r requirements.txt`
1. A bosh deployed `redis-service-release` that uses default configuration

Alternatively, run tests in docker and the only requirement is docker.

Usage (docker)
--------------
1. `cp .envrc.template .envrc`
1. Define variables in `.envrc`
1. `docker build -t redis-service-tests .`
1. `./scripts/docker-test.sh`

Usage
-----
1. `cp .envrc.template .envrc`
1. Define variables in `.envrc`
1. `direnv allow`
1. `./scripts/test.sh`

Notes
-----
It's recommended that you use [`pyenv`](https://github.com/yyuu/pyenv) with the
[`virtualenv` extension](https://github.com/yyuu/pyenv-virtualenv) to sandbox
your python environment. This avoids polluting or changing the system Python.
