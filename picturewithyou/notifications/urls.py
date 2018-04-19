from django.conf.urls import url
from . import views

app_name = "notification"
urlpatterns = [
	url(regex=r"^$", 
		view=views.Notifications.as_view(), 
		name="notifications"
	)
]

