import requests

# 微信SDK 密匙 和 id
class Choices:
    AppID, AppSecret = 'wxca92f0b93dba223a', 'e4d42b1c898197d84d5de372900695e0'

# 微信SDK auth.code2Session
def WXSDK_GetUserToken(code):

    '''SDK请求地址'''
    wechat_url = 'https://api.weixin.qq.com/sns/jscode2session'

    '''请求参数'''
    wechat_data = {
        'appid': Choices.AppID,
        'secret': Choices.AppSecret,
        'js_code': code,
        'grant_type': 'authorization_code',
    }

    '''返回 400=请求不成功'''
    try:
        requests.get(wechat_url, params=wechat_data).json()
    except:
        return 400