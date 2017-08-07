#!/bin/sh

sed -i 's/localhost/'"${1}"'/g' /etc/attributesmonitoring.conf
sed -i 's/kafkacluster/'"${2}"'/g' /etc/attributesmonitoring.conf

