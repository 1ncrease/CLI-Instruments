import click
import web3
import requests
from client_createbucket import *
from makemessagefile import *
from oPtions import *


@click.group()
def bucket():
  pass


@click.command()
def cmd_createbucket():
    bucketName = "MyBucket"#getBucketNameByUrl(ctx)#in go
    primarySpAddrStr = "https://gnfd-testnet-sp-1.bnbchain.org"#ctx.String(primarySPFlag)#in go
    paymentAddrStr = "212121212"#хз\ Аманжол ты знаешь
    opts = NewOpts(Visibility,TxOpts,PaymentAddrStr,ChargedQuota,IsAsyncMode)#sdktypes.CreateBucketOptions{} #in go ,make opts list with visivility ,payment ,address etc          
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