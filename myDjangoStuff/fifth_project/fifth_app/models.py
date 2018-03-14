from django.db import models

class UserInfo(models.Model):
    firstName = models.CharField(max_length=246)
    lastName = models.CharField(max_length=246)
    email = models.EmailField(unique=True)

    def __str__(self):
        return "First name: {} \n Last name: {} \n Email: {}".format(
            self.firstName, self.lastName, self.email)

    def class_name():
        return "User Info"
