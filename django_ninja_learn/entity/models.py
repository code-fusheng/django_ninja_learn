from django.db import models
import json
from django.http import HttpResponse
from ninja import Schema
from typing import List

class BaseEntity(models.Model):
    id = models.BigAutoField(verbose_name="主键", primary_key=True)
    """基础模型"""
    remark = models.CharField(verbose_name="备注", max_length=255, null=True, blank=True)
    ENABLED_CHOICES = (
        (1, "启用"),
        (0, "弃用")
    )
    is_enabled = models.IntegerField(verbose_name="是否启用", choices=ENABLED_CHOICES, default=1)
    # 逻辑删除
    DELETED_CHOICES = (
        (0, "未删除"),
        (1, "已删除")
    )
    is_deleted = models.IntegerField(verbose_name="是否删除", choices=DELETED_CHOICES, default=0)
    creator_id = models.BigIntegerField(verbose_name="创建者ID", null=True, blank=True)
    updater_id = models.BigIntegerField(verbose_name="更新者ID", null=True, blank=True)
    creator_name = models.CharField(verbose_name="创建者名称", max_length=50, null=True, blank=True)
    updater_name = models.CharField(verbose_name="更新者名称", max_length=50, null=True, blank=True)
    created_time = models.DateField(verbose_name="创建时间", null=True, blank=True)
    updated_time = models.DateField(verbose_name="更新时间", null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = '基础模型'
        verbose_name_plural = verbose_name

class BaseResponse(HttpResponse):
    """公共响应体"""
    def __init__(self, data=None, msg="success", code=200, *args, **kwargs) -> None:
        std_data = {
            "code": code,
            "data": data,
            "msg": msg
        }
        data = json.dumps(std_data)
        super.__init__(data, *args, **kwargs)


class LimitDto(Schema):
    """基础分页"""
    page_no: int = 1
    page_size: int = 10

class PageVo(Schema):
    """分页响应对象"""
    page_no: int = 1
    page_size: int = 10
    total: int
    list: List