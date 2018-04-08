from django.conf.urls import url

from . import views

app_name = 'office'

urlpatterns = [

    url(r'^officeOfDeanStudents/$', views.officeOfDeanStudents, name='officeOfDeanStudents'),
    url(r'^officeOfPurchaseOfficer/', views.officeOfPurchaseOfficr, name='officeOfPurchaseOfficer'),
    url(r'^officeOfRegistrar/', views.officeOfRegistrar, name='officeOfRegistrar'),
    url(r'^officeOfDeanRSPC/', views.officeOfDeanRSPC, name='officeOfDeanRSPC'),
    url(r'^officeOfDeanPnD/', views.officeOfDeanPnD, name='officeOfDeanPnD'),
    url(r'^genericModule/', views.genericModule, name='genericModule'),
    url(r'^officeOfDeanStudents/holding_meeting', views.holdingMeeting, name='holdingMeetings'),
    url(r'^officeOfDeanStudents/meeting_Minutes', views.meetingMinutes, name='meetingMinutes'),
    url(r'^officeOfDeanStudents/hostelRoomAllotment', views.hostelRoomAllotment),
    url(r'^officeOfDeanStudents/budget_approval', views.budgetApproval),
    url(r'^officeOfDeanStudents/budget_rejection', views.budgetRejection),
    url(r'^officeOfDeanStudents/club_approval', views.clubApproval),
    url(r'^officeOfDeanStudents/club_rejection', views.clubRejection),

]
