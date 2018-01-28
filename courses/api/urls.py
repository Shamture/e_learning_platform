from django.conf.urls import url, include
from courses.api import view
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', view.CourseViewSets)

urlpatterns = [
    url(r'^subjects/$', view.SubjectListView.as_view(), name='subject_list'),
    url(r'^subjects/(?P<pk>\d+)/$', view.SubjectDetailView.as_view(), name='subject_detail'),
    url(r'^', include(router.urls)),
]