from django.urls import path
from . import views
urlpatterns = [
    # 127.0.0.1:8000/pages
    path('' , views.pagesIndex),
    path('cars/', views.viewCars, name="viewCars"),
    path('singleCar/<id>',views.singleCar, name="singleCar"),
    path('deleteCar/<id>',views.deleteCar, name="deleteCar"),
    path('createCar',views.createCar, name="createCar"),
    path('editCar/<id>',views.editCar, name="editCar"),
]