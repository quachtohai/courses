from django.contrib import admin
from django.utils.html import mark_safe
from django import forms
from django.template.response import TemplateResponse
from .models import Category, Course,Lesson, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from django.urls import path
from django.db.models import Count

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    
    class Meta:
        model = Lesson
        fields = '__all__'
        
class LessionAdmin(admin.ModelAdmin):
    form = LessonForm
    
    class Media:
        css = {
            'all': ('/static/css/main.css',)
        }
    
    list_display = ["id","subject","created_date","active"]

    readonly_fields = ["avatar"]
    
    def avatar(self, obj):
        return mark_safe("<img src = '/static/{img_url}' alt ='{alt}' width = 400px/>" \
            .format(img_url=obj.image.name, alt = obj.subject))
    

class CourseAppAdminSite(admin.AdminSite):
    site_header ="HE THONG QUAN LY KHOA HOC"
    
    def get_urls(self):
        return [
            path('course-stats/', self.course_stats)
        ] + super().get_urls()
    
    def course_stats(self, request):
        course_count = Course.objects.count()
        stats = Course.objects.annotate(lesson_count = Count('lessons')).values("id","subject","lesson_count")
        return TemplateResponse(request,'admin/course-stats.html',{
            'course_count' : course_count,
            'stats':stats
        } )
    
    
admin_site = CourseAppAdminSite('mycourse')

# admin.site.register(Category)
# admin.site.register(Course)
# admin.site.register(Lesson, LessionAdmin)
# admin.site.register(Tag)


admin_site.register(Category)
admin_site.register(Course)
admin_site.register(Lesson, LessionAdmin)
admin_site.register(Tag)



# Register your models here.
