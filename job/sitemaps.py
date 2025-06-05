from django.contrib.sitemaps import Sitemap
from .models import Job

class JobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Job.objects.all()

    def location(self, obj):
        return f'/{obj.slug}/'

    def lastmod(self, obj):
        return obj.date_at
