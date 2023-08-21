from django.db import models
from django_ninja_learn.entity.models import BaseEntity
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Department(BaseEntity):
    """"部门表"""
    title = models.CharField(max_length=100)

class Employee(BaseEntity):
    """员工表"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.BigIntegerField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True)


# 用户 RBAC 系统设计
class SysUser(BaseEntity):
    """系统用户"""
    username = models.CharField(verbose_name="用户名", max_length=150, db_index=True)
    password = models.CharField(verbose_name="密码", max_length=500)
    mobile = models.CharField(verbose_name="手机号", max_length=50, null=True)
    email = models.CharField(verbose_name="邮箱", max_length=255, null=True)
    avatar = models.TextField(verbose_name="头像", null=True)
    GENDER_CHOICES = (
        (0, "未知"),
        (1, "男"),
        (2, "女")
    )
    gender = models.IntegerField(verbose_name="性别", choices=GENDER_CHOICES, default=0, null=True, blank=True)
    real_name = models.CharField(verbose_name="真实姓名", max_length=100, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    signature = models.CharField(verbose_name="签名", max_length=500, null=True)

    class Meta(BaseEntity.Meta):
        db_table = "sys_user"
        verbose_name = "系统-用户表"
        verbose_name_plural = verbose_name
        ordering = ('-created_time',)


class SysRole(BaseEntity):
    """系统角色"""
    name = models.CharField(verbose_name="角色名称", max_length=50)
    code = models.CharField(verbose_name="角色编码", max_length=50, unique=True)

    class Meta(BaseEntity.Meta):
        db_table = "sys_role"
        verbose_name = "系统-角色表"
        verbose_name_plural = verbose_name
        ordering = ('-created_time',)



