from django.contrib import admin

from .models import clubInfo,clubMember,coreTeam,clubBudget,sessionInfo,eventReport

admin.site.register(clubInfo)
admin.site.register(clubMember)
admin.site.register(coreTeam)
admin.site.register(clubBudget)
admin.site.register(sessionInfo)
admin.site.register(eventReport)
