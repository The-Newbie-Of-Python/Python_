#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/9
'''

'''

import random
import time

'''列出AK信息'''
SecretId = "AKIDMdjegcmoGYiolXbk5EC3jEYhiYFo9WdE"
SecretKey = "d5MRL4VoxyvlQvMchaUHhx658A2lNq7D"

#需要调用的接口地址
uri = "cvm.tencentcloudapi.com"
#选择操作的action
Action = "RunInstances"
#选择Region
Region = "ap-chengdu"
#镜像id
ImageId = "img-8toqc6s3"
#实例配置型号
InstanceType = "SA1.SMALL1"
#计费方式
InstanceChargeType1 ="PREPAID"
InstanceChargeType2 ="POSTPAID_BY_HOUR"
#系统盘类型
DiskType0 = "LOCAL_BASIC"#默认值
DiskType1 = "LOCAL_BASIC"#本地硬盘
DiskType2 = "LOCAL_SSD"#本地SSD硬盘
DiskType3 = "CLOUD_BASIC"#普通云硬盘
DiskType4 = "CLOUD_SSD"#SSD云硬盘
DiskType5 = "CLOUD_PREMIUM"#高性能云硬盘
DiskType = DiskType5
#系统盘大小
DiskSize = 50
#Vpc信息
VpcId = "vpc-7qdjzzqq"
SubnetId = "subnet-kvzvmaxt"
#实例name
InstanceName = "wun_api"
#所需参数构成的字典
paramDict = {
    "Timestamp":int(time.time()),
    "Nonce":random.randint(65535,999999999),
    "SecretId":SecretId,
    "Action":Action,
    "Version":'2017-03-12',
    "Region":Region,
    "ImageId":ImageId
}

appendDict={
    "Placement.Zone":"ap-chengdu-1",
    "InstanceType":InstanceType,
    "InstanceChargeType":InstanceChargeType2,
    "SystemDisk.DiskType":DiskType,
    "SystemDisk.DiskSize":DiskSize,
    "VirtualPrivateCloud.VpcId":VpcId,
    "VirtualPrivateCloud.SubnetId":SubnetId,
    "InternetAccessible.PublicIpAssigned":True,
    "InternetAccessible.InternetMaxBandwidthOut":1,
    "InstanceName":InstanceName,
    "LoginSettings.KeyIds.0":"skey-c5duk1zr"
}
paramDict.update(appendDict)


if __name__ == "__main__":
    print(paramDict)