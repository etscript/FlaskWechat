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
    username = db.Column(db.String(255))  # username
    avatar = db.Column(db.String(255))  # avatarUrl
    gender = db.Column(db.String(255))  # gender

    country = db.Column(db.String(255))  # country
    province = db.Column(db.String(255))  # province
    city = db.Column(db.String(255))  # city

    # 定义对象
    def __init__(self, openid=None, username=None, avatar=None, gender=None, country=None, province=None, city=None):
        self.openid = openid
        self.username = username
        self.avatar = avatar
        self.gender = gender
        self.country = country
        self.province = province
        self.city = city
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

