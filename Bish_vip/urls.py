from django.conf.urls import url
from django.conf.urls.static import static

from accaunts.views import (login_view, register_view, logout_view, profile_view)
from untitled import settings
from . import views

app_name = 'Bish_vip'
urlpatterns = [
    # url(r'^/', views.post_home, name="list"),
    url(r'^$', views.post_home, name="list"),
    url(r'^create/', views.post_create, name="create"),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^kattaluu/$', register_view, name='kattaluu'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^sort_by_price/$', views.post_sort, name='sort'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
