'''
boto3-ec2-describe-region.py: 

This code displays the names of all aws regions for ec2.
Logs events in boto3-ec2-describe-region.log file.

Created By  : stepanova13
'''
import boto3
import logging


# setup logger
logging.basicConfig(filename='Python\\boto3-ec2-describe-region.log', filemode='w', level=logging.INFO)
logger = logging.getLogger()

# call boto client
ec2 = boto3.client('ec2')

# retrieve all regions that work with ec2
response = ec2.describe_regions()

# print(type(response))

def region_name():
    '''
    tris function displays the names of all aws regions for ec2
    arg: None
    return: True/False
    '''
    try:
        for element in response['Regions']:
            print(element['RegionName'])
    except Exception as error:
        logger.error(f'There is an error: {error}')
        return False
    return True

if __name__ == '__main__':
    region_name()
    logger.info('Execution successful.')