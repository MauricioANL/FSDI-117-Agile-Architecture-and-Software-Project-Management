# from django.shortcuts import render, redirect
# from .models import Project
# from .forms import ProjectForm

# # Create your views here.
# def projects_list_view(request):
#     return render(request,"content/home.html")

# def projects_list_view(request):
#     projects = Project.objects.all()
#     return render(request, "projects/projects_list.html",{"projects":projects})

# def project_new(request):
#     if request.method == "POST":
#         form = ProjectForm(request.POST,request.FILES)
#         if form.is_valid():
#             project = form.save()
#             return redirect("projects_list")
#     else:
#         form = ProjectForm()
#     return render(request,"projects/project_new.html", {"form":form})


from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    model=Project
    template_name="projects/projects_list.html"
    context_object_name= "projects"


class ProjectCreateView(CreateView):
    model=Project
    form_class = ProjectForm
    template_name="projects/project_new.html"
    success_url = reverse_lazy("projects_list")

class ExperienceListView(TemplateView):
    template_name = "experience\experience.html"