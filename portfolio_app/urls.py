from django.urls import path
from portfolio_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('update_profile/',update_profile,name="update"),

]
