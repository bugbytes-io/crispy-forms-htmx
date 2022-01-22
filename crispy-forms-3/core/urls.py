from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', LogoutView.as_view(), name='logout')
]

htmx_urlpatterns = [
    path('check-username', views.check_username, name='check-username'),
    path('check-subject', views.check_subject, name='check-subject')
]

urlpatterns += htmx_urlpatterns