type CreateBucketOptions struct {
	Visibility     storageTypes.VisibilityType
	TxOpts         *gnfdsdktypes.TxOption
	PaymentAddress string
	ChargedQuota   uint64
	IsAsyncMode    bool // indicate whether to create the bucket in asynchronous mode
}

(
	VISIBILITY_TYPE_UNSPECIFIED VisibilityType = 0
	VISIBILITY_TYPE_PUBLIC_READ VisibilityType = 1
	VISIBILITY_TYPE_PRIVATE     VisibilityType = 2
	VISIBILITY_TYPE_INHERIT VisibilityType = 3
)

VisibilityType_name = {
	0: "VISIBILITY_TYPE_UNSPECIFIED",
	1: "VISIBILITY_TYPE_PUBLIC_READ",
	2: "VISIBILITY_TYPE_PRIVATE",
	3: "VISIBILITY_TYPE_INHERIT",
}
VisibilityType_value = {
	"VISIBILITY_TYPE_UNSPECIFIED": 0,
	"VISIBILITY_TYPE_PUBLIC_READ": 1,
	"VISIBILITY_TYPE_PRIVATE":     2,
	"VISIBILITY_TYPE_INHERIT":     3,
}
#list of visib num

def createbucket(bucketName, primaryAddr, opts):
    address  = sdk.AccAddressFromHexUnsafe(primaryAddr)
    
	visibility = 2
	#visibility =  storageTypes.VisibilityType
    #if opts.Visibility == 0:
		#visibility = 2
    #else:
		#visibility = opts.Visibility
	

	opts.PaymentAddress = 
    
    createBucketMsg = storageTypes.NewMsgCreateBucket(c.MustGetDefaultAccount().GetAddress(), bucketName,visibility, address, paymentAddr, 0, nil, opts.ChargedQuota)
	
	signedMsg = c.GetCreateBucketApproval(ctx, createBucketMsg)


	if opts.TxOpts == nil :
		broadcastMode := tx.BroadcastMode_BROADCAST_MODE_SYNC
		opts.TxOpts = &gnfdsdk.TxOption{Mode: &broadcastMode}
	
    
	createBucketMsg = storageTypes.NewMsgCreateBucket(c.MustGetDefaultAccount().GetAddress(), bucketName,
		visibility, address, paymentAddr, 0, nil, opts.ChargedQuota)


	resp = c.chainClient.BroadcastTx(ctx, []sdk.Msg{signedMsg}, opts.TxOpts)


	txnHash = resp.TxResponse.TxHash
    
	return txnHash 
