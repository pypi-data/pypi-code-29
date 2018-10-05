def main():
    import os
    from kivy.config import Config
    Config.read(os.path.join('Client', 'android.ini'))

    from LRC.Common.logger import logger
    from LRC.Client.ClientUI import ClientUI

    logger.set_logger('kivy')

    # start application
    ClientUI().run()


if '__main__' == __name__:
    main()
