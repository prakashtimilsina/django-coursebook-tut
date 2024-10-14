from django.db import models

class AccessRequired(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Email required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    DRAFT = "draft", "Draft"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    access = models.CharField(max_length=10, choices=AccessRequired.choices, default=AccessRequired.EMAIL_REQUIRED)
    status = models.CharField(max_length=10, choices=PublishStatus.choices, default=PublishStatus.DRAFT)


@property
def is_published(self):
    return self.status == PublishStatus.PUBLISHED