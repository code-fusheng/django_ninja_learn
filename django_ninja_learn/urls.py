"""django_ninja_learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""

"""

from django.contrib import admin, auth
from django.urls import path
# 导入 NinjaAPI
from ninja import NinjaAPI, Schema
from user_app.models import SysUser
from ninja_extra import NinjaExtraAPI, api_controller, http_get, route
from ninja_jwt.controller import NinjaJWTDefaultController
from django.contrib.auth import authenticate

api = NinjaExtraAPI()

api.auto_discover_controllers()

api.register_controllers(NinjaJWTDefaultController)

class LoginIn(Schema):
    username: str
    password: str


@api.post("/login", auth=None)
def login(request, payload: LoginIn):
    """用户登录"""
    user = auth.authenticate(username=payload.username, password=payload.password)
    if user is not None:
        return {"code": 200, "msg": user.id}
    else:
        return {"code": -1, "msg": "xxx"}


urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置公共基础路由
    path('api/', api.urls),
    # 框架路由
]
