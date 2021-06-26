from django.contrib import admin
from .models import *


class LessonsInline(admin.StackedInline):
    model = Lesson
    extra = 3
    exclude = ['slug']
    ordering = ['order_number']


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'enrollment_date']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['total_users',  'rank', 'ranked_by_count']
    inlines = [LessonsInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    # list_display = ['title', 'slug', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    pass


@admin.register(LessonCompletion)
class CompletionAdmin(admin.ModelAdmin):
    # list_display = ['title', 'slug', 'created', 'updated']
    # prepopulated_fields = {'slug': ('title',)}
    pass


@admin.register(LastLesson)
class LastLessonAdmin(admin.ModelAdmin):
    # list_display = ['title', 'slug', 'created', 'updated']
    # prepopulated_fields = {'slug': ('title',)}
    pass

