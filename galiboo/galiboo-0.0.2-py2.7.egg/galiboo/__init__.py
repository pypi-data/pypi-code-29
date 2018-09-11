# -*- coding: utf-8 -*-
import requests
from requests.exceptions import HTTPError


class Galiboo(object):

    def __init__(self, api_key):
        self.url = "http://secure.galiboo.com/api"
        self.session = requests.Session()
        self.session.params["token"] = api_key

    @property
    def artist(self):
        """Proxy :class:`Artist` class
        """
        return Artist(connection=self)

    @property
    def track(self):
        """Proxy :class:`Track` class
        """
        return Track(connection=self)

    @property
    def user(self):
        """Proxy :class:`User` class
        """
        return User(connection=self)

    @property
    def user_event(self):
        """Proxy :class:`UserEvent` class
        """
        return UserEvent(connection=self)

    @property
    def job(self):
        """Proxy :class:`Job` class
        """
        return Job(connection=self)


class Resource(object):

    def __init__(self, connection):
        self._connection = connection

    @property
    def session(self):
        return self._connection.session

    @property
    def base_url(self):
        return self._connection.url

    def _raise_or_return_json(self, response):
        """Raise HTTPError before converting response to json

        :param response: Request response object
        """
        try:
            response.raise_for_status()
        except HTTPError:
            raise

        try:
            json_value = response.json()
        except ValueError:
            return response.content
        else:
            return json_value


class Artist(Resource):

    def metadata(self, artist_id):
        """Retreives the metadata for the given artist.

        :param artist_id: Artist id
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "metadata/artists/%s" % artist_id),
        )
        return self._raise_or_return_json(resp)

    def get(self, artist, limit=10, page=1):
        """Searches our index for artists that match your search criteria.
        This can be useful for retrieving the ids of artists by their name,
        for example, which can then be used for the other API endpoints.

        :param artist: The name of the artist
        :param limit: The maximum number of search results to return
        :param page: The page of the search result to return
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "metadata/artists/search/"),
            params={
                "artist": artist,
                "limit": limit,
                "page": page
            }
        )
        return self._raise_or_return_json(resp)


class Track(Resource):

    def metadata(self, track_id):
        """Retreives the emotions and other important metadata
        (energy, danceability, etc.) for the given track.

        :param track_id: Track id
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "metadata/tracks/%s" % track_id),
        )
        return self._raise_or_return_json(resp)

    def get(self, track=None, artist=None, limit=10, page=1):
        """Searches our index for tracks that match your search criteria.
        This can be useful for retrieving the ids of tracks by their name,
        for example, which can then be used for the other API endpoints
        (e.g. recommendations, finding similar tracks, etc).

        :param track: The title of the track
        :param artist: The name of the artist
        :param limit: The maximum number of search results to return
        :param page: The # of the page in the search result to return
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "metadata/tracks/search/"),
            params={
                "track": track,
                "artist": artist,
                "limit": limit,
                "page": page
            }
        )
        return self._raise_or_return_json(resp)

    def smart_search(self, q, count=10, page=1):
        """Search for music with natural language queries, & our music A.I.
        will return the relevant music tracks within seconds, automagically.
        This endpoint searches for tracks that are relevant to the given natural language query.
        Since our A.I. understands music like humans, it's able to search for tracks
        based on their audio, without using their titles, manually-curated tags, etc.

        :param q: The natural language search query
        :param count: The maximum number of tracks to return per page
        :param page: The page of results to return
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "discover/tracks/smart_search/"),
            params={
                "q": q,
                "count": count,
                "page": page
            }
        )
        return self._raise_or_return_json(resp)

    def search_by_tags(self, tags_query, limit=10, page=1):
        """Finds tracks that are musically close to the tag values that you specify.
        This can come in handy for many different tasks, such as curating a
        special playlist with specific types of tracks (ie. mellow, relaxing songs), for example

        :param tags_query: JSON tag query

            Eg. {
                "energy" : 0.2,
                "smart_tags" : {
                    "Emotion-Calming_/_Soothing" : 0.9
                }
                # ... add any other tags/search criteria that you'd like!
            }

        :param limit: The maximum number of tracks to return per page
        :param page: The page of results to return
        """
        resp = self.session.post(
            url="%s/%s" % (self.base_url, "discover/tracks/find/"),
            params={
                "limit": limit,
                "page": page
            },
            json=tags_query
        )
        return self._raise_or_return_json(resp)

    def search_by_similar(self, track_id, count=15):
        """Finds tracks in the catalog that are musically similar to the specified track,
        as felt by humans. This could be especially useful in a radio session,
        for example, when a user would prefer to listen to a stream of songs that sound similar.

        :param track_id: Track id
        :param count: The number of similar tracks to search for
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "discover/tracks/%s/similar/" % track_id),
            params={
                "count": count,
            }
        )
        return self._raise_or_return_json(resp)

    def analyze(self, url):
        """Schedule a background job in our cloud to analyze the audio file at the given URL.
        Please note that, unlike our AI Analyzer API, the analysis will not be done
        within the cycle of the HTTP request. Rather, it will be batch processed
        in the background, and you can track the job's status using the job ID
        returned by this endpoint and the Job Status API endpoint below.

        :param url: The URL of the audio file to analyze (must be publicly accessible)
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "integration/tracks/analyze/"),
            params={"url": url}
        )
        return self._raise_or_return_json(resp)

    def ai_analyze(self, url):
        """Enables you to analyze a music audio file given its URL,
        using our A.I. music-understanding technology

        :param url: The URL of the audio file to analyze
        """
        if "youtube" in url:
            req_url = "%s/%s" % (self.base_url, "analyzer/analyze_youtube/")
        else:
            req_url = "%s/%s" % (self.base_url, "analyzer/analyze_url/")

        resp = self.session.get(
            url=req_url,
            params={"url": url}
        )
        return self._raise_or_return_json(resp)


class User(Resource):

    def create(self, _id):
        """Enables you to add your service's users in our backend,
        in order to make use of our powerful personalization features for them.

        :param _id: The unique id of the user as saved in your service (as a string)
        """
        resp = self.session.post(
            url="%s/%s" % (self.base_url, "personalization/users/new/"),
            json={
                "_id": _id,
            }
        )
        return self._raise_or_return_json(resp)

    def get(self, user_id):
        """Enables you to retrieve a user in your service, stored in our backend.

        :param user_id: User id
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "personalization/users/%s" % user_id)
        )
        return self._raise_or_return_json(resp)

    def get_recommended_tracks(self, user_id):
        """Enables you to get music recommendations for a user in real-time,
        using our AI-powered personalization technology.

        :param user_id: User id
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "personalization/users/%s/recommend_tracks/" % user_id)
        )
        return self._raise_or_return_json(resp)


class UserEvent(Resource):

    def create(self, user_id, event):
        """Allows you to notify our live A.I. recommendation engine of user events
        (such as listens, skips, etc.) as they happen, enabling our technology
        to instantly adapt and provide smarter recommendations automagically, with no delay

        :param user_id: User id
        :param event: Event json
            Eg. {
                'timestamp' : datetime.datetime.utcnow().isoformat(),
                'type' : 'listen',
                'object' : {
                    'type' : 'track',
                    'id' : sample_track_id
                }
            }
        """
        resp = self.session.post(
            url="%s/%s" % (self.base_url, "personalization/users/%s/events/new" % user_id),
            json=event
        )
        return self._raise_or_return_json(resp)

    def get(self, user_id):
        """Enables you to retrieve the events for a specific user in your service,
        stored in our backend.

        :param user_id: User id
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "personalization/users/%s/events/" % user_id)
        )
        return self._raise_or_return_json(resp)


class Job(Resource):

    def get(self, job_id):
        """Enables you to monitor the status of a music analysis job that
        you scheduled using our Batch Integration API.

        :param job_id: The job ID returned by the previous API endpoint
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "integration/jobs/%s" % job_id)
        )
        return self._raise_or_return_json(resp)

    def all(self, show_progress=False, page=1):
        """Enables you to get a list of all the music analysis jobs
        that you've scheduled using our Batch Integration API.

        :param show_progress: Whether to return some stats about the overall
        progress of all the music analysis jobs that you've submitted.
        :param page: The page of the results to return
        """
        resp = self.session.get(
            url="%s/%s" % (self.base_url, "integration/jobs"),
            params={
                "show_progress": show_progress,
                "page": page
            }
        )
        return self._raise_or_return_json(resp)
