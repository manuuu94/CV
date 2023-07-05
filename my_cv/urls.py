from django.urls import path
from . import views


app_name = 'cv_manu'

urlpatterns = [
    path('',views.my_cv,name='cv_manu'),

]

