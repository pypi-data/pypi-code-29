import pinkboto

aws = pinkboto.aws(profile='production', region='us-east-1')

aws.clean_cache()
rds = aws.find({'resource': 'aws_db_instance'})
a=1