from datetime import timedelta, datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from taggit.managers import TaggableManager
from .helpers import unique_slugify


class Difficulty(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Difficulties'


class Category(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Profile(AbstractUser):
    is_author = models.BooleanField(default=False)
    # pass


class Course(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='courses/thumbnails/')
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)
    category = models.ManyToManyField(Category, default=[1])
    difficulty = models.ForeignKey(Difficulty, models.SET_NULL, null=True, default=1)
    tags = TaggableManager()
    total_users = models.PositiveIntegerField(default=0, null=True, blank=True)
    rank = models.PositiveSmallIntegerField(default=0)
    # How many people ranked the course
    ranked_by_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField()

    @property
    def course_duration(self):
        lessons = self.lessons.all()
        s = timedelta(seconds=0)
        for lesson in lessons:
            s += lesson.duration
        return s

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='lessons')
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()
    duration = models.DurationField(default=timedelta(minutes=20))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    order_number = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Lesson, self).save(*args, **kwargs)
