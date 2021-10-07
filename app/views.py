from django.shortcuts import render, redirect
from datetime import datetime,timedelta
# Create your views here.

def Index(request):
    context = {}
    if request.method == "POST":
        last = request.POST["last"]
        ovulation = int(request.POST["ovulation"])
        old_date=datetime.strptime(last,'%d-%m-%Y')
        est_date=timedelta(days=ovulation)
        men_date=old_date + est_date
        context = {
            'm':men_date
        }
    return render(request, 'app/index.html', context)