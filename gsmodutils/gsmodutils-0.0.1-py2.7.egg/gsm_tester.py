from gsmodutils.project import GSMProject
import cameo
import sys
import StringIO
import contextlib
import os
import glob
import json
from collections import defaultdict


@contextlib.contextmanager
def stdoutIO(stdout=None):
    """
    Context to capture standard output of python executed tests during run time
    This is displayed to the user for them to see
    """
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def test_model_default(model):
    """
    Basic model tests
    Ensures a model loads, validates and finds a solution
    """
    solution = model.solve()
    validation_messages = validate_model(model)

    # Test all conditions
    
    # Test all 




class LogRecord(object):
    """Class for handling different types of errors"""
    def __init__(self):
        self.success = []
        self.error = []


class GSMTester(object):
    """
    Loads models and executes user specified tests for the genome scale models
    """
    
    def __init__(self, project_path, **kwargs):
        """Creates the storage locations for logs"""
        self.project = GSMProject(project_path)
        self.log = defaultdict(LogRecord)
        self._load_json_test()
        self.load_errors = []
        self.syntax_errors = dict()
        
    
    def _load_json_tests(self):
        """
        Load all json files from test directory, validate format and add tests to be run
        """
        def req_fields(entry):
            _required_fields = [
                'conditions', 'models', 'designs', 'reaction_fluxes', 'required_reactions', 'description'
            ]
        
            for rf in _required_fields:
                if rf not in entry:
                    return False
            return True 
        
        load_errors = []
        invalid_tests = []
        
        for tf in glob.glob(os.path.join(self.project.test_dir, "test_*.json")):
            id_key = os.path.basename(tf).split(".json")[0]
            with open(tf) as test_file:
                try:
                    entries = json.load(tf)
                    
                    for entry_key, entry in entires.items():
                        if req_fields(entry):
                            self._d_tests[id_key, entry_key] = entry
                        else:
                            self.invalid_tests.append((id_key, entry_key))
                except AttributeError, ValueError:
                    # Test json is invalid format
                    self.load_errors.append(id_key)


    def _entry_test(self, test_id, mdl, entry):
        """
        broken up code for testing individual entries
        """
        try:
            soltuion = mdl.solve()
                
            # Test entries that require non-zero fluxes
            for reaction_id in entry['required_reactions']:
                
                try:
                    reac = mdl.reactions.get_by_id(reaction_id)
                    
                    if reac.flux == 0:
                        # Required reaction not active at steady state
                        msg = 'required reaction {} not active'.format(reaction_id)
                        self.log[test_id].error.append(msg)
                    else:
                        # success log
                        msg = 'required reaction {} present at steady state'.format(reaction_id)
                        self.log[test_id].success.append(msg)
                    
                except KeyError:
                    #TODO: log reaction not found in errors
                    err = "required reaction {} not found in model".format(reaction_id)
                    self.log[test_id].error.append(err)
                    continue
                
            # tests for specific reaction flux ranges
            for rid, (lb, ub) in entry['reaction_fluxes'].items():
                try:
                    reac = mdl.reactions.get_by_id(rid)
                    if reac.flux < lb or reac.flux > ub:
                        err='reaction {} outside of flux bounds {}, {}'.format(reaction_id, lb, ub)
                        self.log[test_id].error.append(err)
                    else:
                        msg='reaction {} inside flux bounds {}, {}'.format(reaction_id, lb, ub)
                        self.log[test_id].success.append(msg)
                except KeyError:
                    # Error log of reaction not found
                    err = "required reaction {} not found in model".format(rid)
                    self.log[test_id].error.append(err)
                    continue
                
        except cameo.exceptions.Infeasible:
            # This is a full test failure (i.e. the model does not work)
            # not a conditional assertion
            self.failed_tests.append(test_id)

    def _dict_test(self, tf, entry_key, entry):
        """
        execute a standard test in the dictionary format
        """
        
        if not len(entry['conditions']):
            entry['conditions'] = [None]
            
        if not len(entry['designs']):
            entry['designs'] = [None]
        
        if not len(entry['models']):
            entry['models'] = self.project.config.models
        
        # load models
        for model_name in entry['models']:
            # load conditions
            mdl = self.project.load_model(model_name)
            for conditions_id in entry['conditions']:
                # load condtions
                mdl = self.project.load_conditions(model=mdl, conditions_id=conditions_id)
                for design in entry['designs']:
                    self.project.load_design()
                    test_id = ( tf, entry_key, (model_name, conditions_id, design) )
                    self._entry_test(test_id, mdl, entry)
    
    def _run_dtests(self):
        """Run entry tests"""
        for (tf, entry_key), entry in self._d_tests.items():
            self._dict_test(tf, entry_key, entry)
    
    
    def _exec_test(self, tf_name, compiled_code, test_func):
        """
        encapsulate a test function and run it storing the report
        """
        
        log_ns = self.test_results[tf_name][test_func]
        # The current project can be used as a global var
        
        # Load the module in to the namespace
        with stdoutIO() as stdout:
            global_namespace = dict(
                project=self.project,
                __name_='__gsmodtest_env__',
                __result_capture__=dict()
            )
            
            local_namespace = dict()
            try:
                exec compiled_code in global_namespace, local_namespace
            except:
                # the whole module has an error somewhere, no functions will run
                return -2
            
            try:
                # Call the function
                # BUG: FUNCTION ARGS!
                namespace[test_func]()
            except:
                # the specific test case has an error
                return -1
            
        logoutput = stdout.getvalue()
        
        return 0
        
    def _py_tests(self):
        """
        Loads and compiles each python test in the project's test path
        """
        test_files = os.path.join(self.project.tests_dir, "test_*.py")
        
        for pyfile in test_files:
            tf_name = os.basename(pyfile)
            with open(pyfile) as codestr:
                
                self.test_results[tf_name] = dict()
                try:
                    compiled_code = compile(codestr.read(), '', 'exec')
                except SyntaxError as ex:
                    # syntax error for user written code
                    # ex.lineno, ex.msg, ex.filename, ex.text, ex.offset
                    self.syntax_errors[pyfile] = ex
                    continue
            
                
                for func in code.co_names:
                    self.test_results[tf_name][func] = dict()
                    # if the function is explicitly as test function
                    if func[:5] == "test_":
                        r_code = self._exec_test(tf_name, compiled_code, func)
                        
    
    def run_all(self):
        """
        Find and run all tests for a project
        """
        pass
    
            
