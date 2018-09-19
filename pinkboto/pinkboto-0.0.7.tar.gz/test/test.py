import pinkboto

aws = pinkboto.aws(profile='production', region='us-east-1', cache=3600)

# rds = aws.find({'resource': 'aws_db_instance'}, ['Endpoint.Address', 'AvailabilityZone'])
# pinkboto.to_csv(rds, 'result.csv')


selector = {'resource': 'aws_db_instance'}

projection = [
    'DBInstanceIdentifier',  # nome do banco
    'Endpoint.Address',  # endpoint
    'PubliclyAccessible',  # ip publico
    'MultiAZ',  # multi AZ
    'AvailabilityZone', 'SecondaryAvailabilityZone',  # qual zona
    'DBSubnetGroup.DBSubnetGroupName',  # qual vpcs
    'VpcSecurityGroups.VpcSecurityGroupId',  # security group
    'DBInstanceClass',  # tipo da instancia
    'Iops',  # iops reservado
    'AllocatedStorage'  # tamanho do disco
]

rds = aws.find(selector, projection)

pinkboto.to_csv(rds, 'rds.csv')
