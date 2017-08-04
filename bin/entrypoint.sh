#!/bin/sh

sed -i 's/$burrow_host/'"$1"'/g' kafka-health_checker_consumer_group/etc/attributesmonitoring.conf
exec "$@"

sed -i 's/$kafka_cluster/'"$2"'/g' kafka-health_checker_consumer_group/etc/attributesmonitoring.conf
exec "$@"

