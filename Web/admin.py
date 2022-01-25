from django.contrib import admin
from .models import Verdict

# ----------------- Registering Verdict Model ---------------- #

@admin.register(Verdict)
class VerdictAdmin(admin.ModelAdmin):
    list_display = [
        "stock",
        "verdict"
    ]
    list_filter = [
        "verdict"
    ]
