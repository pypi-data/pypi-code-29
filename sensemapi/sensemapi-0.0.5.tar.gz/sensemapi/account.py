# system modules
import logging
import inspect
import json
import time
import re
import functools
from posixpath import join as urljoin

# internal modules
from sensemapi import paths
from sensemapi.client import SenseMapClient
from sensemapi.errors import *
from sensemapi.utils import *
from sensemapi import compat
from sensemapi.senseBox import senseBox, senseBoxCollection

# external modules
import requests

logger = logging.getLogger(__name__)

class SenseMapAccount(SenseMapClient):
    """
    Client to interface an `OpenSenseMap <https://opensensemap.org>`_ account
    via the `OpenSenseMap API <https://api.opensensemap.org>`_

    Args:
        email (str, optional): the user's login email address
        password (str, optional): the user's login password
        api (str, optional): the api server to use. You may use
            :any:`OPENSENSEMAP_API_LIVE` (default) or
            :any:`OPENSENSEMAP_API_TEST` for testing purposes.
    """
    def __init__(self,
        email = None,
        password = None,
        api = paths.OPENSENSEMAP_API_LIVE,
        ):
        frame = inspect.currentframe()
        args = inspect.getargvalues(frame)[0]
        for arg in args[1:]:
            val = locals().get(arg)
            if val is not None:
                setattr(self, arg, val)

    @simplegetter
    def email(self):
        return None

    @simplesetter(email)
    def email(self, new):
        return new

    @simplegetter
    def password(self):
        return None

    @simplesetter(password)
    def password(self, new):
        return new

    @simplegetter
    def name(self):
        return None

    @simplesetter(name)
    def name(self, new):
        return new

    @simplegetter
    def role(self):
        return None

    @simplesetter(role)
    def role(self, new):
        return new

    @simplegetter
    def language(self):
        return None

    @simplesetter(language)
    def language(self, new):
        return new

    @property
    def boxes(self):
        try:
            self._boxes
        except AttributeError:
            self._boxes = senseBoxCollection()
            self._boxes.client = self
        return self._boxes

    @boxes.setter
    def boxes(self, new):
        if hasattr(new, "boxes"): # is already a senseBoxCollection
            self._boxes = new
        else:
            self._boxes = senseBoxCollection()
            self._boxes.client = self
            self._boxes.boxes = new

    @simplegetter
    def token(self):
        return None

    @simplesetter(token)
    def token(self, new):
        return new

    @simplegetter
    def refresh_token(self):
        return None

    @simplesetter(refresh_token)
    def refresh_token(self, new):
        return new

    @property
    def signed_in(self):
        """
        Whether the user is currently logged in

        :type: bool
        """
        return self.token is not None and self.refresh_token is not None

    @property
    def authorization_header(self):
        """
        Authorization header

        :type: :any:`dict`
        :getter: Return a :any:`requests`-compatible header-dict containing the
            authorization token. :any:`sign_in` if necessary.
        """
        if not self.token:
            self.sign_in()
        return {"Authorization": "Bearer {}".format(self.token)}

    def request(self, *args, **kwargs):
        """
        Wrapper around :any:`SenseMapClient.request` that handles some more
        corner cases

        Raises:
            OpenSenseMapAPIOutdatedTokenError : if the tokens are outdated
            OpenSenseMapAPIAuthenticationError : if access is prohibited
        """
        response = super().request(*args, **kwargs)
        # forbidden
        if response.status_code == 403:
            try:
                response_json = response.json()
            except compat.JSONDecodeError:
                response_json = {}
            code = response_json.get("code","")
            message = response_json.get("message","")
            if re.search("invalid.+jwt",message.lower()) or \
                re.search("refresh\s+token.+invalid.+too.+old",
                    message.lower()):
                raise OpenSenseMapAPIOutdatedTokenError(
                    (code + ": " if code else "" + message))
            if re.search("user.+password.+not\s+valid",message.lower()):
                raise OpenSenseMapAPIInvalidCredentialsError(message)
            # something else went wrong
            raise OpenSenseMapAPIAuthenticationError(
                (code + ": " if code else "" + message))
        return response

    def sign_in(self):
        """
        Sign in with the user's credentials.

        Returns:
            True : if the login process was successful

        Raises:
            OpenSenseMapAPIInvalidCredentialsError : wrong credentials
            OpenSenseMapAPIAuthenticationError : if the login did not work
        """
        assert self.email is not None, "No user email specified"
        assert self.password is not None, "No user password specified"
        response = self.request("post",
            urljoin(self.api, paths.SIGN_IN),
            json = {
                "email": self.email,
                "password": self.password,
                },
            )
        response_json = response.json()
        try:
            code = response_json["code"]
            message = response_json["message"]
            if code == "Forbidden":
                if re.search("user.+password.+not\s+valid",message.lower()):
                    raise OpenSenseMapAPIInvalidCredentialsError(message)
            if code != "Authorized":
                raise OpenSenseMapAPIAuthenticationError(
                    "Login did not work" + (": " + message or ""))
            self.token = response_json["token"]
            self.refresh_token = response_json["refreshToken"]
            data = response_json["data"]
            user = data["user"]
        except KeyError as e: # pragma: no cover
            raise OpenSenseMapAPIResponseError(
                "API response did not contain {}".format(e))
        self.read_user_details(user)
        return True

    def sign_out(self):
        """
        Sign out the user

        Returns:
            True : if the logout process was successful

        Raises:
            OpenSenseMapAPIOutdatedTokenError : if the logout did not work
        """
        if self.signed_in:
            response = self.request("post",
                urljoin(self.api, paths.SIGN_OUT),
                headers = self.authorization_header)
            response_json = response.json()
            try:
                code = response_json["code"]
                message = response_json["message"]
                if code == "Forbidden":
                    if re.search("invalid.+jwt",message.lower()):
                        raise OpenSenseMapAPIOutdatedTokenError(message)
                if code != "Ok":
                    raise OpenSenseMapAPIError(
                        "Logout did not work" + (": " + message or ""))
            except KeyError as e: # pragma: no cover
                raise OpenSenseMapAPIResponseError(
                    "API response did not contain {}".format(e))
        self.token = None
        self.refresh_token = None
        return True

    def refresh_tokens(self):
        """
        :any:`_refresh_tokens` and :any:`sign_in` again if necessary.

        Returns:
            True : if the refreshing was successful

        Raises:
            OpenSenseMapAPIAuthenticationError : if refreshing didn't work
        """
        try:
            self._refresh_tokens()
        except OpenSenseMapAPIOutdatedTokenError:
            logger.debug("Tokens are outdated. Signing in...")
            self.sign_in()
        return True

    def _refresh_tokens(self):
        """
        Attempt to refresh the tokens

        Returns:
            True : if the refreshing was successful

        Raises:
            OpenSenseMapAPIOutdatedTokenError : the refresh token is outdated
        """
        assert self.refresh_token, \
            "No refresh token available. Please sign_in()"
        response = self.request("post",
            urljoin(self.api, paths.REFRESH),
            headers = self.authorization_header,
            json = {"token": self.refresh_token},
            )
        response_json = response.json()
        try:
            code = response_json["code"]
            message = response_json["message"]
            if code == "Forbidden":
                if re.search("token.+invalid.+too.+old",message.lower()):
                    raise OpenSenseMapAPIOutdatedTokenError(message)
            if code != "Authorized":
                raise OpenSenseMapAPIError(
                    "Refreshing tokens did not work" + (": " + message or ""))
            self.token = response_json["token"]
            self.refresh_token = response_json["refreshToken"]
        except KeyError as e: # pragma: no cover
            raise OpenSenseMapAPIResponseError(
                "API response did not contain {}".format(e))
        return True

    def refresh_and_retry_on_outdated_tokens(decorated_function):
        """
        Decorator to call a decorated method, catching an
        :any:`OpenSenseMapAPIOutdatedTokenError`, then doing
        :any:`refresh_tokens` and then retries.
        """
        @functools.wraps(decorated_function)
        def wrapper(self, *args, **kwargs):
            try:
                return decorated_function(self, *args, **kwargs)
            except OpenSenseMapAPIOutdatedTokenError:
                logger.debug("Tokens are outdated. Refreshing tokens...")
                self.refresh_tokens()
            logger.debug("Now trying again to call {}"
                .format(decorated_function))
            return decorated_function(self, *args, **kwargs)
        return wrapper

    def get_box(self, id):
        """
        Call :any:`SenseMapClient.get_box` and update own boxes if present

        Args:
            id (str) : the senseBox id to retreive

        Returns:
            senseBox : the retreived senseBox
        """
        box = super().get_box(id)
        try:
            own_box = self.boxes.by_id[box.id]
            own_box.update_from_json(box.to_json())
        except KeyError:
            pass
        return box

    def get_own_boxes(self):
        """
        Run :any:`get_details` to fetch the current box ids and then
        call :any:`get_box` on all of them.

        Returns:
            senseBoxCollection : all own boxes
        """
        self.get_details()
        for box in self.boxes:
            self.get_box(box.id)
        return self.boxes

    @refresh_and_retry_on_outdated_tokens
    def get_details(self):
        """
        Get the user details

        Returns:
            True : if the retrieval was successful

        Raises:
            OpenSenseMapAPIError : if the retreival did not work
        """
        response = self.request("get",
            urljoin(self.api, paths.USER_DETAILS),
            headers = self.authorization_header,
            )
        response_json = response.json()
        try:
            code = response_json["code"]
            message = response_json.get("message")
            if code != "Ok":
                raise OpenSenseMapAPIError(
                    "Retrieving user details did not work" \
                        + (": " + message or ""))
            data = response_json["data"]
        except KeyError as e: # pragma: no cover
            raise OpenSenseMapAPIResponseError(
                "API response did not contain {}".format(e))
        try:
            user = data["me"]
        except KeyError as e: # pragma: no cover
            raise OpenSenseMapAPIResponseError(
                "API response data did not contain {}".format(e))
        self.read_user_details(user)
        return True

    @refresh_and_retry_on_outdated_tokens
    def update_box_metadata(self, box):
        """
        Update metadata of a :any:`senseBox`

        Args:
            box (senseBox) : the box to update

        Returns:
            True : if the updating went well
        """
        box_json = box.to_json(with_id = True)
        logger.debug("Uploading senseBox metadata:\n{}"
            .format(pretty_json(box_json)))
        response = self.request("put",
            urljoin(self.api,paths.BOXES,box.id),
            headers = self.authorization_header,
            json = box_json,
            )
        response_json = response.json()
        try:
            code = response_json["code"]
            message = response_json.get("message","")
            if code != "Ok":
                raise OpenSenseMapAPIError(
                    "Could not update senseBox with id '{}'{}"
                    .format(box.id, ": {}".format(message) if message else ""))
            data = response_json["data"]
        except KeyError as e:
            raise OpenSenseMapAPIResponseError(
                "Response did not contain {}".format(e))
        # only keep edited boxes, not deleted and new ones
        edited_boxes_ids = set(sensor_json.get("_id") \
            for sensor_json in box_json.get("sensors",[]) \
                if (sensor_json.get("edited") and not sensor_json.get("new"))
            )
        box.sensors = [sensor for sensor in box.sensors \
            if sensor.id in edited_boxes_ids]
        # update the box data
        box.update_from_json(data)

    @refresh_and_retry_on_outdated_tokens
    def new_box(self, box):
        """
        Upload a new :any:`senseBox`

        Args:
            box (senseBox) : the box to upload

        Returns:
            senseBox : the responded new senseBox
        """
        assert box.exposure, "new box needs 'exposure'"
        assert box.current_lat, "new box needs 'current_lat'"
        assert box.current_lon, "new box needs 'current_lon'"
        assert box.name, "new box needs 'name'"
        assert box.sensors, "new box needs at least one sensor"
        box_json = box.to_json(with_id = False)
        logger.debug("Uploading new senseBox:\n{}"
            .format(pretty_json(box_json)))
        response = self.request(
            "post",
            urljoin(self.api, paths.BOXES),
            headers = self.authorization_header,
            json = box_json,
            )
        response_json = response.json()
        try:
            message = response_json.get("message","")
            if not "successfully" in message:
                raise OpenSenseMapAPIError(
                    "Could not post new senseBox{}"
                        .format(": {}".format(message) if message else ""))
            data = response_json["data"]
        except KeyError as e:
            raise OpenSenseMapAPIResponseError(
                "Response did not contain {}".format(e))
        box.update_from_json(data)
        new_box = senseBox.from_json(data)
        logger.debug("new box:\n{}".format(new_box))
        self.get_details()
        return self.get_box(id = new_box.id)

    @refresh_and_retry_on_outdated_tokens
    def delete_box(self, box_id, really = False):
        """
        Mark a senseBox for deletion. This will also delete all the
        measurements. Deletion does not happen immediately. Also calls
        :any:`get_details`.

        Args:
            box_id (str) : the :any:`senseBox.id`
            really (bool, optional): really delete this box? Defaults to
                ``False``.

        Returns:
            True : if the marking for deletion went well
        """
        assert really, \
            "Refusing to delete box '{}' without really=True".format(box_id)
        response = self.request("delete",
            urljoin(self.api,paths.BOXES,box_id),
            headers = self.authorization_header,
            json = {"password": self.password},
            )
        try:
            response_json = response.json()
            code = response_json.get("code","")
            message = response_json.get("message","")
            if re.search("user.+not.+own.+box",message.lower()):
                raise OpenSenseMapAPIPermissionError(
                    message or "User does not own box '{}'".format(box_id))
            if not response.status_code == requests.codes.OK:
                raise OpenSenseMapAPIError(
                    "Could not mark senseBox '{}' for deletion{}"
                    .format(box_id,": {}".format(message) if message else ""))
        except compat.JSONDecodeError:
            raise OpenSenseMapAPIResponseError("Response is not JSON")
        except KeyError as e:
            raise OpenSenseMapAPIResponseError(
                "Response did not contain {}".format(e))
        self.get_details()
        return True

    @refresh_and_retry_on_outdated_tokens
    def upload_current_measurement(self, box, sensor):
        """
        Upload the current measurements of a given sensor of a given senseBox

        Args:
            box_id (str) : the :any:`senseBox.id`
            really (bool, optional): really delete this box? Defaults to
                ``False``.

        Returns:
            True : if the upload went well
        """
        assert box.id, "box has no 'id'"
        assert sensor.id, "sensor has no 'id'"
        response = self.request("post",
            urljoin(self.api,paths.BOXES,box.id,sensor.id),
            headers = self.authorization_header,
            json = {},
            )
        response_json = response.json()
        message = response_json.get("message","")
        if re.search("user.+not.+own.+box",message.lower()):
            raise OpenSenseMapAPIPermissionError(
                message or "User does not own box '{}'".format(box_id))
        if not response.status_code == requests.codes.OK:
            raise OpenSenseMapAPIError(
                "Could not mark senseBox '{}' for deletion{}"
                .format(box_id,": {}".format(message) if message else ""))
        self.get_details()
        return True

    def read_user_details(self, user_details, exception=OpenSenseMapAPIError):
        """
        Read user details into object properties

        Args:
            user_details (dict): the user details as returned by the API
            exception (Exception): the exception to raise if the data is
                ill-formed

        Returns:
            True : if everything is alright

        Raises:
            ``exception`` : if the data is ill-formed
        """
        try:
            email = user_details["email"]
            if email != self.email:
                logger.info("The user's email '{}' is not the same "
                    "as the login email '{}'?!?".format(self.email, email))
            if not user_details["emailIsConfirmed"]:
                logger.warning("The email '{}' is unconfirmed!".format(email))
            self.email = user_details["email"]
            self.name = user_details["name"]
            self.role = user_details["role"]
            self.language = user_details["language"]
            for own_box in self.boxes:
                if not own_box.id in user_details["boxes"]:
                    self.boxes.remove(own_box)
            for box_id in user_details["boxes"]:
                if not box_id in self.boxes.by_id:
                    box = senseBox(id = box_id)
                    self.boxes.append(box)
        except KeyError as e: # pragma: no cover
            raise exception(
                "user information did not contain {}".format(e))
        return True

    @refresh_and_retry_on_outdated_tokens
    def delete_sensor_measurements(self, box_id, sensor_id,
        timestamps = None, from_date = None, to_date = None,
        all = None, really = False):
        """
        Issue a request to delete measurements from a sensor

        Args:
            box_id (str): the senseBox id
            sensor_id (str): the sensor id
            to_date, from_date (datetime.datetime, optional): start and end
                dates to delete the data
            timestamps (list of datetime.datetime, optional): timestamps to
                delete
            all (bool, optional): delete all measurements?
            really (bool, optional): really delete the measurements?

        Returns:
            bool : whether the deletion worked
        """
        assert really, ("Refusing to delete measurements from sensor "
            "'{}' without really=True").format(sensor_id)
        d = {}
        if from_date is not None:
            d.update({"from-date" : date2str(from_date)})
        if to_date is not None:
            d.update({"to-date" : date2str(to_date)})
        if all is not None:
            d.update({"deleteAllMeasurements" : bool(all)})
        if timestamps is not None:
            d.update({"timestamps" : [date2str(x) for x in timestamps]})
        logger.debug("Request payload:\n{}".format(pretty_json(d)))
        response = self.request("delete",
            urljoin(self.api,paths.BOXES,box_id,sensor_id,"measurements"),
            headers = self.authorization_header,
            json = d,
            )
        response_json = response.json()
        message = response_json.get("message","")
        if not response.status_code == requests.codes.OK:
            raise OpenSenseMapAPIError(
                "Could not delete measurements from sensor '{}'"
                    .format(box_id) +
                ": {}".format(message) if message else "")
        return True

    def __del__(self):
        """
        Class deconstructor. Calls :any:`sign_out`.
        """
        self.sign_out()
