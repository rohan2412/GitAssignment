from django.conf.urls import include, url
from django.contrib import admin
from git.views import UsersView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/$', UsersView.as_view(template_name='users.html'), name='users'),
]
