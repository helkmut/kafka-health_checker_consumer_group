FROM python:3

ENV burrow_host=localhost
ENV kafka_cluster=localhost

RUN pip install --upgrade setuptools
RUN pip install requests configparser

RUN git clone https://github.com/helkmut/kafka-health_checker_consumer_group 

RUN echo ${burrow_host}
RUN echo ${kafka_cluster}

CMD ["./kafka-health_checker_consumer_group/bin/entrypoint.sh", $burrow_host, $kafka_cluster]

RUN cp kafka-health_checker_consumer_group/etc/attributesmonitoring.conf /etc/attributesmonitoring.conf

CMD [ "python", "./kafka-health_checker_consumer_group/bin/health_checker_consumer_group.py", "0" ]

