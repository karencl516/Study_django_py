from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)
    foundation = models.IntegerField()

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=40)
    creator = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                                related_name="employees")
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.name