import boto3
import random
import string


def generate_random_bucket_name(y):
    """ 
    This function generates a unique s3 bucket name.

    Parameters:
    int: user provides a integer for how many letters

    Returns:
    str: returns a string of ascii letters joined with delimiter

    """
  
    return '-'.join((random.choice(string.ascii_lowercase) for x in range(y)))

# # call s3 client
# # allows us to interact with s3 API
my_s3_client = boto3.client('s3')

response = my_s3_client.create_bucket(
    Bucket= generate_random_bucket_name(25),
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2',
    },
)

# # display the output
print(response)