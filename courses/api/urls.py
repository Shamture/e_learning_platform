from django.conf.urls import url
from courses.api import view

urlpatterns = [
    url(r'^subjects/$', view.SubjectListView.as_view(), name='subject_list'),
    url(r'^subjects/(?P<pk>\d+)/$', view.SubjectDetailView.as_view(), name='subject_detail'),
    url(r'^courses/(?P<pk>\d+)/enroll/$', view.CourseEnrollView.as_view(), name='course_enroll'),
]