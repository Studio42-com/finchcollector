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
      
      path('finches/<int:finch_id>/assoc_medicine/<int:medicine_id>/', views.assoc_medicine, name='assoc_medicine'),
#     path('cats/   <int:cat_id>/  assoc_toy/     <int:toy_id>     /', views.assoc_toy,      name='assoc_toy'),
#       
      path('medicines/', views.MedicineList.as_view(), name='medicines_index'),
      
      path('medicines/<int:pk>/', views.MedicineDetail.as_view(), name='medicines_detail'),
      path('medicines/create/', views.MedicineCreate.as_view(), name='medicines_create'),
      
      path('medicines/<int:pk>/update/', views.MedicineUpdate.as_view(), name='medicines_update'),
      path('medicines/<int:pk>/delete/', views.MedicineDelete.as_view(), name='medicines_delete'),]