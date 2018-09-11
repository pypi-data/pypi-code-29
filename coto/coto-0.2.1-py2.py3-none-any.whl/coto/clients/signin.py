from bs4 import BeautifulSoup
from pyotp import TOTP
from urllib import parse
import json
from . import BaseClient


class Client(BaseClient):
    REQUIRES_AUTHENTICATION = False
    _REDIRECT_URL = "https://console.aws.amazon.com/console/home?state=hashArgs%23&isauthcode=true"

    def __init__(self, session):
        super().__init__(session)
        self.__csrf_token = None
        self.__session_id = None

    def _csrf_token(self):
        if self.__csrf_token == None:
            self._get_tokens()

        return self.__csrf_token

    def _session_id(self):
        if self.__session_id == None:
            self._get_tokens()

        return self.__session_id

    def _get_tokens(self):
        r = self.session()._get(
            "https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Fstate%3DhashArgs%2523%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fhomepage&forceMobileApp=0"
        )

        if r.status_code != 200:
            raise Exception("failed get tokens")

        soup = BeautifulSoup(r.text, 'html.parser')
        meta = {
            m['name']: m['content']
            for m in soup.find_all('meta') if 'name' in m.attrs
        }
        self.__csrf_token = meta['csrf_token']
        self.__session_id = meta['session_id']

    def _action(self, action, data=None, api="signin"):
        """
        Execute an action on the signin API.

        Args:
            action: Action to execute.
            data: Arguments for the action.

        Returns:
            dict: Action response.
        """
        if not data:
            data = {}

        data['action'] = action
        data['redirect_uri'] = self._REDIRECT_URL
        data['csrf'] = self._csrf_token()
        data['sessionId'] = self._session_id()

        r = self.session()._post(
            "https://signin.aws.amazon.com/{0}".format(api),
            data=data,
        )

        if r.status_code != 200:
            print(r.text)
            raise Exception("failed action {0}".format(action))

        out = json.loads(r.text)
        if out['state'].lower() != 'success':
            if 'Message' in out['properties']:
                raise Exception("failed action {0}: {1}".format(action, out['properties']['Message']))
            else:
                raise Exception("failed action {0}".format(action))

        return out['properties']

    def get_account_type(self, email):
        """
        Determine the type of account.

        Account Types:
            Coupled: Coupled to an amazon.com account.
            Decoupled: Independend from amazon.com.
            Unknown: Non-existent account.

        Request Syntax:

            .. code-block:: python

                response = client.get_account_type(
                    email=str,
                )

        Args:
            email: Account email address.

        Returns:
            str: Account type
        """
        response = self._action('resolveAccountType',
                            {'email': email})
        print(response)
        return response['resolvedAccountType']

    def mfa_required(self, email):
        mfa_client = self.session().client('mfa')
        mfa = mfa_client.get_mfa_status(email)
        if 'mfaType' in mfa:
            if mfa['mfaType'] != 'SW':
                raise Exception("cannot handle hardware mfa tokens")

            return True

        return False

    def signin(self, email, password, mfa_secret=None):
        # check account type
        account_type = self.get_account_type(email)

        # check mfa
        mfa_required = self.mfa_required(email)
        if mfa_required and (mfa_secret is None or len(mfa_secret) == 0):
            raise Exception("account mfa protected but no secret provided")

        if not mfa_required:
            mfa_secret = None

        if account_type == 'Decoupled':
            return self.signin_decoupled(email, password, mfa_secret)
        elif account_type == 'Coupled':
            raise Exception(
                "coupled account signin not supported {0}".format(email))
        elif account_type == 'Unknown':
            raise Exception("account {0} not active".format(email))
        else:
            raise Exception("unsupported account type {0}".format(email))

    def signin_decoupled(self, email, password, mfa_secret=None):
        """
        Signin into the AWS Management Console using account root user.

        Request Syntax:

            .. code-block:: python

                response = client.get_account_type(
                    email=str,
                    password=str,
                    mfa_secret=str,
                )

        Args:
            email: Account email address.
            password: Account password.
            mfa_secret: Account mfa secret. The Base32 seed defined as specified
                in RFC3548. The Base32StringSeed is Base64-encoded.

        Returns:
            bool: Signin successful
        """
        data = {
            'email': email,
            'password': password,
            'client_id': 'arn:aws:iam::015428540659:user/homepage',
        }

        if mfa_secret is not None:
            data['mfa1'] = TOTP(mfa_secret).now()

        # an exception is thrown if authentication was unsuccessful
        self._action('authenticateRoot', data)
        self.session().authenticated = True
        self.session().root = True
        return True

    def get_password_recovery_captcha(self):
        """
        Obtains a captcha for password recovery.

        The value ``CES`` must be used as ``captcha_token`` in
        :py:meth:`get_reset_password_token`.

        Returns:
            dict: Response Syntax

            .. code-block:: python

                {
                    'CES': str,
                    'Captcha': bool,
                    'CaptchaURL': str,
                    'captchaObfuscationToken': str,
                }
        """
        return self._action('captcha', {'forgotpassword': True})

    def get_reset_password_token(self, captcha_token, captcha_guess, email):
        """
        Asks for a password reset token to be sent to the registered email
        address.

        The value token url from the resulting email must be used as
        ``reset_token_url`` in :py:meth:`reset_password`.

        Returns:
            dict: Response Syntax

            .. code-block:: python

                {
                    'recovery_result': 'email_sent'
                }
        """
        return self._action(
            'getResetPasswordToken', {
                'captcha_token': captcha_token,
                'captcha_guess': captcha_guess,
                'email': email,
            })
