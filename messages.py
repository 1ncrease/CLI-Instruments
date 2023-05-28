from cfgFIT import *
from mesg_pb2 import NewBucketMsg


def NewMsgCreateBucket(creator, bucketName, visibility, primarySPAddress, paymentAddress, timeoutHeight, sig, chargedReadQuota):
    msg = NewBucketMsg()
    msg.Creator = str(creator)
    msg.BucketName = bucketName
    msg.Visibility = visibility
    msg.PaymentAddress = str(paymentAddress)
    msg.PrimarySpAddress = str(primarySPAddress)
    msg.PrimarySpApproval=Approval(timeoutHeight, sig)
    msg.ChargedReadQuota= chargedReadQuota
    
