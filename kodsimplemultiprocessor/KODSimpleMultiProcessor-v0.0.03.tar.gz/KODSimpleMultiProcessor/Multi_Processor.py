import ipyparallel
import numpy
import os
import subprocess
import sys
import time


class SimpleMultiProcessor(object):
    '''  A simple interface providing simplified MultiProcessing for Jupyter notebooks.

    This class is a Context Manager that makes a command line call to start a 
    cluster of python processes on entry, and shuts them down again on exit.

    As a context manager, the exit actions take place even if the contextualised
    code throws an error or the user hits the KeyboardInterrupt. Restarting the
    Kernel however, may leave orphaned python processes running. To close them 
    down, open a Command Line Interface and run the following command:
            ipcluster stop

    Methods
    =======

    def __init__(self, cluster_count, startup_delay, modules):

        Args
        ----
        cluster_count: int, default 3, the number of processes to set up

        startup_delay: int, default 30, the delay between the command line call
                    to start the ipyparallel processes

        modules: list, a list containing the names (as strings) of modules that
                    you want to import in each process. sys is imported by default
                    if the modules list is empty or not provided.

    def pass_vars_and_funcs(var_func_dictionary):

        This method is used to pass functions and other variables to each of
        the processes. Importantly, you need to pass all non-imported functions
        and variables to the processes.

        Args
        ----
        var_func_dictionary: dict, a dictionary with the desired name of the
            function or variable, and the function or variable itself.

    def run_this(function, against, chunkify):

        This method instructs the processes to run the provided function against
        each of the items in the against list.

        Args
        ----
        function: func, the function we wish to apply. The function must take an
                    item from the against list as an argument.

        against: list, the list of objects to individually run the function against.

        chunkify: boolean, if True the against list is broken up into equally-
                    sized sublists, each of which goes to a different processor.
                    This will be useful if your function does its own chunking.
                    If False, then the function is applied to the contents of the
                    against list one at a time.

    Usage
    =======

    from KODSimpleMultiProcessor import SMP


    def distributed_function(part_of_list_to_process, *args, **kwargs):
        # You need to alias all the modules you'd normally alias here, rather
        # than when importing.
        np = numpy

        return part_of_list_to_process * 2

    # The processes will churn through a list of items, process them one at a 
    # time, and then return the results in a list.
    list_to_process = [1, 2, 3, 4, 5, 6]

    def test_func():
        pass

    test_var = 1

    var_func_dictionary = {'test_func': test_func, 'test_var': test_var}

    with SMP(cluster_count=6, modules=['sys', 'numpy']) as mp:

        mp.pass_vars_and_funcs(var_func_dictionary)

        results = mp.run_this(
                    function=distributed_function, 
                    against=list_to_process,
                    chunkify=False
                    )

    print(results)
    '''

    def __init__(self,
                cluster_count=4,
                startup_delay=30,
                modules=None
                ):

        self.cluster_count = cluster_count
        self.startup_delay = startup_delay

        self.workers = []
        self.pid_map =  []
        self.Client = None

        default_modules = ['sys']

        self.modules = modules or default_modules

        if type(self.modules) is str:
            self.modules = [self.modules]

        elif type(self.modules) is not list:
            raise ImportError('"modules" must be a single module name string, or a list of modules names as strings.')


    def __enter__(self, *args, **kwargs):
        ''' Start the clusters by calling the following on the command line:
                ipcluster start -n <cluster_count> --daemon

        Calling with the daemon argument will allow the code to keep running.

        We then wait until a connection can be made to the clusters, or the 
        startup_delay expires.

        Once a connection is established, we load the initial libraries the user
        provided in the 'modules' argument, into each processor.

         '''

        _ = subprocess.Popen(['ipcluster', 'start', '-n', str(self.cluster_count), '--daemon'])

        # Give the cluster few seconds to startup.
        time.sleep(5)

        connected = False
        retries = 0

        while not connected and retries <= self.startup_delay:

            try:
                self.Client = ipyparallel.Client()
                ar = self.Client[:].apply_async(os.getpid)
                connected = True
            except ipyparallel.error.NoEnginesRegistered:
                continue
            except ipyparallel.error.TimeoutError:
                continue
            finally:
                retries += 1
                time.sleep(1)

        self.pid_map = ar.get_dict()
        self.workers = self.Client[:]

        with self.workers.sync_imports():
            for module in self.modules:
                globals()[module] = __import__(module)

        return self

    def __exit__(self, *args, **kwargs):
        ''' Upon exit, always shut down the cluster.

            The exit actions take place even if the contextualised code throws 
            an error or the user hits the KeyboardInterrupt. Restarting the 
            Kernel however, may leave orphaned python processes running. 

            To close them down manually, open a Command Line Interface and run
            the following command:
                    ipcluster stop
        '''

        _ = subprocess.Popen(['ipcluster', 'stop'])


    def pass_vars_and_funcs(self, var_func_dictionary, *args, **kwargs):
        ''' Use this function to pass variables and functions to each of the
            workers. The workers will only have access to these variables and 
            functions in addition to the standard library. 

            The variables and functions are not shared; they are copied.

            var_func_dictionary must be a dictionary with the keys as the 
            names of the variable or function and the values being the actual
            items.
        '''

        for worker in self.Client:
            worker.push(
                var_func_dictionary,
                block = True
                )

    def run_this(self, function, against, chunkify=False, *args, **kwargs):
        ''' The function we want to run on the disparate processes, and the list
            we want to run through.

            The list called against is processed one item at a time.

            When chunkify is True, the list gets broken into equally-sized 
            sub-lists for distribution to each of the the workers.
        '''

        if chunkify:
            against = [x.tolist() for x in numpy.array_split(against, self.cluster_count)]

        return self.workers.map_sync(function, against)



if __name__ == '__main__':

    # import sys
    # sys.path.append('C:\\Stash\\ToolKit\\SimpleJupyterMultiProcessor')
    # from Multi_Processor import MultiProcessor

    def distributed_function(part_of_list_to_process, *args, **kwargs):
        # Alias all the modules you'd normally alias
        np = numpy

        return np.nan

    # The processes will churn through a list of items, process them, and 
    # return the results in a list.
    list_to_process = [1, 2, 3, 4, 5, 6]

    def test_func():
        pass

    test_var = 1

    var_func_dictionary = {'test_func': test_func, 'test_var': test_var}

    with MultiProcessor(cluster_count=6, modules=['sys', 'numpy']) as mp:

        mp.pass_vars_and_funcs(var_func_dictionary)

        results = mp.run_this(function=distributed_function, against=list_to_process)

    print(results)