from django.contrib import admin
from django.urls import path

from thndr.api.deposit import deposit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deposit/', deposit, name="account-deposit"),
]
