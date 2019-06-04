from apps import app
from apps.auth import auth

# 微信登录验证
app.register_blueprint(auth, url_prefix='/auth')