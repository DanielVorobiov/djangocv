from django.db import models

# Create your models here.


class Person(models.Model):
    class Genders(models.TextChoices):
        MALE = "male"
        FEMALE = "female"

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(choices=Genders.choices, max_length=6)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    about = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Education(models.Model):
    class Level(models.TextChoices):
        HIGH_SCHOOL = "High School"
        COLLEGE = "College"
        UNIVERSITY = "University"
        OTHER = "Other"

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    level = models.CharField(choices=Level.choices, max_length=16)
    institution = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)


class Experience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)


class Achievement(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    year = models.IntegerField()
