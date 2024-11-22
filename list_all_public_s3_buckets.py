import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    s3_client = boto3.client("s3")
    # s3 = boto3.client("s3")
    
    # List all S3 buckets
    response = s3_client.list_buckets()
    public_buckets = []
    # print(response)

    # Iterate through each bucket
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        
        # print (bucket_name)
        
        try:
            bucket_policy = s3_client.get_bucket_policy_status(Bucket=bucket_name)
            # print (bucket_policy)
            if bucket_policy['PolicyStatus']['IsPublic']:
                public_buckets.append(bucket_name)
        except s3_client.exceptions.from_code('NoSuchBucketPolicy'): 
            print("No Bucket Policy for bucket " + bucket_name)
        except: 
            print('something else failed')
            
    print(public_buckets)
        
    return {
        'statusCode': 200,
        'body': json.dumps(public_buckets)
    }
