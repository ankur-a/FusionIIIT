from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from applications.academic_information.models import Meeting
from .models import Constants,hostel_allotment
from applications.gymkhana.models import Club_budget

def officeOfDeanStudents(request):
    budget= Club_budget.objects.all().filter(status='open');
    past_budget=Club_budget.objects.all().exclude(status='open');
    minutes=Meeting.objects.all().filter(minutes_file="");
    final_minutes=Meeting.objects.all().exclude(minutes_file="");
    hall_allotment=hostel_allotment.objects.all()
    context = {'meetingMinutes':minutes,
                'final_minutes':final_minutes,
                'hall': Constants.HALL_NO,
                'hall_allotment':hall_allotment,
                'budget':budget,
                'p_budget':past_budget}
    # print(budget)
    return render(request, "officeModule/officeOfDeanStudents/officeOfDeanStudents.html", context)


def officeOfPurchaseOfficr(request):
    return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html", {})


def officeOfRegistrar(request):
    context = {}

    return render(request, "officeModule/officeOfRegistrar/officeOfRegistrar.html", context)


def officeOfDeanRSPC(request):
    context = {}

    return render(request, "officeModule/officeOfDeanRSPC/officeOfDeanRSPC.html", context)


def officeOfDeanPnD(request):
    context = {}

    return render(request, "officeModule/officeOfDeanPnD/officeOfDeanPnD.html", context)


def genericModule(request):
    context = {}

    return render(request, "officeModule/genericModule/genericModule.html", context)

def holdingMeeting(request):
    title= request.POST.get('title')
    date = request.POST.get('date')
    Time = request.POST.get('time')
    Venue = request.POST.get('venue')
    Agenda = request.POST.get('Agenda')
    p=Meeting(title=title,venue=Venue,date=date,time=Time,agenda=Agenda);
    p.save()
    return HttpResponseRedirect('/office/officeOfDeanStudents')
    
def meetingMinutes(request):
    # print(request.FILES['minutes_file'])
    # print(request.POST)
    file=request.FILES['minutes_file']
    id=request.POST.get('id')
    b=Meeting.objects.get(id=id)
    b.minutes_file=file
    b.save()
    #print(file)
    #a=Meeting.objects.all().filter(minutes_file="");
    #print(a)
    return HttpResponseRedirect('/office/officeOfDeanStudents')

def hostelRoomAllotment(request):
    file=request.FILES['hostel_file']
    hall_no=request.POST.get('hall_no')
    #description= request.POST.get('description')
    p=hostel_allotment(allotment_file=file,hall_no=hall_no)
    p.save()
    return HttpResponseRedirect('/office/officeOfDeanStudents')

def budgetApproval(request):
    # print(request.POST.getlist('check'))
    id_r=request.POST.getlist('check')
    remark=request.POST.getlist('remark')
    for i in range(len(id_r)):
        a=Club_budget.objects.get(id=id_r[i]);
        a.status='confirmed'
        a.remarks=remark[i]
        a.save()
        

    # print(id[0])

    return HttpResponseRedirect('/office/officeOfDeanStudents')

def budgetRejection(request):
    id_r=request.POST.getlist('check')
    remark=request.POST.getlist('remark')
    # print(remark)
    for i in range(len(id_r)):
        a=Club_budget.objects.get(id=id_r[i]);
        a.status='rejected'
        a.remarks=remark[i]
        a.save()

    return HttpResponseRedirect('/office/officeOfDeanStudents')