from django.urls import path
from . import views  # to import views from same folder represents .

'''
urlpatterns = [
    path("january", views.january),
    path("february", views.february),
    path("march", views.march),
    path("april", views.april)
    ]
'''
    #instead of above multiple entries for each month we can do it dynamic as below
urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number), #int will convert the input month value to int
    path("<str:month>", views.monthly_challenge) #str will convert the input month value to string
    ]

