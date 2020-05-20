from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    # Setting 'blank=True' tells the field is optional. This can be used 
    # with the other fields as well.
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
