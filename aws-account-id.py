''' Display only the Account ID from the given ARN/ Amazon Resounce Name'''

# initiate a variable 'amazon_resource_name' to hold the ARN
amazon_resource_name = "arn:aws:iam::123456789012:user/Development/product_1234*"
# initiate a variable 'account_id'
# with the method 'split' split the ARN by ':'
# OUTPUT ----> ['arn', 'aws', 'iam', '', '123456789012', 'user/Development/product_1234*']
# and take the value of the element with index 4 from the list - '123456789012' - that is the Account ID
account_id = amazon_resource_name.split(':')[4]
# display on the screen 
print(f"The AWS Account ID is: {account_id}")