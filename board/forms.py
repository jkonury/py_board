from django import forms
from board.models import Entry


class EntryForm(forms.Form):
    class Meta:
        model = Entry
        fields = ('category', 'title', 'content')


class CommentForm(forms.ModelForm):
    model = Entry
    fields = ('title', 'content')

