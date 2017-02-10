#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT="$( dirname $DIR )"

function docker_envs {
  grep "^export" .envrc | cut -c 8- | xargs -I{} echo -n "-e {} "
}

pushd $ROOT > /dev/null
  docker run \
    $( docker_envs ) \
    -e SSH_GATEWAY_PKEY=/home/test/pkey.pem \
    -v $SSH_GATEWAY_PKEY:/home/test/pkey.pem \
    -v $ROOT:/home/test/redis-service-tests \
    -i -t redis-service-tests redis-service-tests/scripts/test.sh
popd > /dev/null
