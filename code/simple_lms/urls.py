"""
URL configuration for simple_lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *

from django.contrib import admin
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path('testing/', testing),
    path('addData/', addData),
    path('editData/', editData),
    path('deleteData/', deleteData),
    path('courses/', allCourse),
    path('usercourses/', userCourses),
    path('coursestat/', courseStat),
    path('coursememberstat/', courseMemberStat),
    path('coursedetail/<int:course_id>/', courseDetail, name='courseDetail'),
    path('profile/<int:user_id>/', userProfile, name='userProfile'),
    path('userstat/', userStats, name='userStats'),
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]