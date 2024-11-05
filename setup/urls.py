from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("snippets.urls")),
    path("api-auth/", include("rest_framework.urls")),  # Para login via browsable API
]