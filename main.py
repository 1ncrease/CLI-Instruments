import click
import web3
import requests
from client_createbucket import *
from makemessagefile import *
from oPtions import *
from cfgFIT import *

primarySpAddrStr = storage_provider#ctx.String(primarySPFlag)#in go
paymentAddrStr = paymentAddress

visibility = 2#хз
TxOpts = хз 
ChargedQuota = хз
IsAsyncMod = хз

@click.group()
def bucket():
  pass


@click.command()
def cmd_createbucket():
    bucketName = "MyBucket"   #getBucketNameByUrl(ctx)#in go
    opts = NewOpts(visibility,TxOpts,paymentAddrStr,ChargedQuota,IsAsyncMode)#sdktypes.CreateBucketOptions{} #in go ,make opts list with visivility ,payment ,address etc          
    if paymentAddrStr != "":
        opts.PaymentAddress = paymentAddrStr
    #if primarySpAddrStr == "" : 
	    #spInfo = 1#client.ListStorageProviders(c, False)
	    #primarySpAddrStr = 1#spInfo[0].GetOperatorAddress()         
    createbucket(bucketName, primarySpAddrStr, opts)


@click.command()
def cmd_deletebucket():
    pass


bucket.add_command(cmd_createbucket)
bucket.add_command(cmd_deletebucket)


if __name__ == '__main__':
    bucket()