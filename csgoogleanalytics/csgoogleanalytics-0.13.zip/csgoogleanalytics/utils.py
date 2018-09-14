import httplib2
from apiclient.discovery import build
from models import CredentialsModel, AnalyticsProfile, Analytics, PageStats, Page
from django.conf import settings

from django.core.paginator import Paginator

URL_VALIDATOR = getattr(settings, 'CSGOOGLEANALYTICS_URL_VALIDATOR', 'csgoogleanalytics.validators.default_validator')

def _load_validator():
    validator = __import__('.'.join(URL_VALIDATOR.split('.')[:-1]))
    for n in URL_VALIDATOR.split('.')[1:]:
        validator = getattr(validator, n)
    return validator

def _build_analytics_service():
    credentialsmodel = CredentialsModel.objects.first()
    credential = credentialsmodel.credential
    http = httplib2.Http()
    http = credential.authorize(http)
    return build('analytics', 'v3', http=http)


def get_most_viewed_urls(max_results=100):
    service = _build_analytics_service()
    profile = AnalyticsProfile.objects.first()
    return service.data().ga().get(
        ids='ga:{}'.format(profile.tracking_code),
        start_date= 'yesterday',
        end_date= 'today',
        metrics='ga:pageviews',
        dimensions='ga:pagePath',
        sort='-ga:pageviews',
        max_results=max_results).execute()

def create_analytics():
    Analytics.objects.all().delete()
    data = get_most_viewed_urls()
    validator = _load_validator()
    for row in data.get('rows', []):
        an= Analytics(path=row[0],
                      title=row[0],
                      pageviews=row[1])
        try:
            is_valid, title, photo_src, content_type, object_id = validator(row[0])
            an.is_valid = is_valid
            an.title = title
            an.photo_src = photo_src
            an.content_type = content_type
            an.object_id = object_id
        except:
            pass
        an.save()


def get_pageviews_from_urls(pagepaths, start_date, end_date):
    """
    https://www.googleapis.com/analytics/v3/data/ga?ids=ga%3A14407&start-date=2017-05-08&end-date=2018-05-08&metrics=ga%3Apageviews&dimensions=ga%3ApagePath&filters=ga%3ApagePath%3D%3D%2Faktualitatea%2F1524904927196%2Cga%3ApagePath%3D%3D%2Faktualitatea%2F1525336600    """
    service = _build_analytics_service()
    profile = AnalyticsProfile.objects.first()
    strpagepaths = ','.join([u'ga:pagePath=={}'.format(a) for a in pagepaths])
    max_results = len(pagepaths)
    return service.data().ga().get(
        ids='ga:{}'.format(profile.tracking_code),
        start_date= start_date,
        end_date= end_date,
        metrics='ga:pageviews',
        dimensions='ga:pagePath',
        filters=strpagepaths,
        sort='-ga:pageviews',
        max_results=max_results).execute()

def create_page_stats(pagepaths_list, start_date_str, end_date_str, period_id):
    """ """
    pager = Paginator(pagepaths_list, 10)
    for i in pager.page_range:
        pagepaths = pager.page(i).object_list
        results = get_pageviews_from_urls(pagepaths,start_date_str,end_date_str)
        for row in results.get('rows',[]):
            page = Page.objects.get(pagepath=row[0])
            PageStats.objects.filter(page=page,period=period_id).delete()
            pstats = PageStats()
            pstats.page = page
            pstats.period = period_id
            pstats.pageviews = row[1]
            pstats.save()

    return True
