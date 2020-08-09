from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='insert'),
    path('<int:id>/', views.employee_form, name='update'),
    path('list', views.employee_list, name='list'),
    path('delete', views.employee_delete)
]
