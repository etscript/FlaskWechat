__author__ = 'Ran'
from apps.auth import service
from ..auth import auth
from apps.components.common import returnData
from apps.components.middleware import requestPOST

'''登录接口'''
@auth.route('/sgin', methods=["GET","POST"])
@requestPOST
def login(request):
    code, msg, json = service.login(request)
    return returnData(code, msg, json)