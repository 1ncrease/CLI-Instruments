import click
import web3
import requests
from client_createbucket import *
from oPtions import *
from cfgFIT import *

primarySpAddrStr = storage_provider#ctx.String(primarySPFlag)#in go
paymentAddrStr = paymentAddress

visibility = 2
TxOpts = #we dont know where it is from  
ChargedQuota =   #we dont know where it is from
IsAsyncMode = 1   #we dont know where it is from

@click.group()
def bucket():
  pass


@click.command()
def cmd_createbucket():
    bucketName = "MyBucket"   #getBucketNameByUrl(ctx)#in go #we dont know where it is from
    opts = NewOpts(visibility,TxOpts,paymentAddrStr,ChargedQuota,IsAsyncMode)#sdktypes.CreateBucketOptions{} #in go ,make opts list with visivility ,payment ,address etc          
    if paymentAddrStr != "":
        opts.PaymentAddress = paymentAddrStr
    if opts.Visibility == 0 :
	    opts.Visibility = visibility
        
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