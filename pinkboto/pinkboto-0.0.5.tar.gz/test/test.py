import pinkboto

aws = pinkboto.aws(profile='production', region='us-east-1', cache=3600)

rds = aws.find({'resource': 'aws_db_instance'}, ['Endpoint.Address', 'AvailabilityZone'])
pinkboto.to_csv(rds, 'result.csv')