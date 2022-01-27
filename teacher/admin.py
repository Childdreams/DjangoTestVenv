# encoding=utf8
from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    #  配置展示列表，在Score版块下的列表展示
    list_display = ('status', 'tid', 'name', 'email', 'class_name', 'gender', 'phone', 'user')
    # 配置过滤查询字段，在Score版块下右侧过滤框
    list_filter = ('name', 'status', 'class_name', 'tid')
    # 配置可以搜索的字段，在Score版块下右侧搜索框
    # student是外键，管理student类，这里使用双下划线+属性名的方式搜索。
    ordering = ('-created_at',)  # 定义列表显示的顺序，负号表示降序
    fieldsets = (
        (None, {
            'fields': ('name', 'status', 'class_name', 'tid')
        }),
    )


admin.site.register(Teacher)
