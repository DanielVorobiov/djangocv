from django.shortcuts import render

from cv.models import Achievement, Education, Experience, Person


def index(request):
    person = Person.objects.first()
    experience = Experience.objects.filter(person=person).order_by("-start_date")
    education = Education.objects.filter(person=person).order_by("-start_date")
    achievement = Achievement.objects.filter(person=person).order_by("-year")
    return render(
        request,
        "cv.html",
        context={
            "person": person,
            "experience_list": experience,
            "education_list": education,
            "achievement_list": achievement,
        },
    )
