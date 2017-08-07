FROM python:3

ENV burrow_host localhost
ENV kafka_cluster kafkacluster

RUN pip install --upgrade setuptools
RUN pip install requests configparser

RUN git clone https://github.com/helkmut/kafka-health_checker_consumer_group

RUN cp kafka-health_checker_consumer_group/etc/attributesmonitoring.conf /etc/attributesmonitoring.conf

ENTRYPOINT sed -i 's/localhost/'"${burrow_host}"'/g' /etc/attributesmonitoring.conf 
ENTRYPOINT sed -i 's/kafkacluster/'"${kafka_cluster}"'/g' /etc/attributesmonitoring.conf

CMD [ "python", "./kafka-health_checker_consumer_group/bin/health_checker_consumer_group.py", "0" ]
