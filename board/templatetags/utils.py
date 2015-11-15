import hashlib
from django.forms import FileField
from django.template import Library
from django_gravatar.helpers import get_gravatar_url

register = Library()


@register.filter
def get_range(value):
    return range(1, value+1)


@register.filter()
def get_hash(value):
    return hashlib.md5(value.encode()).hexdigest()


@register.tag()
def get_gravatar(email):
    return get_gravatar_url(email=email, size=40, default='identicon', rating='r')


# get_gravatar_url(email, size=GRAVATAR_DEFAULT_SIZE, default=GRAVATAR_DEFAULT_IMAGE,
#     rating=GRAVATAR_DEFAULT_RATING, secure=GRAVATAR_DEFAULT_SECURE):

@register.filter()
def field_value(value):
    if value:
        return value
    else:
        return ''

# @register.filter(name='field_value')
# def field_value(field):
#     """
#     Returns the value for this BoundField, as rendered in widgets.
#     """
#     if not field.form.is_bound:
#         val = field.form.initial.get(field.name, field.field.initial)
#         if callable(val):
#             val = val()
#     else:
#         if isinstance(field.field, FileField) and field.data is None:
#             val = field.form.initial.get(field.name, field.field.initial)
#         else:
#             val = field.data
#     if val is None:
#         val = ''
#     return val
