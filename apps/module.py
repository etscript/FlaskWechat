# -*- coding: utf-8 -*-
from apps import db

'''登录状态表'''
class LoginSessionCache(db.Model):
    __tablename__ = 'login_session_cache'

    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(255))  # openid
    session_key = db.Column(db.String(255))  # token

    # 定义对象
    def __init__(self, openid=None, session_key=None):
        self.openid = openid
        self.session_key = session_key
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

'''用户数据表'''
class Userdata(db.Model):
    __tablename__ = 'userdata'

    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(255))  # openid

    # 定义对象
    def __init__(self, openid=None):
        self.openid = openid
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

