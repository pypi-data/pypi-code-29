def import_basemap():
    Basemap = None
    has_basemap = True
    try:
        from mpl_toolkits.basemap import Basemap
    except ImportError:
        has_basemap=False
        print('-W- Basemap is not installed')
        print('    If you want to make maps, look at the Cookbook install instructions:')
        print('http://earthref.org/PmagPy/Cookbook#getting_python')
    except (KeyError, FileNotFoundError):
        has_basemap = False
        print('-W- Basemap is installed but could not be imported.')
        print('    You are probably missing a required environment variable')
        print('    To use basemap, you will need to run this program or notebook in a conda env.')
        print('    For more on how to create a conda env, see: https://conda.io/docs/user-guide/tasks/manage-environments.html')
        # quit current program
        # make a copy of your environment:
        #conda create --name pmagpy_ --clone base
        # activate that environment:
        #source activate pmagpy
        # run this program
        print('    Or, you could just skip using Basemap (for now -- we are working on making this easier)')
        #if set_env.IS_WIN:
            #print('    You should quit the current program, and run the following line in your Command Prompt:')
            #print('    set "PROJ_LIB=%CONDA_PREFIX%\Library\share"')
            #print('    You can also solve this problem permanently by adding PROJ_LIB to your environment variables')
            #print('    Check out: https://www.java.com/en/download/help/path.xml for more on environment variables')
        #else:
            #print('    You should quit the current program, and run the following line in your Terminal:')
            #print('    export PROJ_LIB=$CONDA_PREFIX/share/proj')
            #print('    You can also solve this problem permanently by adding this line to your .bashrc file')
    return has_basemap, Basemap
