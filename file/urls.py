from django.conf.urls import url

urlpatterns = [
    url(r'^upload', 'file.views.fileupload', name='fileupload'),
    url(r'^download', 'file.views.filedownload', name='filedownload')
]