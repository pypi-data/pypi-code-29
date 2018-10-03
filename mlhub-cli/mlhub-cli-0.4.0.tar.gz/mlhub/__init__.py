import argparse
from PyInquirer import style_from_dict, Token, prompt, Validator, ValidationError
import tarfile
import tempfile
import os
from shutil import copyfile
from halo import Halo
from google.cloud import storage
import re

package_path = os.path.dirname(os.path.abspath(__file__))

def init():
    fname = os.path.join(package_path, 'PredictionModel.py')
    if not os.path.isfile('PredictionModel.py') or prompt([dict(type='confirm', name='create_file', message='Overwrite existing `PredictionModel.py` file?', default=False)])['create_file']:
        print('Creating `PredictionModel.py` file...')
        copyfile(fname, 'PredictionModel.py')

def deploy(name):
    if not os.path.isfile('PredictionModel.py'):
        print('There doesn\'t seem to be a `PredictionModel.py` file here. Run `mlhub init` to get a basic template and edit it to your needs.')
        return

    def validate_name(name):
        if re.match('^[a-zA-Z][A-Za-z0-9-]*$', name):
            return True
        else:
            return 'Only letter, digits and dashes. Start with a letter.'

    if not validate_name(name):
        raise ValueError('Invalid model name, use only letter, digits and dashes. Start with a letter.')

    class DescValidator(Validator):
        def validate(self, desc):
            if len(desc.text):
                return True
            else:
                raise ValidationError('Required field.')

    answers = prompt([
        dict(type='input', name='desc', message='Input a description for this deployment', validate=DescValidator),
        dict(type='list', name='env', message='Select a python environment', choices=('python3', 'python2'), default='python3'),
    ])

    tmp, spinner = False, Halo()
    try:
        desc = answers['desc']
        env = answers['env']

        spinner.start('Checking name availability...')
        bucket = storage.Client.from_service_account_json(package_path + '/sa.json').bucket('mlhub-firebase.appspot.com')
        if bucket.blob(name + '.tar.gz').exists():
            raise ValueError('The name `%s` is already taken' % name)
        spinner.succeed()

        spinner.start('Compressing current directory...')
        tmp = tempfile.mktemp()
        open(tmp, 'a').close() # create tmp file
        with tarfile.open(tmp, 'w:gz') as archive:
            archive.add('.', arcname='/')
        spinner.succeed()

        spinner.start('Uploading archive to mlhub...')
        blob = bucket.blob(name + '.tar.gz')
        blob.metadata = dict(name=name, env=env, desc=desc)
        blob.upload_from_filename(tmp, content_type='application/gzip')
        spinner.succeed()
        spinner.succeed('Done!')
        spinner.succeed('View your new deployment at: https://mlhub-firebase.firebaseapp.com/')
        spinner.succeed('Use your new REST API endpoint at: https://mlhub-firebase.firebaseapp.com/api/%s/' % name)
        spinner.info('Note: Your endpoint may take a few minutes to warm up before its fully available.')
    except Exception as e:
        spinner.fail('An error occured: %s' % str(e))
    finally:
        if tmp:
            os.remove(tmp)

def main():
    parser = argparse.ArgumentParser()
    command = parser.add_subparsers(dest='command', help='The command to run')
    command.required = True
    init_cmd = command.add_parser('init', help='Initalize the current directory with a `PredictionModel.py` file')
    deploy_cmd = command.add_parser('deploy', help='Deploy the current directory to mlhub')
    deploy_cmd.add_argument('model_name', help='A unique name for your model deployment')

    args = parser.parse_args()

    if args.command == 'init':
        init()
    if args.command == 'deploy':
        deploy(args.model_name)

if __name__ == '__main__':
    main()
