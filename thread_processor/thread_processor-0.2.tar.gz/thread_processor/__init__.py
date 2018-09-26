import copy
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)


class Thread(object):
    def __init__(
            self,
            thread_object,
            threads_args
    ):
        self.thread_object = thread_object
        self.threads_args = threads_args
        self.is_success = None
        self.exception = None

    def __repr__(self):
        return "Name: {} Args: {}".format(self.thread_object.name, self.threads_args)


class ThreadProcessor(object):
    """
    Generate tasks for each argument in a list and
    execute them on a fixed number of threads
    """

    def __init__(
            self,
            thread_func,
            thread_func_args_list,
            max_threads
    ):
        """
        :param thread_func: function to execute in each thread
        :type thread_func: function
        :param thread_func_args_list: arguments passed to thread_func
        :type thread_func_args_list: list of tuples
        :param max_threads: max number of threads to spawn
        :type max_threads: int
        """
        self.thread_func = thread_func
        self.thread_func_args_list = copy.deepcopy(thread_func_args_list)
        self.max_threads = max_threads
        self.created_threads = list()

    def start(self):
        thread_counter = 0
        create_threads = True
        monitor_threads = True
        while create_threads or monitor_threads:
            if create_threads and len(self._fetch_active_threads()) < self.max_threads:
                thread_counter += 1
                thread = self._create_thread(thread_name=thread_counter)
                if thread:
                    monitor_threads = True
                    continue
                else:
                    logging.info("No more threads to create")
                    create_threads = False
            if monitor_threads:
                active_threads = self._fetch_active_threads()
                if not active_threads:
                    monitor_threads = False
                else:
                    logging.info("Active Threads {}".format(active_threads))
                    time.sleep(10)
        logging.info("All threads complete")
        self._print_report()
        logging.info("Bye")

    def _fetch_active_threads(self):
        active_threads = list()
        for thread in self.created_threads:
            if thread.thread_object.is_alive():
                active_threads.append(thread)
        return active_threads

    def _wrapper_func(self, thread, *args):
        try:
            self.thread_func(*args)
            thread.is_success = True
        except Exception as e:
            thread.is_success = False
            thread.exception = e

    def _create_thread(self, thread_name):
        if len(self.thread_func_args_list) > 0:
            thread_args = self.thread_func_args_list.pop()
            thread = Thread(thread_object=None, threads_args=thread_args)
            wrapper_func_args = (thread,) + thread_args
            t = threading.Thread(
                name=thread_name,
                target=self._wrapper_func,
                args=wrapper_func_args
            )
            t.setDaemon(True)
            t.start()
            thread.thread_object = t
            logging.info("Started Thread {}".format(thread))
            self.created_threads.append(thread)
            return thread

    def _print_report(self):
        num_threads = len(self.created_threads)
        failed_threads = list()
        for thread in self.created_threads:
            if not thread.is_success:
                failed_threads.append(thread)
        logging.info(
            "Ran:{} Successful:{} Failed:{}"
            .format(
                num_threads,
                num_threads - len(failed_threads),
                len(failed_threads)
            )
        )
        logging.info("Failed threads: {}".format(failed_threads))
