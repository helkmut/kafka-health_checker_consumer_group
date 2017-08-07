FROM python:3

ENV burrow_host=localhost
ENV kafka_cluster=localhost

RUN pip install --upgrade setuptools
RUN pip install requests configparser

RUN git clone https://github.com/helkmut/kafka-health_checker_consumer_group

RUN echo ${burrow_host}
RUN echo ${kafka_cluster}

RUN sed -i 's/burrow_host/'"${burrow_host}"'/g' kafka-health_checker_consumer_group/etc/attributesmonitoring.conf
RUN sed -i 's/kafka_cluster/'"${kafka_cluster}"'/g' kafka-health_checker_consumer_group/etc/attributesmonitoring.conf

RUN cp kafka-health_checker_consumer_group/etc/attributesmonitoring.conf /etc/attributesmonitoring.conf

CMD sed -i 's/burrow_host/'"${burrow_host}"'/g' /etc/attributesmonitoring.conf 
CMD sed -i 's/kafka_cluster/'"${kafka_cluster}"'/g' /etc/attributesmonitoring.conf

CMD [ "python", "./kafka-health_checker_consumer_group/bin/health_checker_consumer_group.py", "0" ]
