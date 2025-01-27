import django_tables2 as tables
from django.contrib.auth.models import User

class UserTable(tables.Table):
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ("username", "last_name" ,"first_name", "email", "is_active", "is_superuser", "last_login" )