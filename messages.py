from cfgFIT import *
#from msgs_pb2 import CreateBucketMsg
class NewMsgCreateBucket:
    def __init__(self, creator, bucket_name, visibility, payment_address, primary_sp_address, timeout_height, signature, charged_read_quota):
        self.creator = creator
        self.bucket_name = bucket_name
        self.visibility = visibility
        self.payment_address = payment_address
        self.primary_sp_address = primary_sp_address
        self.timeout_height = timeout_height
        self.signature = signature
        self.charged_read_quota = charged_read_quota
"""
creator = ""
bucket_name = "my-bucket"
visibility = "public"
payment_address = хз#типо "0x0123456789abcdef"
primary_sp_address = хз#"0x9876543210fedcba"
timeout_height = 1000
signature = "abc123xyz"
charged_read_quota = 100
"""


