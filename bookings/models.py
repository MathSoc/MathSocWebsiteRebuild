from django.db import models

class BookingRequest(models.Model):
    REQUESTED_STATUS = 1
    ACCEPTED_STATUS = 2
    REJECTED_STATUS = 3
    STATUS_CHOICES = (
        (REQUESTED_STATUS, 'Requested'),
        (ACCEPTED_STATUS, 'Accepted'),
        (REJECTED_STATUS, 'Rejected'),
    )

    calendar_id   = models.CharField(max_length=256)
    calendar      = models.CharField(max_length=256)
    requesting_id = models.CharField(max_length=16)
    contact_name  = models.CharField(max_length=256)
    contact_email = models.CharField(max_length=256)
    contact_phone = models.CharField(max_length=256)
    organisation  = models.CharField(max_length=256)
    event_name    = models.CharField(max_length=256)
    status        = models.IntegerField(choices=STATUS_CHOICES, default=REQUESTED_STATUS)
    start         = models.DateTimeField()
    end           = models.DateTimeField()

    def __str__(self):
        return self.event_name
