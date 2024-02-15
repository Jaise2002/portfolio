from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home,name='home'),
    path('dummy',views.dummy,name='dummy'),
    
    path('add/',views.add,name='add'),
    path('addrec/',views.addrec,name='addrec'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('update/uprec/<int:id>/',views.uprec,name='uprec'),
    path('',views.main,name='main'),
    path('login/',views.user_login,name='login'),
    path('loginn/',views.loginn,name='loginn'),
    path('register/',views.register,name='register'),
    path('registerr/',views.user_register,name='user_register'),
    path('addmark/',views.addmark,name='addmark'),
    path('addmarks/',views.addmarks,name='addmarks'),
    path('seemarks/',views.seemarks,name='seemarks')

  ]