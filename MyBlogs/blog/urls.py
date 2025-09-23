from django.urls import path
from .views import *


urlpatterns = [
    path('',home),
    path('blog/<str:url>',post),
    path('category/<str:url>',category),
    path('about/',about)
]