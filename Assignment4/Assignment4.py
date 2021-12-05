import boto3
import time

ebsClient = boto3.client('elasticbeanstalk',region_name = 'us-east-1',aws_access_key_id='ASIAW7PYSJHAMKWTXTUR',
aws_secret_access_key='sidzvkFk6/ylpZuKGXQTmioSyglLbkdzaxvK+A9p',
aws_session_token='FwoGZXIvYXdzELX//////////wEaDDsRDZU81QEGdXUsqyLJAZUHVy/Vlv/wg3wJJgkElXlCezQ65VoIOZTovxxPDNfPYPfz13bG3YgRRDI7wrVnX2Ww4FRX0lE4OWIfy0DeG0sBM0U2/gaYKWugpls6p8IENWB0XkM87y65fbNJIUG0fgV9KWcdfs5JIFapyY1BxMfR0mYwvSQZAc06BO1ZH4eoNj0gLzowOPjH7LiBrAHPYyY4k6YDDHwhl4H3rudJON1zgRwpIsWsaJ0CDnEInY5LnEwTrTieSYRhN+LLuZXcTpMdayc4eoiSTyjXxqqKBjItQljNOEzHTqOV1hW5ryuoNV4lH9jpdb+1u6XFzSGNQwFhfVjaIA6y3Z70bUOY')

version_label = 'new_version'
application_name = 'vikash_application'
environment_name = 'Application_env'


def createNewVersion():
    try:
        ebsClient.create_application_version(
            ApplicationName=application_name,
            VersionLabel=version_label,
            Description='My Website',
            SourceBundle={
                'S3Bucket': 'Vikash_Rajput',
                'S3Key': '1901216.zip'
            },
            AutoCreateApplication=True,
            Process=False
        )
        print('application Created')
    except Exception as e:
        print('some error has occured: ', e)


def createEnvironment():
    try:
        ebsClient.create_environment(
            ApplicationName=application_name,
            EnvironmentName=environment_name,
            Description='My web app environment',
            CNAMEPrefix='VIKASH_RAJPUT',
            Tier={
                'Name': 'WebServer',
                'Type': 'Standard',
            },
            VersionLabel=version_label,
            SolutionStackName='64bit Amazon Linux 2 v3.3.5 running Python 3.8',
            OptionSettings=[
                {
                    'Namespace': 'aws:autoscaling:launchconfiguration',
                    'OptionName': 'IamInstanceProfile',
                    'Value': 'aws-elasticbeanstalk-ec2-role'
                },
            ],
        )
        print('Environment Created')
    except Exception as e:
        print('some error has occured: ', e)


createNewVersion()
time.sleep(20)
createEnvironment()