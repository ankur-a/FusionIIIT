# imports
from django.contrib.auth.models import User
from django.db import models
from django import template
from datetime import datetime, timedelta
from django.utils import timezone

register = template.Library()
# Class definations:


# # Class for various choices on the enumerations
class Constants:
	categoryCh = (
		('Technical','Technical'),
		('Sports','Sports'),
		('Cultural','Cultural')
		)
	status = (
		('open','Open'),
		('confirmed','Confirmed'),
		('rejected','Rejected')
		)

class clubInfo(models.Model):
	clubName = models.CharField(max_length=50, primary_key=True)
	category = models.CharField(max_length=50, null=False, choices = Constants.categoryCh)
	coOrdinator = models.ForeignKey(User, null=False, related_name='co_of')
	cocoOrdinator = models.ForeignKey(User, null=False, related_name='coco_of')
	faultyIncharge = models.ForeignKey(User, null=False, related_name='faculty_incharge_of')	
	clubFile = models.FileField(upload_to='uploads/',null=True)
	activityCalender = models.FileField(upload_to='uploads/',null=True)

	def __str__(self):
		return self.clubName

class clubMember(models.Model):
	id = models.AutoField(max_length=20, primary_key=True)
	member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member_of')
	club = models.ForeignKey(clubInfo, related_name='this_club', null=False)
	desc = models.TextField(max_length=256, null=True)
	status = models.CharField(max_length=50, choices = Constants.status, default = 'open')

	def __str__(self):
		return 'username : {}'.format(self.member.username)

class coreTeam(models.Model):
	id = models.AutoField(max_length=20,primary_key=True)
	rollNo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applied_for')
	postApplied = models.CharField(max_length=50, null=False)
	backlogs = models.TextField(max_length=256, null=False)
	pda = models.TextField(max_length=256, null=False)
	status = models.CharField(max_length=50, choices=Constants.status, default = 'open')

	def __str__(self):
		return self.id

class clubBudget(models.Model):
	id = models.AutoField(max_length=20,primary_key=True)
	club = models.ForeignKey(clubInfo,max_length=50,null=False)
	budgetFor = models.CharField(max_length=256, null=False)
	budgetFile = models.FileField(upload_to='uploads/',null=False)
	desc = models.TextField(max_length=256, null=False)
	status = models.CharField(max_length=50, choices=Constants.status, default='open')

	def __str__(self):
		return self.id

class sessionInfo(models.Model):
	id = models.AutoField(max_length=20,primary_key=True)
	club = models.ForeignKey(clubInfo, max_length=50,null=True)
	venue = models.CharField(max_length=50,null=False)
	date = models.DateTimeField(default=datetime.now()+ timedelta(days=1),max_length=50, blank = True)
	details = models.TextField(max_length=256, null=True)

	def __str__(self):
		return self.id

class eventReport(models.Model):
	id = models.AutoField(max_length=20,primary_key=True)
	club = models.ForeignKey(clubInfo,max_length=50,null=False)
	incharge = models.ForeignKey(User,max_length=256,null=False)
	eventName = models.CharField(max_length=50,null=False)
	date = models.DateTimeField(max_length=50,default=datetime.now()+ timedelta(days=1), blank = True)
	eventReport = models.FileField(upload_to='uploads/',null=False)

	def __str__(self):
		return self.id