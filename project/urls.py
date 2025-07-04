"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from job.sitemaps import JobSitemap

# حط تعريف السايت ماب هنا
sitemaps = {
    'jobs': JobSitemap,
}

urlpatterns = [
    path( 'accounts/', include( 'django.contrib.auth.urls' ) ),
    path( 'accounts/', include( 'accounts.urls', namespace='accounts' ) ),
    path( 'admin/', admin.site.urls ),
    path( '', include( 'job.urls', namespace='jobs' ) ),
    path( '', include( 'contacts.urls', namespace='contacts' ) ),
    path( 'api-auth/', include( 'rest_framework.urls' ) ),

    # هذا هو الصحيح لرابط السايت ماب
    path( 'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap' ),
]

urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )