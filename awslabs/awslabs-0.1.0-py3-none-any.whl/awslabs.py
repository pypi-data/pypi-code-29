import click
import importlib
import os
from awslabs.tracks.s3.mytrack import MyTrack

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
DEBUG = False

def load_class(full_class_string):
    """
    dynamically load a class from a string
    """

    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    # Finally, we retrieve the Class
    return getattr(module, class_str)

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('track', default='list')
@click.argument('action', default='validate', type=click.Choice(['start', 'validate', 'help', 'stop', 'restart']))
@click.option('--verbose/-v', is_flag=True)
def main(track = '', action = '', verbose = False):

    scriptDirectory = os.path.dirname(os.path.realpath(__file__))

    if verbose:
        os.environ["AWSLABS_VERBOSE"] = "1"
    else:
        os.environ["AWSLABS_VERBOSE"] = "0"
    
    if track == "list":
        awslabs = click.style('awslabs', fg='red')
        click.echo("\nWelcome to "+awslabs)
        click.echo("\nThe following tracks are available:\n")
        for d in os.listdir(scriptDirectory+'/tracks/'):
            if d not in ["__init__.py", "__pycache__"]:
                click.echo(" " + d)
        click.echo("\nUse the following commands to play:\n")
        click.echo(" awslabs trackname start")
        click.echo(" awslabs trackname help")
        click.echo(" awslabs trackname validate   or   awslabs trackname")
        click.echo(" awslabs trackname stop")
        click.echo(" awslabs trackname restart")
        click.echo("\n")
        exit()
    
    try:
        trackClass = load_class('awslabs.tracks.{}.mytrack.MyTrack'.format(track))(track)
    except:
        print('Track {} not found'.format(track))
        exit()
    
    getattr(trackClass, action)()


if __name__ == '__main__':
    main()