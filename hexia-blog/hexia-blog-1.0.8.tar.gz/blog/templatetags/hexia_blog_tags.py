import datetime

from django import template

from blog.models import Blog

register = template.Library()
    
@register.filter
def month_count(month, year):
    start_date = datetime.date(year,month,1)
    if month == 12:
        year += 1
        month = 1
    else : month += 1
    end_date = datetime.date(year,month,1)
    return Blog.objects.live_blogs().filter(date__gte=start_date, date__lt=end_date).count()
    