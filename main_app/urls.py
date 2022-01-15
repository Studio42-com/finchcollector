from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('finches/', views.finches_index, name='finches_index'),
      path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail'),
      path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
      path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
      path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
      path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
      path('toys/', views.MedicineList.as_view(), name='medicines_index'),
      path('toys/<int:pk>/', views.MedicineDetail.as_view(), name='medicines_detail'),
      path('toys/create/', views.MedicineCreate.as_view(), name='medicines_create'),
      path('toys/<int:pk>/update/', views.MedicineUpdate.as_view(), name='medicines_update'),
      path('toys/<int:pk>/delete/', views.MedicineDelete.as_view(), name='medicines_delete'),]