from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from board.forms import EntryForm
from board.models import Board, Entry, Category


class BoardMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BoardMixin, self).get_context_data(**kwargs)

        board_name = self.kwargs.get('board_name', None)
        if board_name:
            context['board'] = get_object_or_404(Board, name=board_name)
        else:
            context['board'] = self.object.board
        return context


class EntryList(BoardMixin, ListView):
    model = Entry
    context_object_name = 'entry_list'
    template_name = 'board/list.html'
    paginate_by = 5
    # ordering = 'created_date'

    def get_queryset(self):
        board_name = self.kwargs.get('board_name', None)
        board = get_object_or_404(Board, name=board_name)
        return Entry.objects.filter(board=board, parent=None).order_by('-created_date')


class EntryCreate(BoardMixin, CreateView):
    model = Entry
    template_name = 'board/save.html'
    # form_class = EntryForm

    fields = ['title', 'category', 'content']

    def get_context_data(self, **kwargs):
        context = super(EntryCreate, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    # def get(self, request, *args, **kwargs):
    #     if not self.request.user.id:
    #         return redirect(reverse('account_login'))
    #     return super(EntryCreate, self).get(self, request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.board = self.get_context_data()['board']
        return super(EntryCreate, self).form_valid(form)

    def get_success_url(self):
        return self.object.board.get_absolute_url()


class EntryDetail(DetailView):
    model = Entry
    template_name = 'board/detail.html'

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk', None)
    #     print(pk)
    #     # board = get_object_or_404(Board, pk=pk)
    #     return Entry.objects.get(int(pk))

    def get_context_data(self, **kwargs):
        context = super(EntryDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', None)
        context['object_list'] = Entry.objects.filter(parent=pk)
        return context


class EntryUpdate(BoardMixin, UpdateView):
    model = Entry
    # form_class = EntryForm
    fields = ['title', 'category', 'content']
    template_name = 'board/save.html'

    def get_context_data(self, **kwargs):
        context = super(EntryUpdate, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def form_valid(self, form):
        return super(EntryUpdate, self).form_valid(form)


class EntryDelete(BoardMixin, DeleteView):
    model = Entry

    def get_success_url(self):
        return reverse_lazy('entry-list', self.object.board.name)


class CommentList(ListView):
    model = Entry
    paginate_by = 5
    template_name = 'board/comment_list.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        return Entry.objects.filter(parent=pk)


class CommentCreate(CreateView):
    model = Entry
    fields = ('title', 'content')
    template_name = 'board/comment_save.html'

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', None)
        context['object'] = get_object_or_404(Entry, id=pk)
        context['board'] = context['object'].board
        return context

    def form_valid(self, form):
        pk = self.kwargs.get('pk', None)
        parent = get_object_or_404(Entry, id=pk)
        form.instance.user = self.request.user
        form.instance.board = parent.board
        form.instance.parent = parent
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        return self.object.parent.get_absolute_url()


def send_mail():
    from django.core.mail import send_mail
    send_mail('test', 'hello world', 'yahoojjnag@gmail.com', ['yahoojjnag@gmail.com'], fail_silently=True)
