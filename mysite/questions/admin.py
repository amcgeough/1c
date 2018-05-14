from django.contrib import admin

from .models import Choice, Question, SubQuestion, SubChoice, Audit

import nested_admin


class AuditInLine(admin.TabularInline):
    model = Audit
    extra = 0

class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 0


class SubChoiceInline(nested_admin.NestedTabularInline):
    model = SubChoice
    extra = 0
    fields = ['choice_text', 'compliance_status', 'comment', 'action', 'score']
    title = 'choice'



class SubQuestionInline(nested_admin.NestedTabularInline):
    model = SubQuestion
    extra = 0
    inlines = [SubChoiceInline]

    # filter_vertical = ['sub_choice']
#    radio_fields = {"outcome": admin.VERTICAL}



class QuestionAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text', 'weight', 'choice_type', 'owner_email', 'user', 'information', 'file_upload', 'image_upload', 'footnote']}),
        ('Date information', {'fields': [('pub_date', 'frequency')], 'classes': ['expand'], 'description': 'This is the date the question will get published to end users'}),
    ]

    inlines = [ChoiceInline, SubQuestionInline]
    list_display = ('question_text', 'pub_date', 'owner_email', 'was_published_recently')
    #fields = ('question_text', 'pub_date', 'owner_email', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    actions_on_bottom = True
    actions_on_top = False
    date_hierarchy = 'pub_date'
    #list_display_links = ['owner_email']
    filter_horizontal = ['user']


class SubQuestionAdmin(nested_admin.NestedModelAdmin):
    inlines = [SubChoiceInline]
    list_filter = ['pub_date']


class AuditAdmin(nested_admin.NestedModelAdmin):
    model = Audit
    list_filter = ['start_date']
    filter_horizontal = ['owner', 'question']



admin.site.register(Question, QuestionAdmin)
admin.site.register(SubQuestion, SubQuestionAdmin)
admin.site.register(Audit, AuditAdmin)

