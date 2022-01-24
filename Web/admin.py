from django.contrib import admin
from .models import Verdict

# Register your models here.

@admin.register(Verdict)
class VerdictAdmin(admin.ModelAdmin):
    list_display = [
        "stock",
        "verdict"
    ]
    list_filter = [
        "verdict"
    ]