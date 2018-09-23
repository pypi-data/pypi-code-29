from blog.models import Tag, Blog

def hexia_blog (request):
    return {
        'hexia_blog_tags' : Tag.objects.all(),
        'hexia_blog_recent_posts' : Blog.objects.live_blogs().order_by('-date')[:5]
        }