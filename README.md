# Kafka - Health_Checker_Consumer_Group

## Versao 

0.1 - 13/07/2017
0.2 - 04/08/2017
0.3 - 07/08/2017

## Introducao

Agente de coleta em Python3 para expor metricas obtidas pelo Burrow no formato do InfluxDB. 

Em sua terceira versão(0.3) ainda tem como restricao coletar metricas de varios consumergroups de um unico cluster do Kafka. Tambem nao foi implementado o recurso de timeout, logo deve ser controlado atraves do programa que o consome / executa requisicao. 

-> Wishlist

> Timeout agent; <br />
> Timestamp per URLrequest;<br />
> Refactor code. <br />


## Requerimentos

* PYTHON > 3.0
* Modules: configparser sys requests socket
* Burrow
* Acesso para a URL do Burrow do Kafka que desejas monitorar

## Modo de Uso

### Script health_checker_consumer_group

Example: 

```shell
~/health_checker_consumer_group/bin/health_checker_consumer_group.py 0
```


<br />
Trabalhando com Docker: 

```shell
git clone https://github.com/helkmut/kafka-health_checker_consumer_group
cd kafka-health_checker_consumer_group/opt
docker build -t kafka-health_checker_consumer_group .
docker run --env burrow_host=$my_burrow_hostip --env kafka_cluster=$my_kafka_cluster_name --name my_container kafka-health_checker_consumer_group

```


Onde: 

   ARGV -> 1 : debug mode (0: off 1: on)

   Todas as configurações devem ser definidas no arquivo ~/health_checker_consumer_group/etc/attributesmonitoring.conf

[component_list]<br />
comp_keys = status totallag -> metricas para serem coletadas<br />
[actuator_healthaddress]<br />
address = http://localhost:8000 -> URL do Burrow<br />
[actuator_healthcluster]<br />
cluster = local -> Nome do cluster do Kafka<br />
[actuator_healthtimeout]<br />
timeout = 30 -> Ainda nao implementado<br />


### Author
Gabriel Prestes
<gabriel.prestes@ilegra.com>
