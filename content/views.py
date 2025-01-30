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


from django.views.generic import ListView, CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm, ContactForm
from django.views import View


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


class ContactView(FormView):
    form_class = ContactForm  # Aquí usas el formulario de contacto, no el de proyectos
    template_name = 'contact/contact.html'  # La plantilla correspondiente para la vista de contacto
    success_url = reverse_lazy('success_url')  # Redirige a una URL de éxito después de enviar el formulario

    def form_valid(self, form):
        # Aquí puedes manejar los datos cuando el formulario sea válido
        form.save()  # O cualquier lógica que necesites (por ejemplo, enviar un correo)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Aquí puedes manejar el caso cuando el formulario no sea válido
        return super().form_invalid(form)