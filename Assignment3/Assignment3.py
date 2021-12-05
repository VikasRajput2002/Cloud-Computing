 
import boto3

client = boto3.client('autoscaling',region_name = 'us-east-1',aws_access_key_id='ASIAW7PYSJHAMKWTXTUR',
aws_secret_access_key='sidzvkFk6/ylpZuKGXQTmioSyglLbkdzaxvK+A9p',
aws_session_token='FwoGZXIvYXdzELX//////////wEaDDsRDZU81QEGdXUsqyLJAZUHVy/Vlv/wg3wJJgkElXlCezQ65VoIOZTovxxPDNfPYPfz13bG3YgRRDI7wrVnX2Ww4FRX0lE4OWIfy0DeG0sBM0U2/gaYKWugpls6p8IENWB0XkM87y65fbNJIUG0fgV9KWcdfs5JIFapyY1BxMfR0mYwvSQZAc06BO1ZH4eoNj0gLzowOPjH7LiBrAHPYyY4k6YDDHwhl4H3rudJON1zgRwpIsWsaJ0CDnEInY5LnEwTrTieSYRhN+LLuZXcTpMdayc4eoiSTyjXxqqKBjItQljNOEzHTqOV1hW5ryuoNV4lH9jpdb+1u6XFzSGNQwFhfVjaIA6y3Z70bUOY')

data = '''
#!/bin/bash
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
cd /var/www/html
rm index.html
wget https://s3.amazonaws.com/www.myassignment2.com/index.html
'''


launch_config = client.create_launch_configuration(
    ImageId='ami-087c17d1fe0178315',
    InstanceType='t2.micro',
    KeyName='CS351-2021',
    LaunchConfigurationName='vikash.raput@iitg.ac.in',
    SecurityGroups=[
        'sg-00ab94d8db2846b6e',
    ],
    UserData=data,
)


response = client.create_auto_scaling_group(
    AutoScalingGroupName='vikash.rajput',
    MaxSize = 3,
    VPCZoneIdentifier = 'subnet-b180ad90',
    MinSize = 1,
    LaunchConfigurationName='vikash.rajput@iiitg.ac.in',
)


policy1 = client.put_scaling_policy(
    AdjustmentType='ChangeInCapacity',
    AutoScalingGroupName='vikash.rajput',
    PolicyName='ScaleDown',
    ScalingAdjustment=-1,
)

policy2 = client.put_scaling_policy(
    AdjustmentType='ChangeInCapacity',
    AutoScalingGroupName='vikash.rajput',
    PolicyName='ScaleUp',
    ScalingAdjustment=1,
)


cloudwatch = boto3.client('cloudwatch',region_name = 'us-east-1')

cloudwatch.put_metric_alarm
(
    AlarmName='high_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=2,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=120,
    Statistic='Average',
    Threshold=80.0,
    AlarmDescription='Alarm when server CPU exceeds 80%',
    Dimensions=[
        {
          'Name': 'AutoScalingGroupName',
          'Value': 'vikash.rajput'
        },
    ],
    Unit='Seconds'
)

cloudwatch.put_metric_alarm
(
    AlarmName = 'low_CPU_Utilization',
    ComparisonOperator='LessThanThreshold',
    EvaluationPeriods=2,
    MetricName='CPUUtilization',                                    
    Namespace='AWS/EC2',
    Period=120,
    Statistic='Average',
    Threshold=20.0,
    AlarmDescription='Alarm when server CPU is below 20%',
    Dimensions=[
        {
          'Name': 'AutoScalingGroupName',
          'Value': 'vikash.rajput'
        },
    ],
    Unit='Seconds'
)
