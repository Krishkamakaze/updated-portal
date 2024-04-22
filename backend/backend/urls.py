from api import views
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('facultyapi', views.facultyViewset , basename= 'faculty_val')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('studentapi/', views.StudentListCreate.as_view()),
    path('studentapi/<int:rollnumber>', views.StudentRetrieveUpdate.as_view()),
    path('', include(router.urls))
]
