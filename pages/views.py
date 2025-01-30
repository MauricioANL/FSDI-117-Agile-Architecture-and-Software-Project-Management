from django.core.mail import send_mail
from django.shortcuts import render, redirect
from content.forms import ContactForm
from django.conf import settings

# Create your views here.

def home_view(request):
    return render(request,"pages/home.html")

def about_view(request):
    return render(request,"pages/about.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Datos del formulario
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Configura el correo
            send_mail(
                f"New Contact Message: {subject}",  # Asunto del correo
                f"Message from {name} ({email}):\n\n{message}",  # Cuerpo del correo
                email,  # Correo del remitente (puedes cambiarlo si deseas)
                [settings.EMAIL_HOST_USER],  # Correo del destinatario (puedes cambiarlo)
                fail_silently=False,
            )
            return redirect('success')  # Redirige a una página de éxito
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})