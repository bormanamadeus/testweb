from django.urls import path
from message.views import hello, text, ajax, file, json, stream, streaming, code


urlpatterns = [
    path('code/<int:code>/', code, name='code'),
    path('ajax/', ajax, name='ajax'),
    path('text/', text),
    path('file/', file),
    path('json/', json),
    path('stream/', stream),
    path('streaming/', streaming),
    path('', hello, name='hello'),
]
