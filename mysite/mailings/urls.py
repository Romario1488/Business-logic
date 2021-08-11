from django.urls.conf import path, include
from . import views

urlpatterns = [
    path('add_to_common_list', views.add_email_to_common_list),
    path('add_to_case_list', views.add_email_to_case_list),
]
