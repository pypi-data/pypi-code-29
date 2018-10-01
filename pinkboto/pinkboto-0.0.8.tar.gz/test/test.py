import pinkboto

aws = pinkboto.aws(profile='production', region='us-east-1')

rds = aws.find({'resource': 'aws_db_instance'}, ['DBInstanceIdentifier', 'Endpoint'])

a=1