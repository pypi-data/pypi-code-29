import base64
import os

import flask
import flask_oauthlib.client
from google.cloud import datastore


def retrieve_config_value(key: str) -> str:
    datastore_client = datastore.Client()
    return datastore_client.get(datastore_client.key("Config", key))["value"]


BLIZZARD_CLIENT_KEY = (os.getenv("BLIZZARD_CLIENT_KEY", "")
                       or retrieve_config_value("redirectAppBlizzardClientKey"))
BLIZZARD_CLIENT_SECRET = (os.getenv("BLIZZARD_CLIENT_SECRET", "")
                          or retrieve_config_value("redirectAppBlizzardClientSecret"))

app = flask.Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "") or retrieve_config_value("secretKey")

oauth = flask_oauthlib.client.OAuth(app)


def blizzard_oauth(region: str) -> flask_oauthlib.client.OAuthRemoteApp:
    return oauth.remote_app(
        "blizzard_{}".format(region),
        request_token_params={"scope": "sc2.profile"},
        consumer_key=BLIZZARD_CLIENT_KEY,
        consumer_secret=BLIZZARD_CLIENT_SECRET,
        base_url="https://{}.api.battle.net/".format(region),
        authorize_url="https://{}.battle.net/oauth/authorize".format(region),
        access_token_url="https://{}.battle.net/oauth/token".format(region),
        access_token_method='POST',
        access_token_headers={
            "User-Agent":
                "Mozilla/5.0",
            "Authorization":
                "Basic " + base64.b64encode("{}:{}".format(
                    BLIZZARD_CLIENT_KEY, BLIZZARD_CLIENT_SECRET).encode()).decode()
        },
        access_token_params={"scope": "sc2.profile"},
    )


blizzard_eu = blizzard_oauth("eu")
blizzard_us = blizzard_oauth("us")
blizzard_kr = blizzard_oauth("kr")


@app.route("/")
def index():
    return blizzard_us.authorize(
        callback=flask.url_for(blizzard_authorised.__name__, _external=True, _scheme="https"))


@app.route("/blizzard-authorised")
def blizzard_authorised():
    """This is the endpoint for the oauth2 callback for the Blizzard API"""

    blizzard_resp_data = blizzard_us.authorized_response()
    if not blizzard_resp_data or "access_token" not in blizzard_resp_data is None:
        return "Login failed", 401

    blizzard_access_token = blizzard_resp_data["access_token"]

    def extract_character_data(region: str, character: dict):
        return {
            "seasonId": character.get("season", {}).get("seasonId", 0),
            "profile_path": "http://{}.battle.net/sc2/en{}".format(region, character.get("profilePath", "/")),
            "totalGamesThisSeason": character.get("season", {}).get("totalGamesThisSeason", 0),
        }

    characters = []

    eu_profile_resp = blizzard_eu.get("sc2/profile/user", token=blizzard_access_token)
    if eu_profile_resp.status == 200 and eu_profile_resp.data:
        eu_profile_data = eu_profile_resp.data
        characters.extend([
            extract_character_data("eu", character)
            for character in eu_profile_data.get("characters", [])
        ])

    us_profile_resp = blizzard_us.get("sc2/profile/user", token=blizzard_access_token)
    if us_profile_resp.status == 200 and us_profile_resp.data:
        characters.extend([
            extract_character_data("us", character)
            for character in us_profile_resp.data.get("characters", [])
        ])

    kr_profile_resp = blizzard_kr.get("sc2/profile/user", token=blizzard_access_token)
    if kr_profile_resp.status == 200 and kr_profile_resp.data:
        characters.extend([
            extract_character_data("kr", character)
            for character in kr_profile_resp.data.get("characters", [])
        ])

    if not characters:
        return "Could not find sc2 profile for account", 404

    sorted_characters = sorted(characters, key=lambda x: (x["seasonId"], x["totalGamesThisSeason"]), reverse=True)
    primary_character = next(iter(sorted_characters))

    return flask.redirect(primary_character["profile_path"])
