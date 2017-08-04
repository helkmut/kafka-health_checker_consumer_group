FROM python:3

ENV burrow_host=localhost
ENV kafka_cluster=localhost

RUN pip install --upgrade setuptools
RUN pip install requests configparser

RUN git clone https://github.com/helkmut/kafka-health_checker_consumer_group 

ENTRYPOINT ["kafka-health_checker_consumer_group/bin/entrypoint.sh", "${burrow_host}", "${kafka_cluster}"]

RUN cp kafka-health_checker_consumer_group/etc/attributesmonitoring.conf /etc/attributesmonitoring.conf

RUN cat kafka-health_checker_consumer_group/etc/attributesmonitoring.conf

RUN /etc/attributesmonitoring.conf

CMD [ "python", "./kafka-health_checker_consumer_group/bin/health_checker_consumer_group.py", "0" ]

