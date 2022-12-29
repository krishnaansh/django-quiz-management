import nested_admin
from django import forms
from django.contrib import admin
from quiz_management.models import *


class QuestionModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionModelForm, self).__init__(*args, **kwargs)
        self.fields["label"].widget.attrs["placeholder"] = "Type your Question"

    class Meta:
        model = Question
        fields = "__all__"


class QuizModelForm(forms.ModelForm):
    slug = forms.SlugField(required=False)

    class Meta:
        model = Quiz
        fields = "__all__"


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    form = QuestionModelForm
    inlines = [
        AnswerInline,
    ]
    extra = 2


class QuizAdmin(nested_admin.NestedModelAdmin):
    form = QuizModelForm
    inlines = [
        QuestionInline,
    ]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]


class ResponseInline(admin.TabularInline):
    model = Response


class QuizTakersAdmin(admin.ModelAdmin):
    inlines = [
        ResponseInline,
    ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizTakers, QuizTakersAdmin)
admin.site.register(Response)
