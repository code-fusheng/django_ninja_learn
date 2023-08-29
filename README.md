# django + ninja 工程模版

### 必要依赖
```shell
pip install django
pip install django-ninja
pip install django-ninja-extra
pip install django-ninja-jwt

```

### 工程指令
```shell
# 创建应用
python manage.py startapp api
python manage.py makemigrations
python manage.py migrate

# 创建管理员
python manage.py createsuperuser
# admin 123456

pip freeze > requirements.txt
pip install -r requirements.txt

```


### 插件推荐
Key Promoter X : 快捷键助手


```angular2html
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
```
