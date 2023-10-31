from django.urls import path, include

urlpatterns = [
    path('', include("apps.users.urls")),
    path('',include("apps.message.urls")),
    path('', include("apps.core.urls")),
    path('', include('apps.resumes.urls'))
]
