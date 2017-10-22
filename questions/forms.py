from django import forms
# from django.forms import ModelForm
from .models import Question

class QuestionForm(forms.Form):
    question = forms.CharField(label = '', widget=forms.Textarea(attrs={'rows': '3', 'cols': '', 'class': 'form-control'}), max_length = 400)

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ('question_text',)