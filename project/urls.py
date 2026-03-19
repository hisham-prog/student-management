"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from Home.views import *
from django.urls import include
# from student import views as S


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('h/',views.hello),
    # # path('w/',views.wel)
    # path('w/<int:age>',views.wel),
    path('', myhome, name='home'),
    path('reg/',Empreg),
    # path('sta/',views.mystatic),
    path('hh/',myhome),
    path('list/',emp_list),
    # path('del/<int:pki>',views.emp_del),
    # path('upd/<int:pke>',views.emp_edit),
    # path('update/<int:pke>',views.emp_update),
    path('studReg/',stud_reg),


    path('registered student/',student_list,name='stud-list'),
    path('student/add',StudentCreateView.as_view(),name='student-add'),
    path('student/',StudentListView.as_view(),name='student-list'),
    path('students/delete/<int:pk>/',StudentDeleteView.as_view(),name='student-delete'),
    path('students/update/<int:pk>/',StudentUpdateView.as_view(),name='student-update'),

    path('login/', user_login, name='login'),   
    

    # path('stud/',S.mystud),
    path('SS/', include('student.urls')),
    path('mail/',send_eml,name='mail')

    
]
