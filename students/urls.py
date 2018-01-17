from django.conf.urls import url
from students import views


app_name = 'students'
urlpatterns = [
    url(r'^register/$', views.StudentRegistrationView.as_view(), name='student_registration'),
]