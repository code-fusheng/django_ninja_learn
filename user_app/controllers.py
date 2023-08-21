from typing import List
from ninja_extra import NinjaExtraAPI, api_controller, route
from ninja import Router, ModelSchema
from ninja.pagination import paginate
from user_app.models import SysUser
from django_ninja_learn.entity.models import LimitDto
from django.core.paginator import Paginator

class SysUserInDto(ModelSchema):
    class Config:
        model = SysUser
        model_fields = "__all__"

class SysUserOutDto(ModelSchema):
    class Config:
        model = SysUser
        model_fields = "__all__"

@api_controller("/sys", tags=["user"])
class SysController:

    @route.post("/user/save")
    def save_user(self, payload: SysUserInDto):
        new_user = SysUser.objects.create(**payload.dict())
        new_user = SysUserOutDto.from_orm(new_user)
        return {"code": 200, "data": new_user}

    @route.get("/user/info/{id}")
    def info_user(self, id: int):
        sys_user = SysUser.objects.all().filter(id=id).first()
        sys_user = SysUserOutDto.from_orm(sys_user)
        return {"code": 200, "data": sys_user}

    @route.post("/user/list")   # response=List[SysUserOutDto]
    def list_user(self, payload: LimitDto):
        db_users = SysUser.objects.all()
        paginator = Paginator(db_users, payload.page_size)
        users_page = paginator.get_page(payload.page_no)
        user_list = [SysUserOutDto.from_orm(user) for user in users_page.object_list]
        return {"code": 200, "data": {
            "page_no": payload.page_no,
            "page_size": payload.page_size,
            "total": paginator.num_pages,
            "list": user_list
        }}

    @route.delete("/user/delete/{id}")
    def delete_user(self, id: int):
        SysUser.objects.filter(id=id).delete()
        return {"code": 200, "data": ""}

