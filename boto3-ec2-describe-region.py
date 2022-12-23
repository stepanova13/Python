'''
boto3-ec2-describe-region: this code displays the names of all aws regions for ec2

Created By  : stepanova13
'''
import boto3

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
        return True
    except Exception as error:
        print(f'There is an error: {error}')
        return False

if __name__ == '__main__':
    region_name()