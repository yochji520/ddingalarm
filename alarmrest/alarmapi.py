#!/usr/bin/python3
#-*- coding: UTF-8 -*-

from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from urllib.parse import unquote
from alarmrest.dd_robot import dingtalk_robot

@csrf_exempt
@api_view(http_method_names=['post', 'get'])
@permission_classes((permissions.AllowAny,))
def receiverdata(request):
    '''
    :param request:alarm的请求
    :return: 返回发送成功
    '''
    if request.method == 'GET':
        return Response('''Welcome to alarmreset!!!''')
    elif request.method == 'POST':
        str_bytes = request.body
        par_str = unquote(str_bytes.decode(encoding='UTF-8'))
        strlist = par_str.split('&')
        content = strlist[2]
        dingtalk_robot(content)
        return Response("Alarm success!!!")
    else:
        pass