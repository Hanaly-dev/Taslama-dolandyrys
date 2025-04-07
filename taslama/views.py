from django.shortcuts import render, get_object_or_404,redirect
from .models import*
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _

def index(request):
    return render(request, 'taslama/index.html')

def proyekt_list(request):
    gornus = request.GET.get("gornus")
    status = request.GET.get("status")
    
    proyektler = Taslama.objects.all()
    
    if gornus:
        proyektler = proyektler.filter(gornusi=gornus)
    
    if status:
        proyektler = proyektler.filter(status=status)
    
    jemi_taslama = Taslama.objects.count()
    dowam_edyan_sany = Taslama.objects.filter(status='dowam').count()
    tamamlanan_sany = Taslama.objects.filter(status='tamam').count()
    meyillesdirilen_sany = Taslama.objects.filter(status='planlanan').count()
    jemi_haryt_sany = Enjam.objects.count()
    
    
    stats = [
        {"label": "Jemi Taslama", "count": jemi_taslama},
        {"label": "Dowam edýän işler", "count": dowam_edyan_sany},
        {"label": "Meýilleşdirilen", "count": meyillesdirilen_sany},
        {"label": "Tamamlanan işler", "count": tamamlanan_sany},
        {"label": "Jemi Haryt", "count": jemi_haryt_sany}
]
    paginator = Paginator(proyektler, 6)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
    'proyektler': page_obj,
    'jemi_taslama': jemi_taslama,
    'dowam_edyan_sany': dowam_edyan_sany,
    'tamamlanan_sany': tamamlanan_sany,
    'meyillesdirilen_sany': meyillesdirilen_sany,  # Added this
    'jemi_haryt_sany': jemi_haryt_sany,
    'selected_gornus': gornus,
    'selected_status': status,
    'page_obj': page_obj,
    'stats': stats,
}
    return render(request, 'taslama/islerimiz.html', context)

def proyekt_detail(request, pk):
    proyekt = get_object_or_404(Taslama, pk=pk)
    return render(request, 'taslama/detail.html', {'proyekt': proyekt})

def products(request):
    enjamlar = Enjam.objects.all()
    paginator = Paginator(enjamlar, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj 
    }

    return render(request, 'taslama/harytlar.html', context)

def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email') 
        password = request.POST.get('password') 

        if not email or not password:
            messages.error(request, "Maglumatlary doly girizmeli!")
            return redirect('login')

        try:
            
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "E-mail salgyňyz ýalňyş")
            return redirect('login')  
        user = authenticate(request, username=user.username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            next_url = request.GET.get('next', 'index')  
            return redirect(next_url)  
        
        messages.error(request, "Ulanyjy hasaby ýok!")
        return redirect('login')  

    return render(request, 'taslama/login.html')  


def logoutView(request):
    logout(request)
    return redirect('login')


def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')  
        password = request.POST.get('password')  
        confirm_password = request.POST.get('confirm_password')  
        if not email or not password or not username:
            messages.error(request, _("Maglumatlary doly girizmeli"))
            return redirect('register')

        if password != confirm_password:
            messages.error(request, _("Parollar bir-birine deň bolmaly"))
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, _("Bu e-mail salgy üçin hasap döredilen"))
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, _("Bu ulanyjy ady üçin hasap döredilen"))
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, _("Hasap döredildi"))
        return redirect('login')  

    return render(request, 'taslama/register.html')