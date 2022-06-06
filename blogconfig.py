import os
import yaml

ConfigPath = os.getenv('CONFIG_PATH', default='/Users/zhangqi/Desktop/rainbond_spider/config.yaml')
with open(ConfigPath, 'r', encoding='utf-8') as f:
    fileContext = f.read()
    context = yaml.load(fileContext, Loader=yaml.FullLoader)


def blog_channel():
    """
    :return: get blog channel
    """
    ChannelKeyList = []
    for key, value in context.items():
        ChannelKeyList.append(key)
    return ChannelKeyList


def blog_link(ChannelName):
    """
    :param ChannelName:
    :return: get channel link
    """
    ChannelValueList = []
    for key, value in context[ChannelName].items():
        ChannelValueList.append(value)
    return ChannelValueList


def blog_doc_name(DocName, DocLink):
    """
    :return:
    """
    for key, value in context[DocName].items():
        if value == DocLink:
            return key
