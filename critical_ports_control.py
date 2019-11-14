import boto3

#Create an ec2 client
ec2 = boto3.client('ec2')

#Create an sns client
sns = boto3.client('sns')

#email address of the subscriber
endpoint = 'subscriber_email_address'

#Create an sns topic
response = sns.create_topic(Name='critical_ports_control')
#save the topic arn in the variable 'topicarn'
topicarn = (response['TopicArn'])

#get the subscribers of the topic
response2 = sns.list_subscriptions_by_topic(
    TopicArn=topicarn
    )

#verify if the given endpoint already subscribe to the topic
if (response2['Subscriptions']) == '[]' or (response2['Subscriptions'][0]['Endpoint']) == endpoint:
    #if so, do nothing
    pass
#if not proceed to subscription
else:
    response3 = sns.subscribe(TopicArn=topicarn, Protocol='email', Endpoint=endpoint)

#Get the description of our security groups
response4 = ec2.describe_security_groups()
#a loop to browse the list of security groups
for i in response4['SecurityGroups']:
    #ignore the default security group created by the default VPC
    if (i['Description']) == 'default VPC security group' and (i['IpPermissions'][0]['IpProtocol']) == '-1':
        pass
    else:
        #get the port
        ports = (i['IpPermissions'][0]['ToPort'])
        #verify if the port is one of those ports (ssh, rdp, mysql, ms sql, postgresql, oracle, redshift)
        if ports in [22,3389,3306,1433,5432,1521,5439]:
            #get the ip range
            cidrRange = (i['IpPermissions'][0]['IpRanges'][0]['CidrIp'])
            #verify if the ip range is '0.0.0.0/0'
            if cidrRange == '0.0.0.0/0':
                tag = (i['Tags'][0]['Value'])
                groupid = (i['GroupId'])
                message = (groupid + ' Security Group which tag name is ' + tag + ' has inbound rule open to internet on port: ' + str(ports))
                response5 = sns.publish(
                    TopicArn = topicarn,
                    Message = message,
                    Subject = 'Critical Ports Control',
                    )
