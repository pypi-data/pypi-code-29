""" Mail Sparkpost Driver """

from masonite.contracts.MailContract import MailContract
from masonite.drivers.BaseMailDriver import BaseMailDriver
from masonite.exceptions import DriverLibraryNotFound


class MailSparkpostDriver(BaseMailDriver, MailContract):
    """Sparkpost driver
    """

    def _sandbox_mode(self):
        if self.config.DEBUG is True:
            return True
        return False

    def send(self, message=None):
        """Sends the message through the Sparkpost service.

        Keyword Arguments:
            message {string} -- The message to be sent to Sparkpost. (default: {None})

        Returns:
            requests.post -- Returns the response as a requests object.
        """

        try:
            from sparkpost import SparkPost
        except ImportError:
            raise DriverLibraryNotFound(
                'Could not find the "sparkpost" library. Please pip install this library '
                'by running "pip install sparkpost"')

        if not message:
            message = self.message_body

        sp = SparkPost(api_key=self.config.DRIVERS['sparkpost']['api_key'])

        response = sp.transmissions.send(
            use_sandbox=self._sandbox_mode(),
            recipients=[self.to_address],
            html=message,
            from_email='{0} <{1}>'.format(self.config.FROM['name'], self.config.FROM['address']),
            subject=self.message_subject
        )

        return response