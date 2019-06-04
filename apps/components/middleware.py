from flask import request
from functools import wraps

from apps.components.common import returnData
from apps.module import LoginSessionCache, Userdata

# 登录验证
def SingAuth(func=None):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':

            #检验参数

            '''获取openid和token 如果不存在返回None'''
            openid, session_key = request.json.get("openid"), request.json.get("token")

            '''判断是否存在None的jsonkey'''
            if openid == None or session_key == None:
                return returnData(400, '参数缺失', '')

            '''判断两个key的值是否为空'''
            if request.json['openid'] == '' or request.json['session_key'] == '':
                return returnData(400, '参数缺失', '')

            else:

                '''获取openid 和 token 一致的记录'''
                if LoginSessionCache.query.filter_by(openid=openid, session_key=session_key).first():

                    '''查询该用户的openid'''
                    if Userdata.query.filter_by(openid=openid).first():
                        return func(request, *args, **kwargs)

                    else:
                        return returnData(403, '未授权', '')

                else:
                    return returnData(401, '未登录', '')

        else:
            '''禁止get请求'''
            return returnData(404, '请求方式不正确', '')

    return wrapper

# POST
def requestPOST(func=None):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            return func(request, *args, **kwargs)
        else:
            return returnData(404, '请求方式不正确', '')
    return wrapper

# GET
def requestGET(func=None):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            return func(request, *args, **kwargs)
        else:
            return returnData(404, '该接口不支持POST方式请求', '')
    return wrapper