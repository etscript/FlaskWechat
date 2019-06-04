from sdk.wechat import WXSDK_GetUserToken

from apps.module import LoginSessionCache

'''
    微信小程序登录流程
    
    1.前端:
    1.通过wx.login()获取code
    2.通过wx.request()发送一个post请求给后端并把code传至后端
    
    2.后端:
    1.appid + appsecret + code 这三个参数传递至微信 获取用户session_key 与 openid
    
    3.登录:
    1.把openid 和 session_key 储存进数据库
    2.返回登录成功 并携带数据
    3.前端储存成功登录的数据
    
    4.验证登录:
    1.每次需要判断用户是否已经登录的功能时 需要携带请求的用户的openid 与 session_key
    2.如果存在对应的记录则为合法(自有数据库)

'''

def login(request):

    '''获取前端传回来的code 并判断是否存在 如不存在则返回400'''
    code = request.json.get('code')
    if code == None:
        return 400, '参数不存在', ''

    else:
        '''获取用户的openid 和 session_key'''
        wechet_data = WXSDK_GetUserToken(request.json['code'])
        openid, session_key = wechet_data['openid'], wechet_data['session_key']

        '''登录逻辑(更新和新建)'''
        if LoginSessionCache.query.filter_by(openid=openid).first():

            '''存在就更新session_key'''
            db.session.query(LoginSessionCache).filter(LoginSessionCache.openid == openid).update({LoginSessionCache.session_key: session_key})
            return 200, '成功', {"openid": openid,"session_key":session_key}

        else:

            '''不存在就创建用户'''
            LoginSessionCache(openid , session_key)
            return 200, '成功', {"openid": openid,"session_key":session_key}