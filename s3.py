import boto3
import random
import string

def generate_random_bucket_name(prefix):
    """ 
    This function generates a unique s3 bucket name.

    Parameters:
    str: bucket prefix to start the bucket name

    Returns:
    str: returns a string of bucket prefix joined with 25 random numbers and characters at the end 
    """
    return (prefix + str(''.join(random.choices(string.ascii_lowercase + string.digits, k=25))))

bucket_prefix = 'boto3-bucket-'

# call s3 client
# allows us to interact with s3 API
my_s3_client = boto3.client('s3')

# create s3 bucket in us-east-2
response = my_s3_client.create_bucket(
    Bucket= generate_random_bucket_name(bucket_prefix),
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2',
    },
)

# display the output
print(response)