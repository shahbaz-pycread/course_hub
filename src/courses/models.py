from django.db import models

# Create your models here.

class AccessRequirement(models.TextChoices):
    ANYONE = "any","Anyone"# any will be store in the database, Anyone will be shown to the user
    EMAIL_REQUIRED = "email_required", "Email Required"
    

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub","Published"# pub will be store in the database, Published will be shown to the user
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"
    
def handle_upload(instance, filename): # for handling file and image upload    
    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    access = models.CharField(max_length=15, 
                              choices=AccessRequirement.choices, 
                              default=AccessRequirement.EMAIL_REQUIRED)
    status = models.CharField(max_length=10, 
                              choices=PublishStatus.choices, 
                              default=PublishStatus.DRAFT)
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED