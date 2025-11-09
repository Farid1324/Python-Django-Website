from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Order
from .forms import OrderForm, ProfileForm, PreferencesForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram

def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    ctx = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form': form,
    }
    return render(request, 'index.html', ctx)

def thanks_page(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        if name or phone:
            element = Order(order_name=name, order_phone=phone)
            element.save()
            try:
                sendTelegram(tg_name=name, tg_phone=phone)
            except Exception:
                pass
        return render(request, 'thanks.html', {'name': name})
    return render(request, 'thanks.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def report(request):
    return render(request, 'report.html')

def settings_page(request):
    # Session-based UI preferences only (no login/profile needed)
    preferences_initial = {
        "timezone": request.session.get("timezone", "UTC"),
        "language": request.session.get("language", "en"),
        "newsletter": request.session.get("newsletter", False),
    }
    # You can leave out the profile stuff unless you want to add those forms
    ctx = {
        "preferences_form": PreferencesForm(initial=preferences_initial),
        "dark_mode": request.session.get("dark_mode", False),
    }
    return render(request, 'settings.html', ctx)

def settings_preferences(request):
    if request.method == "POST":
        form = PreferencesForm(request.POST)
        if form.is_valid():
            request.session["timezone"] = form.cleaned_data["timezone"]
            request.session["language"] = form.cleaned_data["language"]
            request.session["newsletter"] = form.cleaned_data["newsletter"]
            request.session["dark_mode"] = bool(request.POST.get("dark_mode"))
        return redirect("settings")
    return redirect("settings")

def export_data(request):
    return render(request, 'export_data.html')

def add_expense(request):
    return render(request, 'add_expense.html')

# These views can be left as stubs -- for demo only
def settings_profile(request):
    return redirect('settings')

def settings_password(request):
    return redirect('settings')

def settings_delete_account(request):
    return redirect('settings')
