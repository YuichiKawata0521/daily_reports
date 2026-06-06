from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Departments(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="部署名")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, verbose_name="親部門コード")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    is_active = models.BooleanField(default=True, verbose_name="有効・無効")

    def __str__(self):
        return self.name

class Roles(models.Model):
    role = models.CharField(max_length=50, null=False, blank=False, verbose_name="権限")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    is_active = models.BooleanField(default=True, verbose_name="有効・無効")

    def __str__(self):
        return self.role

class CustomUser(AbstractUser):
    class Sex(models.TextChoices):
        MALE = "male", "男性"
        FEMALE = "female", "女性"
        NOANSWER = "noanswer",  "回答無し"

    employee_no = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name="従業員番号")
    middle_name = models.CharField(max_length=20, null=True, blank=True, verbose_name="ミドルネーム")
    sex = models.CharField(max_length=10, choices=Sex, null=False, blank=False, verbose_name="性別")
    birth_date = models.DateField(null=False, blank=False, verbose_name="誕生日")
    tel = models.CharField(max_length=11, null=False, blank=False, verbose_name="電話番号")
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, verbose_name="権限")
    postcode = models.CharField(max_length=7, null=False, blank=False, verbose_name="郵便番号")
    prefecture = models.CharField(max_length=5, null=False, blank=False, verbose_name="都道府県")
    city = models.CharField(max_length=10, null=False, blank=False, verbose_name="市町村")
    address1 = models.CharField(max_length=50, null=False, blank=False, verbose_name="番地以降")
    address2 = models.CharField(max_length=50, null=True, blank=True, verbose_name="マンション名など")
    department = models.ForeignKey(Departments, on_delete=models.PROTECT, related_name="users", verbose_name="部署", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")

    REQUIRED_FIELDS = [
        "email",        # AbstractUserには存在しますが、明示的に入力を求めるため追加推奨
        "employee_no",
        "sex",
        "birth_date",
        "tel",
        "postcode",
        "prefecture",
        "city",
        "address1",
    ]

    def __str__(self):
        return f"{self.employee_no} - {self.last_name} - {self.first_name}"




class DailyReports(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "下書き",
        SUBMITTED = "submitted", "提出済み",
        APPROVED = "approved", "承認済み",
        RETURN = "return", "差し戻し"
    
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="dailyreports", verbose_name="日報")
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="日報")
    content = models.TextField(null=False, blank=False, verbose_name="日報内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    status = models.CharField(choices=Status, null=False, blank=False, verbose_name="ステータス")

    def __str__(self):
        return self.title

class WeeklyReports(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "下書き",
        SUBMITTED = "submitted", "提出済み",
        APPROVED = "approved", "承認済み",
        RETURN = "return", "差し戻し"
    
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="weeklyreports", verbose_name="日報")
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="週報タイトル")
    content = models.TextField(null=False, blank=False, verbose_name="週報内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    status = models.CharField(choices=Status, null=False, blank=False, verbose_name="ステータス")

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="タグ名")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")

    def __str__(self):
        return self.name

class DailyReportTag(models.Model):
    report = models.ForeignKey(DailyReports, on_delete=models.CASCADE, related_name="report_tags")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="report_tags")

    class Meta:
        db_table = "report_tags"
        constraints = [
            models.UniqueConstraint (
                fields=["report", "tag"],
                name="unique_report_tag"
            )
        ]
    
    def __str__(self):
        return f"{self.report.title} - {self.tag.name}"

class Templates(models.Model):
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE, verbose_name="部署ID")
    template_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="テンプレート名")
    content_layout = models.TextField(max_length=max, null=True, blank=True, verbose_name="テンプレート内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    is_active = models.BooleanField(default=True, verbose_name="有効・無効")

    def __str__(self):
        return self.template_name

