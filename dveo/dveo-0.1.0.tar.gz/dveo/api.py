"""Talk to DVEO devices via REST API."""
# TODO: split _request data parsing into separate _parse_result function
# TODO: memoize input_(list|config) output_(list|config)


import hashlib
import sys
from urllib.parse import urljoin

import requests
import xmltodict


class API:
    """Instantiate a single DVEO API container object.

    :param str address: IP address or hostname of encoder.
    :param str password: Password for the apiuser account.
    :param str username: (optional) apiuser username is usually locked to `apiuser`.
    :param port: (optional) Port number configured for the API webserver,
        defaults to `25599`.
    :type port: str or int
    :param https: (optional) Enable https instead of http connections,
        defaults to `False`.
    :type https: bool
    :param str data_format: (optional) Choose between `json` and `xml` format.
        Older firmwares have problems with the JSON output format, defaults to `json`.
    """

    def __init__(
        self,
        address,
        password,
        username="apiuser",
        port="25599",
        https=False,
        data_format="json",
    ):
        """Construct object using DVEO API connection details."""
        self.address = address
        self.port = port
        self.username = username
        self.password = password
        if data_format not in ("xml", "json"):
            # TODO: raise some error
            sys.exit("Invalid data_format set, use either xml or json.")
        self.data_format = data_format

        self._session = requests.Session()
        self._session.verify = False
        self._api_key = None
        self._api_key_altform = False  # `token|username`, instead of `tokenusername`
        self._retry = False

        if https:
            self.scheme = "https"
        else:
            self.scheme = "http"
            # Disable SSL warnings, DVEO devices often use self-signed certs
            requests.urllib3.disable_warnings(
                requests.urllib3.exceptions.InsecureRequestWarning
            )

    def _string2bool(self, string):
        """Converts 'true' to True, 'false' to False and returns anything else."""
        if string == "true":
            return True
        elif string == "false":
            return False
        return string

    def _request(self, operation, payload={}):
        """Send request to API, return result data.

        :param str operation: Operation to request from the API.
        :param dict payload: Dict key:value pairs to send as POST data to API.
        """
        # TODO: deal with HTTP failures, like timeouts and DNS lookup failures
        # TODO: check operation to list of valid operations
        # TODO: check payload is composed of valid keywords
        login_ops = ("ValidKeyRequest", "HttpsGetKeyRequest", "HttpGetTokenRequest")
        if operation not in login_ops:
            if not self._api_key:
                res = self._login()
                if not res:
                    # TODO: raise some error
                    sys.exit("Failed to login")
            payload["Key"] = self._api_key

        url = "{}://{}:{}/{}/reply/".format(
            self.scheme, self.address, self.port, self.data_format
        )

        if self.data_format == "json":
            res = self._session.post(urljoin(url, operation), json=payload, timeout=5)
        else:
            res = self._session.post(urljoin(url, operation), data=payload, timeout=5)
        self.latest_res = res
        res.raise_for_status()

        if self.data_format == "json":
            result = res.json().get("Result")
            if result and isinstance(result, dict):
                output = result.get("configItems")
            else:
                output = result
        else:
            filter_ns = {"d2p1": None, "d3p1": None}
            xmlresult = xmltodict.parse(
                res.content, attr_prefix="", namespaces=filter_ns
            )
            result = xmlresult.get(operation.replace("Request", "Response"), {}).get(
                "Result"
            )
            if isinstance(result, str):
                output = self._string2bool(result)
            elif result and isinstance(result, dict):
                output = result.get("configItems", {}).get("string")
                if not isinstance(output, list):
                    output = [output]
            else:
                output = result

            if output is None:
                output = ""

        if operation not in login_ops and (
            "Authentication failure" in output
            or "error=Authentication failure" in output
        ):
            if self._retry:
                # TODO: raise some error
                sys.exit("Failed to login")

            self._api_key = None
            self._retry = True
            output = self._request(operation, payload)

        if operation not in login_ops:
            self._retry = False

        return output

    def _login(self):
        """Retrieve and set api_key for further authentication."""
        if self.scheme == "https":
            res = self._request(
                "HttpsGetKeyRequest",
                {"UserName": self.username, "Password": self.password},
            )
            if res:
                self._api_key = res
        else:
            md5 = hashlib.md5()
            token = self._request("HttpGetTokenRequest")
            tohash = self.username.upper() + "|" + self.password + "|" + token
            md5.update(tohash.encode("ascii"))
            if self._api_key_altform:
                self._api_key = md5.hexdigest() + "|" + self.username
            else:
                self._api_key = md5.hexdigest() + self.username

        if self._valid_key(self._api_key):
            return True
        elif not self._api_key_altform:
            self._api_key_altform = True
            return self._login()
        return False

    def _valid_key(self, api_key=None):
        """Test if api_key is valid."""
        if not api_key:
            api_key = self._api_key
        res = self._request("ValidKeyRequest", {"Key": api_key})
        if res:
            return True
        return False

    def list_inputs(self):
        """Return list of configured inputs."""
        res = self._request("GetInputConfigListRequest")
        return res

    def list_outputs(self, input_id):
        """Return list of outputs configured for input_id."""
        res = self._request("GetOutputConfigListRequest", {"InputStreamName": input_id})
        return res

    def input_config(self, input_id):
        """Return dict of input stream config variables."""
        res = self._request("GetStreamInputConfigRequest", {"ServiceName": input_id})
        if res:
            output = dict([x.split("=", 1) for x in res])
            return output
        return False

    def output_config(self, input_id, output_name):
        """Return dict of output stream config variables."""
        res = self._request(
            "GetStreamOutputConfigRequest",
            {"InputStreamName": input_id, "OutputStreamName": output_name},
        )
        if res:
            output = dict([x.split("=", 1) for x in res])
            return output
        return False

    def service_status(self, service_name):
        """Return status line of service (daemon or stream) as string."""
        res = self._request("GetServiceStatusRequest", {"ServiceName": service_name})
        return res

    def system_status(self):
        """Return dict of system status information."""
        res = self._request("GetSystemStatusRequest")
        if res:
            if isinstance(res, str):
                return xmltodict.parse(res, attr_prefix="").get("status")
        return False

    def reset_service(self, service_name):
        """Kill and restart a service."""
        res = self._request("ResetServiceRequest", {"ServiceName": service_name})
        if res == "":
            return True
        return res

    def restart_service(self, service_name):
        """Restart service (without killing)."""
        res = self._request("RestartServiceRequest", {"ServiceName": service_name})
        if res == "":
            return True
        return res

    def stop_service(self, service_name):
        """Stop service."""
        res = self._request("StopServiceRequest", {"ServiceName": service_name})
        if res == "":
            return True
        return res

    def start_service(self, service_name):
        """Stop service."""
        res = self._request("StartServiceRequest", {"ServiceName": service_name})
        if res == "":
            return True
        return res

    def reboot_device(self):
        """Reboot the DVEO device."""
        res = self._request("RebootDeviceRequest")
        if res == "":
            return True
        return res

    def restart_all_streams(self):
        """Kill and restart all the active streams."""
        res = self._requesT("RestartAllStreamsRequest")
        if res == "":
            return True
        return res

    def read_service_log(self, service_name):
        """Retrieve log lines for service or stream.

        :param str service_name: Name of service for which to retrieve logs
        :result: A list of log lines.
        :rtype: list
        """
        res = self._request("ReadServiceLogRequest", {"ServiceName": service_name})
        return res

    def input_by_input_name(self, input_name):
        """Lookup input_id (e.g. net_stream1) by configure input name."""
        # TODO: test if multiple streams can share same name, otherwise return x[0]
        return [
            input_id
            for input_id in self.list_inputs()
            if input_name == self.input_config(input_id).get("inputname")
        ]

    def input_by_output_name(self, output_name):
        """Lookup input_id by configured output name."""
        # TODO: test if multiple streams can share same name, otherwise return x[0]
        return [
            input_id
            for input_id in self.list_inputs()
            if output_name in self.list_outputs(input_id)
        ]

    def input_by_output_param(
        self, output_param_name, output_param_value, partial=False, include_value=False
    ):
        """Lookup input_id by output config paramater.

        :param str output_param_name: Name of output config parameter
        :param str output_param_value: Value of output config paramter
        :param partial: (optional) Allow for partial matches, defaults to `False`
        :type partial: bool
        :param include_value: (optional) Include param value in output,
            useful with `partial`, defaults to `False`
        :type include_uri: bool
        """
        lookup_table = dict(
            [
                (
                    input_id,
                    self.output_config(input_id, output_name).get(output_param_name),
                )
                for input_id in self.list_inputs()
                for output_name in self.list_outputs(input_id)
                if output_name
            ]
        )

        if partial:
            result = [
                item for item in lookup_table.items() if output_param_value in item[1]
            ]
        else:
            result = [
                item for item in lookup_table.items() if output_param_value == item[1]
            ]

        if include_value:
            return result
        else:
            return list(dict(result).keys())
