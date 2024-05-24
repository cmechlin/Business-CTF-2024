import boto3

iam = boto3.client("iam")
roles = iam.list_roles()
role_arn = next(
    role["Arn"] for role in roles["Roles"] if role["RoleId"] == "AROAXYAFLIG2BLQFIIP34"
)
print(role_arn)
