from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Expr)
class ExprAdmin(admin.ModelAdmin):
    pass
