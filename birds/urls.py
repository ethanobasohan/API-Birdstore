from django.urls import path
from .views import BirdListCreate, BirdDetail


urlpatterns = [
    path('birds/', BirdListCreate.as_view(), name='bird-list-create'),
    path('birds/<str:name>/', BirdDetail.as_view(), name='bird-detail'),
]


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('birds.urls')),
]


