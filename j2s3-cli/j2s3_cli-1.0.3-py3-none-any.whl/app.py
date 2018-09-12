import click
from j2s3.main import publish

@click.group()
def cli():
    """CLI for publish maven Java projects to an s3 maven repository"""

@cli.command()
@click.option('-i', '--input', help='Input directory containing Java source and pom.xml file')
@click.option('-u', '--username', help='AWS_ACCESS_KEY_ID for an IAM user with s3 access')
@click.option('-p', '--password', help='AWS_SECRET_ACCESS_KEY for an IAM user with s3 access')
@click.option('-b', '--bucket', help='Existing AWS S3 bucket name')
@click.option('--dry', is_flag=True, default=False, help='Dry run')
def publish(input, username, password, bucket, dry):
    """Publish a maven project to an s3 maven repository. 
    Your input directory must contain valid java source and a maven pom.xml file. 
    Your s3 bucket must exist and your IAM user must have GetObject and PutObject access.
    """
    click.echo('Attempting j2s3 upload')
    if dry:
        click.echo('Dry run with %s %s %s %s' % (input, username, password, bucket))
    else:
        publish(input, username, password, bucket)
    click.echo('All done')
