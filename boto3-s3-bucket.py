'''
boto3-s3-bucket.py: creates s3 bucket with unique name
'''

import boto3
import random
import string
import logging

logging.basicConfig(filename='Python\\boto3-s3-bucket.log', filemode='w', level=logging.INFO)
logger = logging.getLogger()

def generate_random_bucket_name(prefix):
    """ 
    this function generates a unique s3 bucket name.

    args:
    prefix(str): bucket prefix to start the bucket name

    returns:
    str: returns a string of bucket prefix joined with 25 random numbers and characters at the end 

    Created By  : stepanova13
    """
    return (prefix + str(''.join(random.choices(string.ascii_lowercase + string.digits, k=25))))


bucket_prefix = 'boto3-bucket-'

# b0dy of the main
if __name__ == '__main__':
    try:
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

    # handle exceptions
    except ModuleNotFoundError:
        logger.error("A module could not be located. Please verify your imported modules.")
    except ImportError:
        logger.error("The import statement has troubles trying to load a module or the “from list” in from ... import has a name that cannot be found.\nPlease check your imported modules.")
    except Exception as error:
        logger.error(f"There is an error: {error}")
