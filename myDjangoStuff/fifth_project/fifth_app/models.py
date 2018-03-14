from django.db import models

class UserInfo(models.Model):
    firstName = models.CharField(max_length=246)
    lastName = models.CharField(max_length=246)
    email = models.EmailField(uniquq=True)

    def __str__(self):
        return "First name: {} \n Last name: {} \n Email: {}".format(
        firstName, lastName, email)
