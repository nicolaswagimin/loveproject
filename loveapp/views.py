from django.shortcuts import render
from datetime import date

def home(request):
    start_date = date(2020, 8, 28)  # fecha de aniversario
    today = date.today()
    days_together = (today - start_date).days

    context = {
        "days_together": days_together,
        "name": "Valentina"
    }
    return render(request, "loveapp/home.html", context)
