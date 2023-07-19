# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:51:22 2023

@author: anhle
"""

from django.urls import path
from . import views

# urlpatterns = [path('', views.index, name = 'index'),]

urlpatterns = [
    path('', views.game, name='game'),
]