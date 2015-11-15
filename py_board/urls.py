from django.conf.urls import include, url
from django.contrib import admin
from py_board.views import HomeView
from django.conf import settings
from django.conf.urls.static import static
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'py_board.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^404', Http404View.as_view, name='404'),

    # url(r'^account/', include('account.urls')),
    url(r'^board/', include('board.urls')),
    url(r'^file/', include('file.urls')),


    url(r'^accounts/', include('allauth.urls')),
    # url(r'^accounts/profile/', )


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
