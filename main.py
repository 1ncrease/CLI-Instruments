import click
import web3
import requests
from client_createbucket import *


@click.group()
def bucket():
  pass


@click.command()
def cmd_createbucket():
    bucketName = getBucketNameByUrl(ctx)#in go
    primarySpAddrStr = ctx.String(primarySPFlag)#in go

    if primarySpAddrStr == "" :
		spInfo = client.ListStorageProviders(c, False)
		primarySpAddrStr = spInfo[0].GetOperatorAddress()
 
    opts = sdktypes.CreateBucketOptions{} #in go         make opts list with visivility   payment address etc
	if paymentAddrStr != "":
		opts.PaymentAddress = paymentAddrStr
                
    createbucket(bucketName, primarySpAddrStr, opts)


@click.command()
def cmd_deletebucket():
    pass


bucket.add_command(cmd_createbucket)
bucket.add_command(cmd_deletebucket)


if __name__ == '__main__':
    bucket()