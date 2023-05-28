from messages import * 
import requests
from signed import *
from cfgFIT import *
from main import *
from oPtions import *
endpoint = хз
sender_address = хз
creator = sender_address 
recipient_address = хз 
def createbucket(bucketName, primaryAddr, opts):
	chargedReadQuota = opts.ChargedQuota 
	timeoutHeight = 1
	visibility = opts.Visibility
	sig_bytes = 2# типа b'\x01\x02\x03\x04'  
	PrimarySpApproval = Approval(timeoutHeight, sig_bytes)
	msg = NewMsgCreateBucket(creator, bucketName, visibility,paymentAddress, primaryAddr,PrimarySpApproval ,timeoutHeight, sig, chargedReadQuota)
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