from django import template
from ..models import Course

register = template.Library()


@register.filter
def is_enrolled(course_id, user_id):
    course = Course.objects.get(pk=course_id)
    return course.users.filter(user_id=user_id).exists()