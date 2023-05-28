import requests
from web3 import Web3

from cfgFIT import *
from signed import *

#Запрос к Tendermint RPC
response = requests.post(tendermint_rpc_url, json={
    "jsonrpc": "2.0",
    "method": "status",
    "params": {},
    "id": 1
})
