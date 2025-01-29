from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','year','image','repository','skill']
        widgets = {
            "name": forms.TextInput(attrs={"placehoder":"Project Name"}),
            "description": forms.Textarea(attrs={"placehoder":"Description"}),
            "year": forms.NumberInput(attrs={"placehoder":"YYYY"}),
            "image": forms.ClearableFileInput(attrs={"placehoder":"Select and Image"}),
            "repository": forms.URLInput(attrs={"placehoder":"Github URL"}),
            # "description": form.Textarea,'year','image','repository','skill'
        }