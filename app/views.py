from django.shortcuts import render, redirect
from datetime import datetime,timedelta
# Create your views here.

def Index(request):
    context = {}
    if request.method == "POST":
        last = request.POST["last"]
        ovulation = request.POST["ovulation"]
        if last and ovulation:
            ovulation_ = int(ovulation)
            old_date=datetime.strptime(last,'%d-%m-%Y')
            est_date=timedelta(days=ovulation_)
            men_date=old_date + est_date
            context = {
                'm':men_date
            }
        else:
            None
    return render(request, 'app/index.html', context)