from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from board.views import EntryCreate, EntryList, EntryDetail, CommentList, CommentCreate, EntryUpdate, EntryDelete

urlpatterns = [
    # url(r'^sign_in', 'account.views.sign_in'),
    # url(r'^sign_up', 'account.views.sign_up'),
    # url(r'^(?P<board_name>[\w-]+)/add/$', EntryCreate.as_view(), name='entry-add'),
    # url(r'^name', 'board.views.name'),
    # url(r'^contract', 'board.views.contract'),

    url(r'^(?P<pk>[0-9]+)/$', EntryDetail.as_view(), name='entry-detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', EntryUpdate.as_view(), name='entry-update'),

    url(r'^(?P<pk>[0-9]+)/delete$', EntryDelete.as_view(), name='entry-delete'),
    url(r'^(?P<board_name>[a-zA-Z]+)/$', EntryList.as_view(), name='entry-list'),
    url(r'^(?P<board_name>[a-zA-Z]+)/add', login_required(EntryCreate.as_view()), name='entry-add'),
    url(r'^(?P<pk>[0-9]+)/$', EntryDetail.as_view(), name='entry-detail'),

    url(r'^(?P<pk>[0-9]+)/comment/$', CommentList.as_view(), name='comment-list'),
    url(r'^(?P<pk>[0-9]+)/comment/add$', CommentCreate.as_view(), name='comment-add'),
    ]

