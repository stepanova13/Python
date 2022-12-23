'''
boto3-ec2-report-generator-s3-sns-email.py: 

This code generates an EC2 report with
Name Tag
InstanceId
ImageId
InstanceType.

Puts the report in a S3 bucket, 
and sends an email with the report attached.
'''

import boto3
import logging
import csv
from botocore.exceptions import ClientError
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


# Setup logger
logging.basicConfig(filename='Python\\boto3-ec2-report-generator-s3-ses-email.log', filemode='w', level=logging.INFO)
logger = logging.getLogger()

# Constants/ Global variables
EC2_REPORT_FILE_NAME = 'Python\ec2--report.csv'

def list_all_instances():
    '''
    this function creates a list with the information requested
    args: None
    return: list
    '''
    # call ec2 the client
    # establish a connection with the aws account - authentication needed
    ec2_client = boto3.client('ec2')
    
    # retrieve all ec2 instances in us-east-1
    response = ec2_client.describe_instances()
    
    # empty list
    list_of_instance_metadata = []

    # for reservation in response['Reservations']:
    #     for instance in reservation['Instances']:
    #         print(instance['InstanceId'])
    for instance in response['Reservations'][0]['Instances']:
        # retrieving the data needed
        instance_name = instance['Tags'][0]['Value']
        instance_id = instance['InstanceId']
        image_id = instance['ImageId']
        instance_type = instance['InstanceType']
        
        # populate the list
        list_of_instance_metadata.append([instance_name, instance_id, image_id, instance_type])

    return list_of_instance_metadata

def generate_excel_report(report):
    '''
    this function creates a csv file 
    args: list
    return: boolean: True if file created succesfully, False if error occures
    '''
    # header of the csv file
    header = ['Instance Name', 'Instance ID', 'Image ID', 'Instance Type']
    
    try:
        with open(EC2_REPORT_FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)   # to write to a csv file
            writer.writerow(header)
            writer.writerows(report)
    except FileNotFoundError as error:
        logger.error(f'File doesn\'t exist. {error}')
        return False
    return True

def upload_report_to_s3():
    '''
    this finction uploads the report csv file to a s3 bucket
    args: None
    return: boolean: True if bucket created succesfully, False if error occures
    '''
    # assign the bucket name
    bucket_name = 's3-bucket-name'
    # call the s3 client
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(EC2_REPORT_FILE_NAME, bucket_name, 'ec2--report.csv')
        logger.info(f'Report {EC2_REPORT_FILE_NAME} uploaded to s3 bucket {bucket_name}')
    except ClientError as error:
        logging.error(f'There is an error: {error}')
        return False
    return True

def send_email():
    '''
    this function sends an email with attachment
    args: None
    return: True if message sent, False if error occures
    '''

    #call SES boto client
    ses_client = boto3.client('ses')
    
    # define variables
    SENDER = "sender@gmail.com"
    RECEIVER = "receiver@gmail.com"
    CHARSET = "utf-8"
    msg = MIMEMultipart('mixed')
    msg['Subject'] = "EC2 Report"
    msg['From'] = SENDER
    msg['To'] = RECEIVER

    msg_body = MIMEMultipart('alternative')

    BODY_TEXT = "Hi BOSS,\n\nPlease find the requested EC2 Report attached.\n\nBest wishes,\nEmployee"

    textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)

    msg_body.attach(textpart)

    # full path to the file that will be attached to the email
    ATTACHMENT1 = EC2_REPORT_FILE_NAME

    # adding attachment
    att1 = MIMEApplication(open(ATTACHMENT1, 'rb').read())
    att1.add_header('Content-Disposition', 'attachment',
                    filename=os.path.basename(ATTACHMENT1))

    msg.attach(msg_body)
    msg.attach(att1)

    try:
        response = ses_client.send_raw_email(
            Source=SENDER,
            Destinations=[
                RECEIVER
            ],
            RawMessage={
                'Data': msg.as_string(),
            },
        )
        logger.info(f"Message send successfully. Message id : {response['MessageId']}")
    except Exception as error:
        logger.error(f'Error: , {error}')
        return False
    return True

if __name__ == '__main__':    
    # get the data for the report
    report = list_all_instances()
    # create the csv file report
    generate_excel_report(report)
    # upload the report to s3
    upload_report_to_s3()
    # send email with report attached
    send_email()