from django.urls import path
from . import views

urlpatterns = [
    path('insert', views.employee_form, name='insert'),
    path('<int:id>/', views.employee_form, name='update'),
    path('', views.employee_list, name='list'),
    path('delete/<int:id>', views.employee_delete, name='delete')
]
