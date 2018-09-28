"""VirtuinBridge shall be used to launch Virtuin-based tests from Anduin."""
from __future__ import print_function
import json
import threading
import tempfile
import os
import time

# Python 3 modules
try:
    from urllib.request import urlopen
    from xmlrpc.server import SimpleXMLRPCServer
    from xmlrpc.server import SimpleXMLRPCRequestHandler

# Python 2 modules
except ImportError:
    from urllib2 import urlopen
    from SimpleXMLRPCServer import SimpleXMLRPCServer
    from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


# IronPython modules
try:
    from System.Diagnostics import Process
    __VIRT_ANDUIN_ENV__ = True

# Python 2/3 modules
except ImportError:
    __VIRT_ANDUIN_ENV__ = False
    from subprocess import Popen, PIPE

# pylint: disable=relative-import
import virtuinglobalstubs as anduinFuncStubs
# from . import virtuinglobalstubs as anduinFuncStubs

# Create stubs for Anduin injected global routines
ANDUIN_GLOBAL_STUBS = dict()
for name in dir(anduinFuncStubs):
    if name.startswith('_'):
        continue
    attr = getattr(anduinFuncStubs, name, None)
    ANDUIN_GLOBAL_STUBS[name] = attr


def runCommand(args, inputStr=None):
    """
    Helper function to run child process using .NET Process or built-in subprocess
    Args:
        args (list: str): Command arguments w/ first
        being executable.
        inputStr (str, None): Standard input to pass in.
    Returns:
        str: Standard output
        str: Standard error
        int: Process exit code
    """
    p = None
    stdout = None
    stderr = None
    code = 130
    try:
        if __VIRT_ANDUIN_ENV__:
            p = Process()
            have_stdin = inputStr is not None
            p.StartInfo.UseShellExecute = False
            p.StartInfo.RedirectStandardInput = have_stdin
            p.StartInfo.RedirectStandardOutput = True
            p.StartInfo.RedirectStandardError = True
            p.StartInfo.FileName = args[0]
            p.StartInfo.Arguments = " ".join(args[1:])
            p.Start()
            if have_stdin:
                p.StandardInput.Write(inputStr)
            p.WaitForExit()
            stdout = p.StandardOutput.ReadToEnd()
            stderr = p.StandardError.ReadToEnd()
            code = p.ExitCode
        else:
            p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            stdout, stderr = p.communicate(inputStr)
            code = p.returncode
        return stdout, stderr, code
    except KeyboardInterrupt:
        if p:
            p.kill()
            stderr = 'Process terminated by user. {0}'.format(stderr if stderr else '')
            code = 130
        return stdout, stderr, code


def net2dict(obj):
    """
    Converts .NET object public primitive attributes to python dict.
    .NET bool gets mapped to int due to IronPython compatibility issue.
    Function performs only shallow mapping (non-recursive).
    Args:
        obj (.Net object): .Net object
    Returns:
        dict: converted python dict
    """
    def _isPrimitive(var):
        return isinstance(var, (int, float, bool, str))

    attrs = (name for name in dir(obj) if not name.startswith('_') and
             _isPrimitive(obj.__getattribute__(name)))
    objDict = dict()
    for attribute in attrs:
        val = obj.__getattribute__(attribute)
        # IronPython json uses incorrect boolean so change to int
        val = int(val) if isinstance(val, bool) else val
        objDict[attribute] = val
    return objDict


def getVirtuinGUI():
    """
    Helper function to find Virtuin GUI
    Args:
        None
    Returns:
        str: GUI Path
    """
    # Check if VirtuinGUI is env variable and exists
    virtuinGUI = os.environ.get('VIRT_GUI_PATH', None)
    if virtuinGUI and os.path.isfile(virtuinGUI) and os.access(virtuinGUI, os.X_OK):
        return virtuinGUI

    # Check if VIRT_PATH/bin/VirtuinGUI exists
    virtuinPath = os.environ.get('VIRT_PATH', '')
    virtuinGUI = os.path.join(virtuinPath, 'bin', 'VirtuinGUI.exe').replace('\\', '/')
    if virtuinGUI and os.path.isfile(virtuinGUI) and os.access(virtuinGUI, os.X_OK):
        return virtuinGUI
    virtuinGUI = os.path.join(virtuinPath, 'bin', 'VirtuinGUI.exe.lnk').replace('\\', '/')
    if virtuinGUI and os.path.isfile(virtuinGUI) and os.access(virtuinGUI, os.X_OK):
        return virtuinGUI

    # See if already on path
    virtuinGUI = 'VirtuinGUI.exe'
    if os.path.isfile(virtuinGUI) and os.access(virtuinGUI, os.X_OK):
        return virtuinGUI

    raise Exception('Unable to locate VirtuinGUI')


class AnduinAPIServer(threading.Thread):
    """
    AnduinAPIServer acts as Anduin DB proxy via XML-based RPC server
    """
    def __init__(self, anduinGlobals, port):
        super(AnduinAPIServer, self).__init__()
        self.server = None
        self.anduinGlobals = anduinGlobals
        self.port = port

    def addResults(self, results):
        """
        XMLRPCServer routine to add DB results
        Args:
            results: Array of results
        Returns:
            bool: Success
        """
        self.processTestResults(results)
        return True

    def processTestResults(self, results):
        """
        Processes DB results
        Args:
            results: Array of results
        Returns:
            str: Error message
        """
        error = None
        results = results if isinstance(results, list) else [results]
        for result in results:
            try:
                self.processTestResult(result)
            except Exception as err:  # pylint: disable=broad-except
                error = err
        return error

    def processTestResult(self, result):
        """
        Processes DB result dict
        Args:
            result: DB result dict
        Returns:
            None
        """
        anduinGlobals = self.anduinGlobals
        rstType = result.get('type', '').lower()
        rstName = result.get('name', None)
        rstUnit = result.get('unit', None)
        rstValue = result.get('value', None)
        rstDisplay = result.get('display', False)
        if rstType == 'blob':
            value = rstValue.encode() if isinstance(rstValue, str) else rstValue
            anduinGlobals['AddResultBlob'](rstName, rstUnit, value)
        elif rstType == 'text':
            anduinGlobals['AddResultText'](rstName, rstUnit, rstValue, rstDisplay)
        elif rstType == 'scalar':
            anduinGlobals['AddResultScalar'](rstName, rstUnit, rstValue, rstDisplay)
        elif rstType == 'list':
            anduinGlobals['AddResultList'](rstName, rstUnit, rstValue)
        elif rstType == 'file':
            if str(type(rstValue)) == "<type 'unicode'>":
                anduinGlobals['AddResultText'](rstName, 'Link', '{0}'.format(rstValue))
            elif isinstance(rstValue, str):
                anduinGlobals['AddResultText'](rstName, 'Link', '{0}'.format(rstValue))
            elif isinstance(rstValue, dict):
                srcURL = rstValue.get('src')
                dstPath = rstValue.get('dst')
                dstFolder = os.path.dirname(dstPath)
                if not os.path.exists(dstFolder):
                    os.makedirs(dstFolder)
                with open(dstPath, 'wb') as fp:
                    fp.write(urlopen(srcURL).read())
                anduinGlobals['AddResultText'](rstName, 'Link', str.format('{:s}', dstPath))
            else:
                raise Exception('AddResultText: Value must be either string or dict.')
        elif rstType == 'flush':
            anduinGlobals['FlushMetrics']()
        elif rstType == 'channel':
            anduinGlobals['SetChannel'](rstValue)

    def run(self):
        """
        Runs proxy thread
        Args:
            None
        Returns:
            None
        """
        class RequestHandler(SimpleXMLRPCRequestHandler):
            """RequestHandler"""
            rpc_paths = ('/RPC', '/')
        self.server = SimpleXMLRPCServer(
            ("0.0.0.0", self.port),
            requestHandler=RequestHandler,
            allow_none=True
        )
        self.server.register_introspection_functions()
        self.server.register_function(self.addResults, 'addResults')
        self.server.serve_forever()

    def shutdown(self):
        """ Shutdown proxy"""
        if self.server:
            self.server.shutdown()
        self.server = None

class VirtuinBridge(object):
    """
    VirtuinBridge used to launch Virtuin from Anduin via IronPython script
    """
    def __init__(self, anduinGlobals, anduinDBPort=8008):
        self.anduinGlobals = ANDUIN_GLOBAL_STUBS.copy()
        self.anduinGlobals.update(anduinGlobals or {})
        self.anduinDBPort = anduinDBPort
        self.anduinAPIProxy = AnduinAPIServer(self.anduinGlobals, self.anduinDBPort)

    def getAnduinData(self):
        """
        Extracts Anduin configs that are injected globally including
        slot, slot.Dut, station, and TestSpecs
        Args:
            None
        Returns:
            dict: Python dict with keys dut, station, and specs.
        """
        anduinGlobals = self.anduinGlobals
        configs = dict(dut={}, station={}, specs={})
        # On Anduin get real configs
        if __VIRT_ANDUIN_ENV__:
            lclDut = net2dict(anduinGlobals['slot'].Dut)
            configs['dut'].update(lclDut)
            lclStation = net2dict(anduinGlobals['station'])
            kvKey = 'translateKeyValDictionary'
            stationConstants = anduinGlobals[kvKey](anduinGlobals['station'].Constants)
            lclStation.update(stationConstants)
            configs['station'].update(lclStation)
            for specName, specDict in anduinGlobals['TestSpecs'].iteritems():
                fullSpecDict = dict(lsl=None, usl=None, details='')
                fullSpecDict.update(specDict.copy())
                if "counts_in_result" in fullSpecDict:
                    # IronPython json uses incorrect boolean so change to string
                    fullSpecDict["counts"] = str(fullSpecDict["counts_in_result"])
                    fullSpecDict["counts_in_result"] = fullSpecDict["counts"]
                configs['specs'][specName] = fullSpecDict
        # Get dummy configs
        else:
            configs['dut'] = anduinGlobals.get('dut', {})
            configs['specs'] = anduinGlobals.get('specs', {})
            configs['station'] = anduinGlobals.get('station', {})
        return configs

    def runAPIProxy(self):
        """
        Only runs API proxy
        Args:
            None
        Returns:
            None
        """
        try:
            self.anduinAPIProxy.start()
            while self.anduinAPIProxy.is_alive():
                time.sleep(2)
            self.anduinAPIProxy.shutdown()
        except KeyboardInterrupt:
            self.anduinAPIProxy.shutdown()
        except Exception:  # pylint: disable=broad-except
            self.anduinAPIProxy.shutdown()
        finally:
            self.anduinAPIProxy.join()

    def runCollection(self, collection, resultDBURL=None):
        """
        Runs Virtuin based test given supplied configs.
        Returns all results returned by test.
        Args:
            collection (dict): Virtuin Collection
        Returns:
            str|None: Error message or None
            list: Results list of dict objects
        """
        errcode = 2
        error = None
        try:
            # Create I/O files for Virtuin
            collectionPath = tempfile.mktemp(dir=None, suffix='.json')
            print('[VIRT] Collection path: {0}'.format(collectionPath))
            errcode = 0
            # pylint: disable=unused-variable
            stdout = ''
            stderr = ''
            # Write test configs to file
            with open(collectionPath, 'w') as fp:
                json.dump(collection, fp, skipkeys=True, ensure_ascii=True)

            # Start Anduin API Proxy
            self.anduinAPIProxy.start()

            # Run Virtuin and block until complete
            virtuinGUI = getVirtuinGUI()
            cmd = [virtuinGUI, '--collection', collectionPath]
            stdout, stderr, errcode = runCommand(args=cmd, inputStr=None)
            error = stderr
            self.anduinAPIProxy.shutdown()
            self.anduinAPIProxy.join()
            if errcode == 0 or errcode == 1:
                if resultDBURL:
                    results = json.loads(urlopen(resultDBURL).read())
                error = self.anduinAPIProxy.processTestResults(results.get('results', []))

            if __VIRT_ANDUIN_ENV__:
                os.remove(collectionPath)
            return errcode, error

        # Catch any exceptions
        except KeyboardInterrupt:
            self.anduinAPIProxy.shutdown()
            self.anduinAPIProxy.join()
            error = 'Process terminated by user'
            return errcode, error

        except Exception as err:  # pylint: disable=broad-except
            self.anduinAPIProxy.shutdown()
            self.anduinAPIProxy.join()
            error = err.message
            return errcode, error


if __name__ == "__main__":
    try:
        bridge = VirtuinBridge(dict(), 8008)
        bridge.runAPIProxy()
    except Exception as err:  # pylint: disable=broad-except
        print('Following exception occurred: ', err)
