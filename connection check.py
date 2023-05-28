import requests
from web3 import Web3

from cfgFIT import *

#Запрос к Tendermint RPC
response = requests.post(tendermint_rpc_url, json={
    "jsonrpc": "2.0",
    "method": "status",
    "params": {},
    "id": 1
})

#Получение ответа к запросу (подкючены ли мы к хттп гринфилд)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")