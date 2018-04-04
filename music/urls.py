from django.urls import path
from . import views


app_name = 'music'
urlpatterns = [
	# /music/
    path('', views.index, name='index'),
   path( '/fib/', views.nth_fibonacci, name='nth_fibonacci' ),

]