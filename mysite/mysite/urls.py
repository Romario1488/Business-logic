from django.urls.conf import path, include

urlpatterns = [
    path('mailings/', include('mailings.urls')),
]
