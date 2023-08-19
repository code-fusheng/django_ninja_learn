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

from django.contrib import admin
from django.urls import path
# 导入 NinjaAPI
from ninja import NinjaAPI, Schema

api = NinjaAPI()

# API DOCS http://127.0.0.1:8000/api/docs

# http://127.0.0.1:8000/api/test?a=1&b=2
@api.get("/test")
def test(request, a: int, b: int):
    return {"result": a + b}

# http://127.0.0.1:8000/api/hello?name=code-fusheng
@api.get("/hello")
def hello(request, name):
    return f"Hello Django & Ninja & {name}"

@api.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"result": a + b}

class HelloSchema(Schema):
    name: str = "world"

@api.post("/test/post")
def test_post(request, body: HelloSchema):
    return f"Hello {body.name}"

from user_app.schemas import EmployeeCreate
from user_app.models import Employee

@api.post("/employee/create")
def create_employee(request, payload: EmployeeCreate):
    new_employee = Employee.objects.create(**payload.dict())
    return {"id": new_employee.id}

# 处理文件上传
from ninja import UploadedFile, File
from django.core.files.storage import FileSystemStorage

STORAGE = FileSystemStorage()

@api.post("/upload")
def create_upload(request, cv: UploadedFile = File(...)):
    filename = STORAGE.save(cv.name, cv)
    print(filename)
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置公共基础路由
    path('api/', api.urls),
]
