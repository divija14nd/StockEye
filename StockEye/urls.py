
from django.contrib import admin
from django.urls import path, include

# ------------------------- Importing Application URL ------------------------- #
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Web.urls'), name='web_urls'),
]
