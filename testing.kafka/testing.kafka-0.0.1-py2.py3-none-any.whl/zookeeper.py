import os
import signal
import socket

from testing.common.database import (
    Database, DatabaseFactory, get_path_of, get_unused_port
)

__all__ = ['ZookeeperServer', 'ZookeeperServerFactory']

ZOO_CFG_TEMPLATE = """dataDir={}
clientPort={}
maxClientCnxns=0"""

LOG4J_CFG_FILE = """zookeeper.root.logger=INFO, CONSOLE
zookeeper.console.threshold=INFO
zookeeper.log.dir=.
zookeeper.log.file=zookeeper.log
zookeeper.log.threshold=DEBUG
zookeeper.tracelog.dir=.
zookeeper.tracelog.file=zookeeper_trace.log

log4j.rootLogger=${zookeeper.root.logger}

log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender
log4j.appender.CONSOLE.Threshold=${zookeeper.console.threshold}
log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout
log4j.appender.CONSOLE.layout.ConversionPattern=%d{ISO8601} [myid:%X{myid}] - %-5p [%t:%C{1}@%L] - %m%n

log4j.appender.ROLLINGFILE=org.apache.log4j.RollingFileAppender
log4j.appender.ROLLINGFILE.Threshold=${zookeeper.log.threshold}
log4j.appender.ROLLINGFILE.File=${zookeeper.log.dir}/${zookeeper.log.file}

log4j.appender.ROLLINGFILE.layout=org.apache.log4j.PatternLayout
log4j.appender.ROLLINGFILE.layout.ConversionPattern=%d{ISO8601} [myid:%X{myid}] - %-5p [%t:%C{1}@%L] - %m%n

log4j.appender.TRACEFILE=org.apache.log4j.FileAppender
log4j.appender.TRACEFILE.Threshold=TRACE
log4j.appender.TRACEFILE.File=${zookeeper.tracelog.dir}/${zookeeper.tracelog.file}

log4j.appender.TRACEFILE.layout=org.apache.log4j.PatternLayout
log4j.appender.TRACEFILE.layout.ConversionPattern=%d{ISO8601} [myid:%X{myid}] - %-5p [%t:%C{1}@%L][%x] - %m%n
"""

class ZookeeperServer(Database):

    DEFAULT_SETTINGS = dict(auto_start=2,
                            base_dir=None,
                            java_bin=None,
                            port=None,
                            zookeeper_home=None,
                            copy_data_from=None)

    subdirectories = ['data', 'log', 'cfg']

    def initialize(self):
        self.java_bin = self.settings.get('java_bin')
        if self.java_bin is None:
            self.java_bin = get_path_of('java')

        self.zookeeper_home = self.settings.get('zookeeper_home')
        if self.zookeeper_home is None:
            self.zookeeper_home = '/usr/share/java/zookeeper'

        self.log_dir = os.path.join(self.base_dir, 'log')
        self.cfg_dir = os.path.join(self.base_dir, 'cfg')
        self.data_dir = os.path.join(self.base_dir, 'data')

    def url(self):
        return "localhost:{}".format(self.client_port)

    def get_data_directory(self):
        return os.path.join(self.base_dir, 'data')

    def prestart(self):
        super(ZookeeperServer, self).prestart()
        self.client_port = self.settings['port']
        with open(os.path.join(self.cfg_dir, 'zoo.cfg'), 'w') as cfgfile:
            cfgfile.write(ZOO_CFG_TEMPLATE.format(self.data_dir, self.client_port))
        with open(os.path.join(self.cfg_dir, 'log4j.properties'), 'w') as cfgfile:
            cfgfile.write(LOG4J_CFG_FILE)

    def get_server_commandline(self):
        cmd = [self.java_bin,
               '-Dzookeeper.log.dir=' + self.log_dir,
               '-Dzookeeper.root.logger=INFO,ROLLINGFILE',
               '-cp', self.zookeeper_home + '/*',
               '-Dlog4j.configuration=file:' + os.path.join(self.cfg_dir, 'log4j.properties'),
               '-Dcom.sun.management.jmxremote',
               'org.apache.zookeeper.server.quorum.QuorumPeerMain',
               os.path.join(self.cfg_dir, 'zoo.cfg')]

        return cmd

    def is_server_available(self):
        sock = None
        try:
            sock = socket.socket()
            sock.connect(('localhost', self.client_port))
            return True
        except Exception as e:
            return False
        finally:
            if sock:
                sock.close()

    def pause(self):
        """stops service, without calling the cleanup"""
        self.terminate(signal.SIGTERM)


class ZookeeperServerFactory(DatabaseFactory):
    target_class = ZookeeperServer
