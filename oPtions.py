
class Approval:
    def __init__(self, expired_height = 1, sig = 2):
        self.expired_height = expired_height
        self.sig = sig


class NewOpts:
    def __init__(self,_Visibility,Tx_Opts,_PaymentAddress,_ChargedQuota,_IsAsyncMode):
        self.Visibility = _Visibility
        self.TxOpts = Tx_Opts
        self.PaymentAddress = _PaymentAddress
        self.ChargedQuota = _ChargedQuota
        self.IsAsyncMode = _IsAsyncMode

   
#storageTypes.VisibilityType
#*gnfdsdktypes.TxOption
#string
 #uint64
 #bool 
 #"""
 #BroadcastMode {
  #// zero-value for mode ordering
  #BROADCAST_MODE_UNSPECIFIED = 0;
  #// DEPRECATED: use BROADCAST_MODE_SYNC instead,
  #// BROADCAST_MODE_BLOCK is not supported by the SDK from v0.47.x onwards.
 # BROADCAST_MODE_BLOCK = 1 [deprecated = true];
 # // BROADCAST_MODE_SYNC defines a tx broadcasting mode where the client waits for
  #// a CheckTx execution response only.
  ## // BROADCAST_MODE_ASYNC defines a tx broadcasting mode where the client returns
 # BROADCAST_MODE_ASYNC = 3;
#}

#"""
#""""
#visibilityType:
#VISIBILITY_TYPE_UNSPECIFIED = 0
#VISIBILITY_TYPE_PUBLIC_READ = 1
##VISIBILITY_TYPE_PRIVATE = 2
#VISIBILITY_TYPE_INHERIT = 3
#"""