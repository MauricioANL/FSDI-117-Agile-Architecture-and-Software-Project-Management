from django.urls import path
from . import views
from .views import ProjectListView, ProjectCreateView, ExperienceListView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("project_new", ProjectCreateView.as_view(), name="project_new"),
    path("experiencie", ExperienceListView.as_view(), name="experience_list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)