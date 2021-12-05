# DB instance identifier : database-1
# username : admin
# password : Vikash2002
# host : database-1.czg5oxs8jo6c.us-east-1.rds.amazonaws.com
# port no: 3306

import boto3
import botocore
import time
import mysql.connector
import pymysql
def main():
    db_identifier = 'database-1'
    rds = boto3.client('rds',region_name = 'us-east-1',aws_access_key_id='ASIAW7PYSJHAMKWTXTUR',
aws_secret_access_key='sidzvkFk6/ylpZuKGXQTmioSyglLbkdzaxvK+A9p',
aws_session_token='FwoGZXIvYXdzELX//////////wEaDDsRDZU81QEGdXUsqyLJAZUHVy/Vlv/wg3wJJgkElXlCezQ65VoIOZTovxxPDNfPYPfz13bG3YgRRDI7wrVnX2Ww4FRX0lE4OWIfy0DeG0sBM0U2/gaYKWugpls6p8IENWB0XkM87y65fbNJIUG0fgV9KWcdfs5JIFapyY1BxMfR0mYwvSQZAc06BO1ZH4eoNj0gLzowOPjH7LiBrAHPYyY4k6YDDHwhl4H3rudJON1zgRwpIsWsaJ0CDnEInY5LnEwTrTieSYRhN+LLuZXcTpMdayc4eoiSTyjXxqqKBjItQljNOEzHTqOV1hW5ryuoNV4lH9jpdb+1u6XFzSGNQwFhfVjaIA6y3Z70bUOY')
    try:
        rds.create_db_instance(DBInstanceIdentifier=db_identifier,
                               AllocatedStorage=200,
                               DBName='Vikash_Rajput',
                               Engine='MySQL',
                               # General purpose SSD
                               StorageType='gp2',
                               StorageEncrypted=True,
                               AutoMinorVersionUpgrade=True,
                               # Set this to true later?
                               MultiAZ=False,
                               MasterUsername='admin',
                               MasterUserPassword='Vikash2002',
                               VpcSecurityGroupIds=['sg-0a2cebf72c9753e59'],
                               DBInstanceClass='db.t2.micro'
                               )
        print('Starting RDS instance with ID: ',db_identifier)
    except botocore.exceptions.ClientError as e:
        print(e)


    running = True
    while running:
        response = rds.describe_db_instances(DBInstanceIdentifier = db_identifier)

        db_instances = response['DBInstances']
        if len(db_instances) != 1:
            raise Exception('More than one DB instance returned; this should never happen')

        db_instance = db_instances[0]

        status = db_instance['DBInstanceStatus']

        print('Last DB status: ',status)

        time.sleep(5)
        if status == 'available':
            endpoint = db_instance['Endpoint']
            host = endpoint['Address']
            # port = endpoint['Port']

            print('DB instance ready with host: ',host)
            running = False


if __name__ == '__main__':
    main()



try:
    dbs = rds.describe_db_instances()
    for db in dbs['DBInstances']:
        print((db['MasterUsername'],db['Endpoint']['Address'],db['Endpoint']['Port'],db['DBInstanceStatus']))
except Exception as e:
    print(e)

# creating database
# cursur = db.cursor()
# sql = '''create a database Vikash_Rajput'''
# cursor.execute(sql)

# connecting to mysql

db_connection = mysql.connector.connect(
    host = 'database-1.czg5oxs8jo6c.us-east-1.rds.amazonaws.com',
    port = '3306',
    user = 'admin',
    password = 'Vikash2002',
    database = 'Vikash_Rajput',
)


        

print(db_connection)
print('successful')
db = db_connection.cursor()

db.execute('use Vikash_Rajput')
# query
db.execute('create table prime(name varchar(15) primary key,pass varchar(15)')

db.execute('insert into prime values(dp102,12345)')

# create new table 
db.execute('create table Student(name varchar(15), city varcahar(15)')


inst = boto3.resource('ec2')
file_h = open('apache_script.sh')
s = ''
for lines in file_h:
    s +=lines

# connecting To instance
instances = inst.create_instances(
    ImageId = 'ami-087c17d1fe0178315',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'CS351-2021',
    SecurityGroupIds = ['sg-00ab94d8db2846b6e'],
    UserData = s
)

micro_ins = instance[0]
micro_ins.wait_unti_running()
micro_ins.load()
print(micro_ins.pulic_dns_name)




# delete = rds.delete_db_instance(
#     DBInstanceIdentifier = 'database-2',
#     SkipFinalSnapshot = True
# )
# print('Deleted')



# try:
#     dbs = rds.describe_db_instance()
#     for db in dbs['DBInstances']:
#         print(db['MasterUsername'],db['Endpoint']['Address'],db['Endpoint']['Port'],db['DBInstanceStatus'])
# # expect Exception as e:
#     # print(e)
