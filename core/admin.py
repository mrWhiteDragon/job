from django.contrib import admin
from .models import Vacancy, VacancyComment

admin.site.register(Vacancy)
admin.site.register(VacancyComment)
