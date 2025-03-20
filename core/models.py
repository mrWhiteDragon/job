from django.db import models

class Vacancy(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    company = models.CharField(max_length=255, verbose_name='Компания')
    description = models.TextField(max_length=3000, verbose_name='Описание')
    salary = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Зарплата', blank=True, null=True)
    link = models.URLField(max_length=200, verbose_name='Ссылка')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-created_date']

    def __str__(self):
        return self.name

class VacancyComment(models.Model):
    text = models.CharField(max_length=500, verbose_name='Комментарий')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy_comments')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
