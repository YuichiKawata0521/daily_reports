from django.contrib import admin
from . import models

admin.site.register(models.Departments)
admin.site.register(models.Roles)
admin.site.register(models.CustomUser)
admin.site.register(models.DailyReports)
admin.site.register(models.WeeklyReports)
admin.site.register(models.Tag)
admin.site.register(models.DailyReportTag)
admin.site.register(models.Templates)

# Register your models here.
