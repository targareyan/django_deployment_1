from django.conf.urls import url
from app_afresh import views

urlpatterns = [
	url(r'^$', views.user1, name='usr'),
]