import click
import web3
import requests
from client import *


@click.group()
def bucket():
  pass


@click.command()
def cmd_createbucket():
    
    createbucket(bucketName, primarySpAddrStr, opts)


@click.command()
def cmd_deletebucket():
    pass


bucket.add_command(cmd_createbucket)
bucket.add_command(cmd_deletebucket)


if __name__ == '__main__':
    bucket()