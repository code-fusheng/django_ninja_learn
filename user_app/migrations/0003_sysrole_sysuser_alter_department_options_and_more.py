# Generated by Django 4.2.4 on 2023-08-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0002_auto_20230812_2150"),
    ]

    operations = [
        migrations.CreateModel(
            name="SysRole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="主键"
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="备注"
                    ),
                ),
                (
                    "is_enabled",
                    models.IntegerField(
                        choices=[(1, "启用"), (0, "弃用")], default=1, verbose_name="是否启用"
                    ),
                ),
                (
                    "is_deleted",
                    models.IntegerField(
                        choices=[(0, "未删除"), (1, "已删除")], default=0, verbose_name="是否删除"
                    ),
                ),
                (
                    "creator_id",
                    models.BigIntegerField(blank=True, null=True, verbose_name="创建者ID"),
                ),
                (
                    "updater_id",
                    models.BigIntegerField(blank=True, null=True, verbose_name="更新者ID"),
                ),
                (
                    "creator_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="创建者名称"
                    ),
                ),
                (
                    "updater_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="更新者名称"
                    ),
                ),
                (
                    "created_time",
                    models.DateField(blank=True, null=True, verbose_name="创建时间"),
                ),
                (
                    "updated_time",
                    models.DateField(blank=True, null=True, verbose_name="更新时间"),
                ),
                ("name", models.CharField(max_length=50, verbose_name="角色名称")),
                (
                    "code",
                    models.CharField(max_length=50, unique=True, verbose_name="角色编码"),
                ),
            ],
            options={
                "verbose_name": "系统-角色表",
                "verbose_name_plural": "系统-角色表",
                "db_table": "sys_role",
                "ordering": ("-created_time",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SysUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="主键"
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="备注"
                    ),
                ),
                (
                    "is_enabled",
                    models.IntegerField(
                        choices=[(1, "启用"), (0, "弃用")], default=1, verbose_name="是否启用"
                    ),
                ),
                (
                    "is_deleted",
                    models.IntegerField(
                        choices=[(0, "未删除"), (1, "已删除")], default=0, verbose_name="是否删除"
                    ),
                ),
                (
                    "creator_id",
                    models.BigIntegerField(blank=True, null=True, verbose_name="创建者ID"),
                ),
                (
                    "updater_id",
                    models.BigIntegerField(blank=True, null=True, verbose_name="更新者ID"),
                ),
                (
                    "creator_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="创建者名称"
                    ),
                ),
                (
                    "updater_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="更新者名称"
                    ),
                ),
                (
                    "created_time",
                    models.DateField(blank=True, null=True, verbose_name="创建时间"),
                ),
                (
                    "updated_time",
                    models.DateField(blank=True, null=True, verbose_name="更新时间"),
                ),
                (
                    "username",
                    models.CharField(db_index=True, max_length=150, verbose_name="用户名"),
                ),
                ("password", models.CharField(max_length=500, verbose_name="密码")),
                (
                    "mobile",
                    models.CharField(max_length=50, null=True, verbose_name="手机号"),
                ),
                (
                    "email",
                    models.CharField(max_length=255, null=True, verbose_name="邮箱"),
                ),
                ("avatar", models.TextField(null=True, verbose_name="头像")),
                (
                    "gender",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "未知"), (1, "男"), (2, "女")],
                        default=0,
                        null=True,
                        verbose_name="性别",
                    ),
                ),
                (
                    "real_name",
                    models.CharField(max_length=100, null=True, verbose_name="真实姓名"),
                ),
                ("first_name", models.CharField(max_length=50, null=True)),
                ("last_name", models.CharField(max_length=50, null=True)),
                (
                    "signature",
                    models.CharField(max_length=500, null=True, verbose_name="签名"),
                ),
            ],
            options={
                "verbose_name": "系统-用户表",
                "verbose_name_plural": "系统-用户表",
                "db_table": "sys_user",
                "ordering": ("-created_time",),
                "abstract": False,
            },
        ),
        migrations.AlterModelOptions(
            name="department",
            options={"verbose_name": "基础模型", "verbose_name_plural": "基础模型"},
        ),
        migrations.AlterModelOptions(
            name="employee",
            options={"verbose_name": "基础模型", "verbose_name_plural": "基础模型"},
        ),
        migrations.AddField(
            model_name="department",
            name="created_time",
            field=models.DateField(blank=True, null=True, verbose_name="创建时间"),
        ),
        migrations.AddField(
            model_name="department",
            name="creator_id",
            field=models.BigIntegerField(blank=True, null=True, verbose_name="创建者ID"),
        ),
        migrations.AddField(
            model_name="department",
            name="creator_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="创建者名称"
            ),
        ),
        migrations.AddField(
            model_name="department",
            name="is_deleted",
            field=models.IntegerField(
                choices=[(0, "未删除"), (1, "已删除")], default=0, verbose_name="是否删除"
            ),
        ),
        migrations.AddField(
            model_name="department",
            name="is_enabled",
            field=models.IntegerField(
                choices=[(1, "启用"), (0, "弃用")], default=1, verbose_name="是否启用"
            ),
        ),
        migrations.AddField(
            model_name="department",
            name="remark",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="备注"
            ),
        ),
        migrations.AddField(
            model_name="department",
            name="updated_time",
            field=models.DateField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AddField(
            model_name="department",
            name="updater_id",
            field=models.BigIntegerField(blank=True, null=True, verbose_name="更新者ID"),
        ),
        migrations.AddField(
            model_name="department",
            name="updater_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="更新者名称"
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="created_time",
            field=models.DateField(blank=True, null=True, verbose_name="创建时间"),
        ),
        migrations.AddField(
            model_name="employee",
            name="creator_id",
            field=models.BigIntegerField(blank=True, null=True, verbose_name="创建者ID"),
        ),
        migrations.AddField(
            model_name="employee",
            name="creator_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="创建者名称"
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="is_deleted",
            field=models.IntegerField(
                choices=[(0, "未删除"), (1, "已删除")], default=0, verbose_name="是否删除"
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="is_enabled",
            field=models.IntegerField(
                choices=[(1, "启用"), (0, "弃用")], default=1, verbose_name="是否启用"
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="remark",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="备注"
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="updated_time",
            field=models.DateField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AddField(
            model_name="employee",
            name="updater_id",
            field=models.BigIntegerField(blank=True, null=True, verbose_name="更新者ID"),
        ),
        migrations.AddField(
            model_name="employee",
            name="updater_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="更新者名称"
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="id",
            field=models.BigAutoField(
                primary_key=True, serialize=False, verbose_name="主键"
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="id",
            field=models.BigAutoField(
                primary_key=True, serialize=False, verbose_name="主键"
            ),
        ),
    ]
