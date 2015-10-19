import boto3,datetime
from boto3.session import Session

session = Session(aws_access_key_id='AKIAJBEOVR653DALXMAQ',
				aws_secret_access_key='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',
				region_name='us-west-1')

ec2 = session.resource('ec2')
instances = ec2.instances.filter(
				Filters=[{'Name':'instance-state-name','Values':['running']}])


client=session.client('cloudwatch')

response = client.get_metric_statistics(
				Namespace='AWS/EC2',
				MetricName='CPUUtilization',
				Dimensions=[
						{
								'Name':'InstanceId',
								'Value':'i-19b37dab'
						},
				],
				StartTime=datetime.datetime.now(),
				EndTime=datetime.datetime.now() + datetime.timedelta(seconds=120),
				Period=60,
				Statistics=[
						'Average'
				],
				Unit='Percent'
			)
cpuUsage = response['Datapoints'][0]['Average']

