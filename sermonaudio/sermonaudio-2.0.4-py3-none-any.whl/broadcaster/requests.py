import datetime
import functools
from http import HTTPStatus

from posixpath import join as posixjoin
from typing import Optional, List

from sermonaudio import API, APIException, _session
from sermonaudio.models import Sermon, SermonEventType
from sermonaudio.utils import update_kwargs_for_key


class BroadcasterAPIError(APIException):  # pragma: no cover
    pass


def parse_sermon(response) -> Sermon:  # pragma: no cover
    if response.ok:
        return Sermon.parse(response.json())
    else:
        raise BroadcasterAPIError(response.json())


class Broadcaster(API):  # pragma: no cover. Unfortunately we can't test this w/o a test account...
    @classmethod
    def create_or_update_sermon(cls,
                                sermon_id: Optional[str],
                                accept_copyright: bool,
                                full_title: str,
                                speaker_name: str,
                                preach_date: datetime.date,
                                publish_date: Optional[datetime.date],
                                event_type: SermonEventType,
                                display_title: Optional[str],
                                subtitle: Optional[str],
                                bible_text: Optional[str],  # TODO: structure this data
                                more_info_text: Optional[str],
                                language_code: str,
                                keywords: Optional[List[str]],
                                **kwargs) -> Sermon:
        """Creates a new sermon record or updates an existing one (media uploaded separately).

        :param sermon_id: The sermon ID, if you are updating an existing sermon. Otherwise, None.
        :param accept_copyright: A boolean value indicating that you agree that you are allowed to upload this content.
        :param full_title: The full sermon title.
        :param speaker_name: The speaker name (please be consistent; speakers will be created if they don't exist).
        :param preach_date: The date the sermon was preached.
        :param publish_date: The date that the sermon should be visible on the site. You must submit this in order
        for the sermon to be visible to the public. Regrettably, we US Eastern time rather than UTC for
        historical reasons.
        :param event_type: The type of event that this sermon was preached at.
        :param display_title: An alternate, shorter version of the title to be displayed in ID3v1 tags and parts of
        the legacy site (30 char limit)
        :param subtitle: The subtitle of the sermon (or the series, if multiple sermons use the same subtitle; this
        will likely be reworked in the future)
        :param bible_text: The scripture passage(s) that this sermon was derived from
        :param more_info_text: Additional info about the sermon that you wish to share
        :param language_code: The ISO 639 language code for the sermon.
        :param keywords: A list of keywords for this sermon.
        :param kwargs: Additional arguments to pass to the underlying get method.
        :return: The created sermon
        """
        update_kwargs_for_key(kwargs, 'params', {
            'acceptCopyright': accept_copyright,
            'fullTitle': full_title,
            'speakerName': speaker_name,
            'preachDate': preach_date.isoformat(),
            'publishDate': publish_date.isoformat() if publish_date else None,
            'eventType': event_type.value,
            'displayTitle': display_title,
            'subtitle': subtitle,
            'bibleText': bible_text,
            'moreInfoText': more_info_text,
            'languageCode': language_code,
            'keywords': ' '.join(keywords) if keywords else None,
        })

        if sermon_id:
            path = posixjoin('node', 'sermons', sermon_id)
            method = 'put'
        else:
            path = posixjoin('node', 'sermons')
            method = 'post'

        return cls._request(path,
                            method,
                            parse_func=parse_sermon,
                            **kwargs)

    @classmethod
    def delete_sermon(cls, sermon_id: str):  # pragma: no cover
        path = posixjoin('node', 'sermons', sermon_id)
        return cls.delete(path)

    @classmethod
    def _upload_media(cls,
                      upload_type: str,
                      sermon_id: str,
                      path: str,
                      **kwargs):  # pragma: no cover
        """Uploads media for a sermon.
        :param upload_type: The type of media to upload.
        :param sermon_id: The Sermon ID you are uploading media for.
        :param path: The path to the file on disk.
        :param kwargs: Additional arguments to pass to the underlying post method.
        :return: No return value. Throws a BroadcasterAPIError with details on failure.
        """
        update_kwargs_for_key(kwargs, 'params', {
            'uploadType': upload_type,
            'sermonID': sermon_id,
        })

        response = cls.post('media', **kwargs)

        if response.status_code != HTTPStatus.CREATED:
            raise BroadcasterAPIError({
                'error': 'Unable to create media upload',
                'json': response.json(),
            })

        upload_url = response.json()['uploadURL']

        with open(path, 'rb') as fp:
            response = _session.post(upload_url,
                                     data=fp,
                                     stream=True)
            if not response.ok:
                raise BroadcasterAPIError({
                    'error': f'Received unexpected HTTP status code {response.status_code} when uploading data.',
                    'response': response.content
                })

    upload_audio = functools.partialmethod(_upload_media, 'original-audio')
    upload_video = functools.partialmethod(_upload_media, 'original-video')
