from django.contrib import admin

from apps.resumes.models import Resumes, ResumeSkills, VacancyResume

admin.site.register(Resumes)
admin.site.register(ResumeSkills)
admin.site.register(VacancyResume)
