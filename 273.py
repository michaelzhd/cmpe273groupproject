import boto3,datetime,time
from boto3.session import Session

session = Session(aws_access_key_id='',#'',
				aws_secret_access_key='',#'
				region_name='us-west-1')

ec2 = session.resource('ec2')
instances = ec2.instances.filter(
				Filters=[{'Name':'instance-state-name','Values':['running']}])


client=session.client('cloudwatch')

for i in range(100):
    response = client.get_metric_statistics(
    				Namespace='AWS/EC2',
    				MetricName='NetworkIn',
    				Dimensions=[
    						{
    								'Name':'InstanceId',
    								'Value':'i-d8400d1e'#'i-19b37dab'
    						},
    				],
    				StartTime=datetime.datetime.now()- datetime.timedelta(seconds=120),
    				EndTime=datetime.datetime.now(),
    				Period=60,
    				Statistics=[
    						'Average'
    				],
    				Unit='Bytes'
    			)
    for key in response:
        print key, ':', response[key]
    # cpuUsage = response['Datapoints'][0]['Average']
    # print cpuUsage
    time.sleep(1)



