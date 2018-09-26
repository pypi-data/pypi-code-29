import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from coingate_api.api_error import BadEnvironment, BadAuthToken, APIError
from coingate_api.error import Error


DEFAULT_SETTINGS = {
    'user_agent': 'CoinGate Python SDK',
    'version': '1.0',
    'retries': 3,
    'backoff_factor': 0.2,
    'status_forcelist': (500, 502, 504)
}


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


class CoingateAPI(object):

    def __init__(self, auth_token='', environment='live', **kwargs):
        super().__init__()

        if environment not in ('live', 'sandbox'):
            raise BadEnvironment(f'Environment must be live or sandbox, but "{environment}" was assigned')

        if len(auth_token) < 40:
            raise BadAuthToken(f'Auth token "{auth_token}" should be longer than 40 symbols')
        self.auth_token = auth_token

        settings = {**DEFAULT_SETTINGS}
        settings.update(kwargs)

        for k, v in settings.items():
            setattr(self, k, v)

        self._base_url = 'https://api.coingate.com/v2'
        if environment == 'sandbox':
            self._base_url = 'https://api-sandbox.coingate.com/v2'

    def url(self, url):
        return f'{self._base_url}{url}'

    @property
    def session(self):
        s = requests.Session()
        s.headers.update({
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Token {self.auth_token}',
            'User-Agent': self.user_agent
        })

        return s

    @property
    def request(self):
        return requests_retry_session(retries=self.retries, backoff_factor=self.backoff_factor,
                                      status_forcelist=self.status_forcelist, session=self.session)

    def do_request(self, url, method='post', payload=None):
        payload = {} if payload is None else {**payload}
        method = method.lower()

        url = self.url(url)
        try:
            if method == 'get':
                response = self.request.get(url=url, params=payload)
            elif method == 'post':
                response = self.request.post(url=url, data=payload)
            else:
                raise APIError(f'Wrong method of API "{method}". CoinGate v2 can work only with GET and POST methods')
        except APIError as e:
            raise e
        except Exception as e:
            raise APIError(e)

        try:
            decoded_response = response.json()
        except Exception:
            decoded_response = response.text

        if response.status_code == 200:
            return decoded_response

        Error.raise_error(response.status_code, decoded_response)

    def test_connection(self):
        return self.do_request(url='/auth/test', method='get')

    def ping(self):
        return self.do_request(url='/ping', method='get')

    def exchange_rate(self, from_='EUR', to='USD'):
        return self.do_request(url=f'/rates/merchant/{from_}/{to}', method='get')

    def exchange_rates(self):
        return self.do_request(url='/rates', method='get')

    def ip_addresses(self):
        return self.do_request(url='/ips-v4?separator=|', method='get')

    def orders(self, per_page=100, page=1, sort='created_at_desc', **kwargs):
        if per_page > 100 or per_page < 0:
            raise APIError('Number of records per page must be between 0 and 100')

        if page < 1:
            raise APIError('Wrong number of page. It must be great than 0')

        if sort not in ('created_at_desc', 'created_at_asc'):
            raise APIError('Wrong ordering. It must be one of "created_at_desc" and "created_at_asc"')

        data = {
            'per_page': per_page,
            'page': page,
            'sort': sort
        }

        if 'created_at_from' in kwargs:
            data['created_at[from]'] = kwargs.get('created_at_from')

        if 'created_at_to' in kwargs:
            data['created_at[to]'] = kwargs.get('created_at_to')

        return self.do_request(url='/orders', method='get', payload=data)

    def checkout(self, order_id, pay_currency='BTC'):
        pay_currency = pay_currency.upper()

        if 3 < len(pay_currency) < 4:
            raise APIError('Pay currency name length must be 3 or 4 symbols')

        url = f'/orders/{order_id}/checkout'

        return self.do_request(url, method='post', payload={'pay_currency': pay_currency})

    def create_order(self, price_amount, price_currency, receive_currency, **kwargs):
        price_currency = price_currency.upper()
        receive_currency = receive_currency.upper()

        for k, _ in kwargs.items():
            if k not in ('order_id', 'title', 'description', 'callback_url', 'cancel_url', 'success_url', 'token'):
                raise APIError(f'Param "{k}" is not allowed')

        if 3 < len(price_currency) < 4:
            raise APIError('Pay currency name length must be 3 or 4 symbols')

        if 3 < len(receive_currency) < 4:
            raise APIError('Receive currency name length must be 3 or 4 symbols')

        data = dict(**kwargs)
        data['price_amount'] = price_amount
        data['price_currency'] = price_currency
        data['receive_currency'] = receive_currency

        return self.do_request(url='/orders', method='post', payload=data)


