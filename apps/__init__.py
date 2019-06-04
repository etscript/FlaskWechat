__author__ = 'Ran'

from apps.config import config
from flask import Flask  # flask
from flask_sqlalchemy import SQLAlchemy  # sql

app = Flask(__name__)
db = SQLAlchemy(app)

# 引入全局配置
app.config.from_object(config)

# 跨域密匙
app.secret_key = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

# 创建数据库
# db.create_all()