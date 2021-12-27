from .views import EmployeeViewSet
from rest_framework import routers
from . import views
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeViewSet, basename='employee')
urlpatterns =[
    path('', include(router.urls) ),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]
