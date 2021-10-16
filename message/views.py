from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse, StreamingHttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.template.loader import get_template, render_to_string
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
import csv


def code(request, code):
    r = request.build_absolute_uri(reverse('code', args=(code,)))
    r_lazy = reverse_lazy('ajax')
    print('AJAX: ', r_lazy)

    print('code: ', code)
    print('request.path: ', request.path)
    print('request.path_info: ', request.path_info)
    print('request.get_host(): ', request.get_host())
    print('request.get_port(): ', request.get_port())
    print('request.get_full_path(): ', request.get_full_path())
    print('request.build_absolute_uri(): ', r)
    print('request.META["REMOTE_HOST"]: ', request.META["REMOTE_HOST"])
    print('request.META["QUERY_STRING"]: ', request.META["QUERY_STRING"])
    print('request.META["HTTP_HOST"]: ', request.META["HTTP_HOST"])

    resp = HttpResponse('', content_type='text/html; charset=utf-8')
    resp.write('<h1>Функция reverse. Обратное разрешение адресов URL</h1>')
    resp.write('<p>Адрес: {}</p>'.format(r))
    #print(reverse('hello'), args=5, urlconf='testweb.urls')
    #print(reverse('hello'), args=5)
    if code in range(1, 10):
        return resp
    else:
        return HttpResponseNotFound('Ключ должен быть в пределах 1-10')

def hello(request):
    resp = HttpResponse('', content_type='text/html; charset=utf-8')
    resp.write('<h1>Страница приветствия</h1>')
    resp.write('<p>Hello world!</p>')
    print('request.scheme: ', request.scheme)
    print('request.body: ', request.body)
    print('request.path: ', request.path)
    print('request: ', request)

    print('resp.content: ', resp.content)
    print('resp.charset',resp.charset)

    print('request.get_host: ', request.get_host())
    print('request: ', request)

    return resp


def text(request):
    elements = {'job': 'Фитнес-тренет', 'home': 'ул.Савушкина'}
    context = {'elements': elements}

    print('is_secure(): ', request.is_secure())
    print('is_ajax(): ', request.is_ajax())


    #1.
    #template = get_template('message/index.html')
    #print('type(template): ', type(template))
    #print('template: ', template)
    #return HttpResponse(template.render(context=context, request=request))
    #return HttpResponse(template.render(context, request))

    #2.
    #return HttpResponse(render_to_string('message/index.html', context, request))

    #3.
    return TemplateResponse(request, 'message/index.html', context)

def ajax(request):
    #print(request.META["HTTP_X_REQUESTED_WITH"])
    print('AJAX request.body: ', request.body)
    
    text = 'no {} in system!'
    resp = HttpResponse('', content_type='text/html; charset=utf-8')
    resp.write(text)

    return resp

def file(request):
    filename = r'C:\Home\project\python\testweb\message\static\message\bg.jpg'
    #filename = r'C:\Home\project\python\testweb\message\static\message\style.css'

    # Файл откроется в браузере
    #return FileResponse(open(filename, 'rb'))

    return FileResponse(open(filename, 'rb'), as_attachment=True)

def json(request):
    data = {'title': 'Car', 'content': 'Old'}

    return JsonResponse(data)

def stream(request):
    #resp_content = ('Main ', 'site  ', 'page ', 'will be ', 'hear.')
    resp_content = ['<p>{}</p>'.format(x) for x in range(500)]
    resp = StreamingHttpResponse(resp_content, content_type='text/html; charset=utf-8')
    resp['keywords'] = 'Python, Django'

    return resp

class Echo:

    def write():
        return 'message/static/message/adresses.csv'

def streaming(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    pseudo_buffer = 'hello man how are you' 
    writer = csv.writer(Echo())
    response = StreamingHttpResponse((writer.writerow(row) for row in rows), 
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return response

