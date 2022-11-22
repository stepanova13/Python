''' Display only the Account ID from the given ARN/ Amazon Resounce Name'''

amazon_resource_name = "arn:aws:iam::123456789012:user/Development/product_1234*"
account_id = amazon_resource_name.split(':')[4]

print(f"The AWS Account ID is: {account_id}")