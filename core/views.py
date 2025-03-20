from django.shortcuts import render, redirect, get_object_or_404
from .models import Vacancy
from .forms import VacancyForm, VacancyCommentForm

def main(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = VacancyForm()

    vacancies = Vacancy.objects.all()
    return render(request,'main.html', {'vacancies': vacancies, 'form': form})


def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    comments = vacancy.vacancy_comments.all()

    if request.method == 'POST':
        form = VacancyCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.vacancy = vacancy
            comment.save()
            return redirect('vacancy_detail', vacancy_id=vacancy.id)
    else:
        form = VacancyCommentForm()

    return render(request, 'vacancy_detail.html', {
        'vacancy': vacancy,
        'comments': comments,
        'form': form,
    })
