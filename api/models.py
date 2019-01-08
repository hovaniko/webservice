# api/models.py

from django.db import models


class docs(models.Model):
    """This class represents the bucketlist model."""
    client_id = models.CharField(max_length=255, blank=False)
    doc_name = models.CharField(max_length=255, blank=True)
    doc_type = models.CharField(max_length=255, blank=True)
    digitalized_by = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.client_id)
