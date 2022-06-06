import logging
import os
from elasticsearch import Elasticsearch
import datetime

es = Elasticsearch(
    [{"host": os.getenv("ES_HOST", default="9200.grd44b0c.64q1jlfb.17f4cc.grapps.cn"), "port": os.getenv("ES_PORT", default=80)}],
    http_auth=(os.getenv("ES_USER", default="elastic"), os.getenv("ES_PASSWORD", default="elastic"))
)


def ESTransmitData(ChannelName, DocChannelTitle, ReadTitle, ReadCount):
    indexData = {
        'DocTitle': ReadTitle,
        'ReadCount': ReadCount,
        'ChannelName': ChannelName,
        'DocChannelName': DocChannelTitle,
        '@timestamp': datetime.datetime.utcnow()
    }
    print(ChannelName, DocChannelTitle, ReadTitle, ReadCount)
    # for ReadNum in range(ReadCount):
    #     result = es.index(index='articlereadingquantity', document=indexData)
    #     logging.error(result)
