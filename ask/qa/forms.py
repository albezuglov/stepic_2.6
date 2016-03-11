from django import forms
from .models import *

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea) 

    def save(self):
        question = Question(**self.cleaned.data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea) 
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def save(self):
        answer = Answer(**self.cleaned.data)
        answer.save()
        return answer

