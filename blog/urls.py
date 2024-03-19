from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('know-us', views.knowUs, name='know-us'),
    path('Features', views.Features, name='Features'),
    path('Admission', views.Admission, name='Admission'),
    path('Academics', views.Academics, name='Academics'),
    path('Students-Corner', views.Students_Corner, name='Students-Corner'),
    path('Notifications', views.Notifications, name='Notifications'),
    path('Downloads', views.Downloads, name='Downloads'),
    path('Gallery', views.Gallery, name='Gallery'),
    path('videos', views.videos, name='videos'),
    path('About', views.About, name='About'),
]
