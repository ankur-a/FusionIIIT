from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from applications.academic_information.models import Meeting
from .models import Constants,hostel_allotment,Budget
from applications.gymkhana.models import Club_budget,Club_info

def officeOfDeanStudents(request):
    budget_app= Club_budget.objects.all().filter(status='open');
    past_budget=Club_budget.objects.all().exclude(status='open');
    minutes=Meeting.objects.all().filter(minutes_file="");
    final_minutes=Meeting.objects.all().exclude(minutes_file="");
    hall_allotment=hostel_allotment.objects.all()
    clubNew= Club_info.objects.all().filter(status='open')
    club =Club_info.objects.all().exclude(status='open')
    budgets=Club_info.objects.all().exclude(status='open')
    context = {'meetingMinutes':minutes,
                'final_minutes':final_minutes,
                'hall': Constants.HALL_NO,
                'hall_allotment':hall_allotment,
                'budget_app':budget_app,
                'p_budget':past_budget,
                'clubNew':clubNew,
                'club':club,
                'budgets':budgets,}
    for details in budgets:
        print(type(details))
        details.avail_budget=details.alloted_budget - details.spent_budget
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
        a.remarks=request.POST.get(id_r[i])
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
        a.remarks=request.POST.get(id_r[i])
        a.save()

    return HttpResponseRedirect('/office/officeOfDeanStudents')


def clubApproval(request):
    id_r=request.POST.getlist('check')
    # print(remark)
    for i in range(len(id_r)):
        a=Club_info.objects.get(pk=id_r[i]);
        a.status='confirmed'
        a.save()

    return HttpResponseRedirect('/office/officeOfDeanStudents')


def clubRejection(request):
    id_r=request.POST.getlist('check')
    # print(remark)
    for i in range(len(id_r)):
        a=Club_info.objects.get(id=id_r[i]);
        a.status='rejected'
        a.save()

    return HttpResponseRedirect('/office/officeOfDeanStudents')