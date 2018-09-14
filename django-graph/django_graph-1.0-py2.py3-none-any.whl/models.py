from django.db import models


# Create your models here.
class Endpoint(models.Model):
    endpoint = models.CharField(max_length=255)
    ts = models.IntegerField()
    t_create = models.DateTimeField(editable=False)
    t_modify = models.DateTimeField()

    class Meta:
        app_label = "graph"
        db_table = "endpoint"


class Counter(models.Model):
    id = models.AutoField(primary_key=True)
    counter = models.CharField(max_length=255, null=False)
    step = models.IntegerField()
    type = models.CharField(max_length=16, null=False)
    ts = models.IntegerField()
    t_create = models.DateTimeField(editable=False)
    t_modify = models.DateTimeField()
    endpoint_id = models.IntegerField()
    endpoint = models.ForeignKey(Endpoint, related_name='counters', on_delete=models.CASCADE)

    class Meta:
        app_label = "graph"
        db_table = "endpoint_counter"


class Tag(models.Model):
    tag = models.CharField(max_length=255, null=False)
    ts = models.IntegerField()
    t_create = models.DateTimeField(editable=False)
    t_modify = models.DateTimeField()
    endpoint_id = models.IntegerField()
    endpoint = models.ForeignKey(Endpoint, related_name='tags', on_delete=models.CASCADE)

    class Meta:
        app_label = "graph"
        db_table = "tag_endpoint"
