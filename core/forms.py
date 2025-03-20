from django import forms
from .models import Vacancy, VacancyComment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'company', 'description', 'salary', 'link']

    def __init__(self, *args, **kwargs):
        super(VacancyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'company',
            'description',
            'salary',
            'link',
            Submit('submit', 'Добавить')
        )


class VacancyCommentForm(forms.ModelForm):
    class Meta:
        model = VacancyComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
                'label': 'Текст',
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Добавить комментарий'))