from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if(len(post_data['title']) < 2):
            errors['title'] = "Title must be atleast 3 characters"
        if(len(post_data['network']) < 3):
            errors['network'] = "Network must be atleast 3 characters"    
        if(len(post_data['desc']) < 3):
            errors['desc'] = "Description must be atleast 10 characters" 
        return errors


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.CharField(max_length=45)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 