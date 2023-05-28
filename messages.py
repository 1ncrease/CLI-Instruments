from cfgFIT import *
from mesg_pb2 import CreateBucketMsg


def NewMsgCreateBucket(creator, bucketName, visibility, primarySPAddress, paymentAddress, timeoutHeight, sig, chargedReadQuota):
    msg = CreateBucketMsg()
    msg.creator = str(creator)
    msg.bucket_name = bucketName
    msg.visibility = visibility
    msg.payment_address = str(paymentAddress)
    msg.primary_sp_address = str(primarySPAddress)    # хз 
    msg.timeout_height = timeoutHeight
    msg.signature = sig
    msg.charged_read_quota = chargedReadQuota
    
