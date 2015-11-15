import urllib.parse
import mimetypes
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDict
from file.models import File
# from jsonview.decorators import json_view
from py_board import settings


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def fileupload1(request):
    return HttpResponse('<script>alert("이미지 파일이 아닙니다.")</script>')


def fileupload(request):
    if request.method == 'POST':
        f = request.FILES['files']

        file = File(file=f, name=f, size=len(f), user_id=request.user.id,
                    ip=get_client_ip(request))

        print(request.user.id)

        # file = File(file=request.FILES['files'])
        # request.FILES.getlist('files')
        # print(f)
        # print(len(f))
        # files = request.FILES
        # print(files)
        # print(files.getlist('files'))

        file.save()

        d = File.objects.last()
        # render
        # "<script>parent.$.imageUploaded('${grailsApplication.config.grails.fileURL}/images/${mil}${ext}');</script>"
        return HttpResponse(
            "<script>parent.$.imageUploaded('/media/" + str(d.file) + "');</script>")
    else:
        return HttpResponse('<script>alert("A")</script>')


def filedownload(request):
    filename = '스크린샷_2015-04-16_204733.png'
    filename = '테스트.pdf'
    filepath = settings.MEDIA_ROOT + '/documents/2015/04/16/' + filename
    with open(filepath, 'rb') as f:
        response = HttpResponse(f.read())

    content_type, encoding = mimetypes.guess_type(filepath)
    if content_type is None:
        content_type = 'application/octet-stream'

    response['Content-Type'] = content_type
    response['Content-Length'] = os.path.getsize(filepath)

    if 'Webkit' in request.META.get('HTTP_USER_AGENT', 'Webkit'):
        header = 'filename=%s' % filename.encode('utf-8')
    elif 'MSIE' in request.META.get('HTTP_USER_AGENT', 'MSIE'):
        # header = 'filename=%s' % filename.encode('utf-8')
        header = 'filename*=UTF-8\'\'%s' % urllib.parse.quote(filename.encode('utf-8'))
    else:
        header = 'filename*=UTF-8\'\'%s' % urllib.parse.quote(filename.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + header
    # response['Content-Disposition'] = 'attachment; filename=%s' % filename.encode('utf-8')
    print('attachment; ' + header)
    print('attachment; filename=%s' % filename.encode('utf-8'))

    return response


'''
response = HttpResponse(mimetype='application/force-download')
response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
response['X-Sendfile'] = smart_str(path_to_file)
# It's usually a good idea to set the 'Content-Length' header too.
# You can also set any other required headers: Cache-Control, etc.
return response

response = HttpResponse(wrapper, mimetype='application/octet-stream')
response['Content-Disposition'] = 'attachment; filename=' + '파일이름'
response['Content-Length'] = os.path.getsize(filename)

return response
'''
