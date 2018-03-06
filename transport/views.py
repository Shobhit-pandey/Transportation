from datetime import datetime, date
import csv
import xlrd
from pyexcel_xls import get_data
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from transport.forms import AddTruck, ImportTruck
from transport.models import TruckLists, NotificationFitness, NotificationInsurance, NotificationPollution


def home(request):
    return render(request, 'home.html')


def list(request):
    lists = TruckLists.objects.all()
    return render(request, 'trucklist.html', {'lists': lists})


def notification(request):
    remainder()
    noti_insurance = NotificationInsurance.objects.all()
    noti_fitness = NotificationFitness.objects.all()
    noti_pollution = NotificationPollution.objects.all()
    for i in noti_insurance:
        if i.remaining_insurance <= 30:
            i.remainder = True
        if i.remaining_insurance <= 7:
            if i.remainded_for_remaining_day != 7:
                i.remainded_for_remaining_day = 7
                i.read = False
                i.save()
        elif i.remaining_insurance <= 15:
            if i.remainded_for_remaining_day != 15:
                i.remainded_for_remaining_day = 15
                i.read = False
                i.save()
        elif i.remaining_insurance <= 30:
            if i.remainded_for_remaining_day != 30:
                i.remainded_for_remaining_day = 30
                i.read = False
                i.save()
    for i in noti_fitness:
        if i.remaining_fitness <= 30:
            i.remainder = True
        if i.remaining_fitness <= 7:
            if i.remainded_for_remaining_day != 7:
                i.remainded_for_remaining_day = 7
                i.read = False
                i.save()
        elif i.remaining_fitness <= 15:
            if i.remainded_for_remaining_day != 15:
                i.remainded_for_remaining_day = 15
                i.read = False
                i.save()
        elif i.remaining_fitness <= 30:
            if i.remainded_for_remaining_day != 30:
                i.remainded_for_remaining_day = 30
                i.read = False
                i.save()
    for i in noti_pollution:
        if i.remaining_pollution <= 30:
            i.remainder = True
        if i.remaining_pollution <= 7:
            if i.remainded_for_remaining_day != 7:
                i.remainded_for_remaining_day = 7
                i.read = False
                i.save()
        elif i.remaining_pollution <= 15:
            if i.remainded_for_remaining_day != 15:
                i.remainded_for_remaining_day = 15
                i.read = False
                i.save()
        elif i.remaining_pollution <= 30:
            if i.remainded_for_remaining_day != 30:
                i.remainded_for_remaining_day = 30
                i.read = False
                i.save()
    notify_insurance = NotificationInsurance.objects.filter(remainder=True, read=False)
    notify_fitness = NotificationFitness.objects.filter(remainder=True, read=False)
    notify_pollution = NotificationPollution.objects.filter(remainder=True, read=False)
    return render(request, 'notification.html', {'notify_insurance': notify_insurance, 'notify_fitness': notify_fitness,
                                                 'notify_pollution': notify_pollution})


def remainder():
    lists = lists = TruckLists.objects.all()
    # Notification.objects.all().delete()
    current_date = date.today()
    for i in lists:
        insurance_left = ''
        remaining = i.insurance - current_date;
        remaining = str(remaining)
        for j in remaining:
            if j == ' ':
                break;
            else:
                insurance_left += j
        fitness_left = ''
        remaining = i.fitness - current_date;
        remaining = str(remaining)
        for j in remaining:
            if j == ' ':
                break;
            else:
                fitness_left += j
        pollution_left = ''
        remaining = i.pollution - current_date;
        remaining = str(remaining)
        for j in remaining:
            if j == ' ':
                break;
            else:
                pollution_left += j
        truck_available = NotificationInsurance.objects.filter(truck_number=i.truck_number)
        if truck_available:
            truck_available.update(remaining_insurance=insurance_left)
        else:
            NotificationInsurance.objects.create(truck_number=i.truck_number, insurance=i.insurance, read=0,
                                                 remainder=0,
                                                 remaining_insurance=insurance_left, remainded_for_remaining_day=31)

        truck_available = NotificationFitness.objects.filter(truck_number=i.truck_number)

        if truck_available:
            truck_available.update(remaining_fitness=fitness_left)
        else:
            NotificationFitness.objects.create(truck_number=i.truck_number, fitness=i.fitness,
                                               read=0, remainder=0, remaining_fitness=fitness_left,
                                               remainded_for_remaining_day=31)

        truck_available = NotificationPollution.objects.filter(truck_number=i.truck_number)
        if truck_available:
            truck_available.update(remaining_pollution=pollution_left)
        else:
            NotificationPollution.objects.create(truck_number=i.truck_number,
                                                 pollution=i.pollution, read=0, remainder=0,
                                                 remaining_pollution=pollution_left, remainded_for_remaining_day=31)


def addtruck(request):
    form = AddTruck()
    if request.method == 'POST':
        form = AddTruck(request.POST)
        if form.is_valid():
            s=form.save(commit=False)
            truck = form.cleaned_data['truck_number']
            t = TruckLists.objects.filter(truck_number=truck)
            if t:
                print("1")
                for i in t:
                    i.delete()
                ins = NotificationInsurance.objects.filter(truck_number=truck)
                for i in ins:
                    print("2")
                    i.delete()
                fit = NotificationFitness.objects.filter(truck_number=truck)
                for i in fit:
                    print("3")
                    i.delete()
                pol = NotificationPollution.objects.filter(truck_number=truck)
                for i in pol:
                    print("4")
                    i.delete()
            s.save()

            return redirect('transport:home')
    else:
        form = AddTruck()
    return render(request, 'addtruck.html', {'form': form})


def import_truck(request):
    form = ImportTruck()
    if request.method == 'POST':
        form = ImportTruck(request.POST, request.FILES)
        print("s")
        if form.is_valid():
            print("dfs")
            excel = request.FILES.get('excel',False)
            print(excel)
            data = get_data(excel)
            import json
            from bson import json_util
            js = json.dumps(data,default=myconverter)  #default=json_util.default
            cs = csv.DictReader(excel)
            print(js)
            # js = json.loads(js)
            k=0
            temp_list=[]
            temp=''
            ini = 0
            start =0
            for key in range(0,len(js)):
                if js[key] == '"':
                    ini+=1
                    if ini % 2 ==0:
                        temp_list.append(temp)
                        temp = ''
                        if start == 0:
                            del temp_list[:]
                        start = start+1
                    if start>1:
                        if len(temp_list) == 4:
                            print(temp_list)
                            TruckLists.objects.create(
                                truck_number=temp_list[0], insurance=temp_list[1], fitness=temp_list[2],
                                pollution=temp_list[3]
                            )
                            del temp_list[:]
                    continue
                if ini !=0:
                    if ini % 2 ==1:
                        temp+=js[key]
            print(temp_list)
            # for ad in range(1,len(temp_list)):
            #     TruckLists.objects.create(
            #         truck_number=temp_list[ad],insurance=temp_list[ad+1],fitness=temp_list[ad+2],pollution=temp_list[ad+3]
            #     )
            #     ad=ad+4
            # TruckLists.objects.create(**js)
            return redirect('transport:list')
    else:
        form = ImportTruck()
    return render(request, 'import_truck.html', {'form': form})


def myconverter(o):
    if isinstance(o, date):
        return o.isoformat()
    raise TypeError("Unknown type")


def notification_insurance_readed(request, pk1):
    insurance = NotificationInsurance.objects.filter(truck_number=pk1)
    for i in insurance:
        i.read = True
        i.save()
    return redirect('transport:notification')


def notification_fitness_readed(request, pk2):
    fitness = NotificationFitness.objects.filter(truck_number=pk2)
    for i in fitness:
        i.read = True
        i.save()
    return redirect('transport:notification')


def notification_pollution_readed(request, pk3):
    pollution = NotificationPollution.objects.filter(truck_number=pk3)
    for i in pollution:
        i.read = True
        i.save()
    return redirect('transport:notification')


def past_notification(request):
    notify_insurance = NotificationInsurance.objects.filter(remainder=True)
    notify_fitness = NotificationFitness.objects.filter(remainder=True)
    notify_pollution = NotificationPollution.objects.filter(remainder=True)
    return render(request, 'past_notification.html', {'notify_insurance': notify_insurance, 'notify_fitness': notify_fitness,
                                                 'notify_pollution': notify_pollution})