from messages import * 
import requests
import ecdsa
from signed import *
from cfgFIT import *

endpoint = хз
sender_address = хз
creator = sender_address
recipient_address = хз 
def createbucket(bucketName, primaryAddr, opts):
	chargedReadQuota = opts[0]
	sig = opts[1]
	timeoutHeight = opts[2]
	visibility = opts[3]
	msg = NewMsgCreateBucket(creator, bucketName, visibility, primaryAddr, paymentAddress, timeoutHeight, sig, chargedReadQuota)
	signed = sign_message(msg, private_key1)
	signature_hex = hex(signed)
	transaction = {
    	"sender": sender_address,
    	"recipient": recipient_address,
    	"message": msg.SerializeToString(),
    	"gas_price": 100
	}     
	#signature = sign_transaction(transaction, private_key)   я хз 
	transaction["signature"] = signature_hex # возможно только signature
	response = requests.post(f"{endpoint}/transactions", json = transaction) 
	return response