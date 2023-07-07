from django.db import models

# makermigrations = create changes and store in a file
# migrate = apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    # defining variable to send fields data to database and each variables are defined from name in html
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    # __str__ used to make string in human readable format. Whatever method name starts with double underscore they are termed as
    # super method
    def __str__(self):
        return self.name
