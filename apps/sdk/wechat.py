import requests

# 微信SDK 密匙 和 id
class Choices:
    AppID, AppSecret = '', ''

# 微信SDK auth.code2Session
def WXSDK_jscode2session(code):
    wechat_url = 'https://api.weixin.qq.com/sns/jscode2session'
    wechat_data = {
        'appid': Choices.AppID,
        'secret': Choices.AppSecret,
        'js_code': code,
        'grant_type': 'authorization_code',
    }
    return requests.get(wechat_url, params=wechat_data).json()

# 微信SDK userinfo
def WXSDK_userinfo(openid, access_token):
    wechat_url = 'https://api.weixin.qq.com/sns/userinfo'
    wechat_data = {
        'openid': openid,
        'access_token': access_token,
    }
    result = requests.get(wechat_url, params=wechat_data).encoding = 'UTF-8'
    return result.json()
