from shoppon.logs import my_syslog

LOG = my_syslog.get_logger()


def main():
    my_syslog.init()
    LOG.info("This is test message.")
