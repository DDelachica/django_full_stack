from django.db import models
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not postData['fname'].isalpha():
            errors['fname'] = "First name cannot have numbers"
        if not postData['lname'].isalpha():
            errors['lname'] = "Last name cannot have numbers"
        if not email_checker.match(postData['email']):    
            errors['email'] = ("Invalid email address!")
        if len(postData['fname']) < 2:
            errors["fname"] = "First name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last name should be at least 2 characters"
        if len(postData['pw']) < 8:
            errors['pw'] = "Password should be at least 8 characters"
        if postData['pw'] != postData['confpw']:
            errors['pw'] = 'Password and Confirm Password do not match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = UserManager()
