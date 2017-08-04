#!/bin/sh

sed -i 's/$burrow_host/'"$burrow_host"'/g' kafka-health_checker_consumer_group/etc/attributesmonitoring.conf
exec "$@"

sed -i 's/$kafka_cluster/'"$kafka_cluster"'/g' kafka-health_checker_consumer_group/etc/attributesmonitoring.conf
exec "$@"

