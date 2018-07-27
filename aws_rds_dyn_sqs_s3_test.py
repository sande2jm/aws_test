import boto3
import yaml

with open('aws_rds_dyn_sqs_s3_test.yaml', 'r') as f:
    config = yaml.load(f)
print(config)

rds = boto3.client('rds')
dbs = rds.describe_db_instances()
dynamodb = boto3.resource('dynamodb')
sqs = boto3.resource('sqs',region_name='us-east-1')
s3 = boto3.resource('s3', 'us-east-1')
queue = sqs.get_queue_by_name(QueueName='test.fifo')


for x in s3.buckets.limit(1):
    print("{}".format(x))

print("sqs: {}".format(queue.url))

for table in dynamodb.tables.all():
    print("dynamodb: {}, {}".format(table.name, table.item_count))
    
for db in dbs['DBInstances']:
    print("rds: {} {} {} {}".format(
        db['MasterUsername'],db['Endpoint']['Address'],db['Endpoint']['Port'], db['DBInstanceStatus']))

rds_host  = 'test-2.cn1xyxm7ffae.us-east-1.rds.amazonaws.com'
name = 'master'
password = 'password'
db_name = 'test_1'

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    print("ERROR: Unexpected error: Could not connect to MySql instance.")

# print("Connected to Test RDS_DB")