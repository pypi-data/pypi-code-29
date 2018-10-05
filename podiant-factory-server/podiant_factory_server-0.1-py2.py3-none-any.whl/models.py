from django.db import models
from . import query, settings


class Machine(models.Model):
    name = models.SlugField(max_length=50, unique=True, db_index=True)
    creator = models.ForeignKey(
        'auth.User',
        related_name='factory_machines',
        on_delete=models.CASCADE
    )

    key = models.CharField(max_length=64, db_index=True)

    def __str__(self):
        return self.name


class Operator(models.Model):
    machine = models.ForeignKey(
        Machine,
        related_name='operators',
        on_delete=models.CASCADE
    )

    namespace = models.SlugField(max_length=50, db_index=True)
    function = models.SlugField(max_length=50, db_index=True)
    url = models.URLField('URL', max_length=255)

    def __str__(self):
        return '%s.%s' % (self.namespace, self.function)

    class Meta:
        unique_together = ('function', 'namespace', 'machine')


class Bundle(models.Model):
    objects = query.BundleQuerySet.as_manager()

    def create_item(self, key, kind, mime_type=None):
        obj = Item(
            bundle=self,
            key=key,
            kind=kind,
            mime_type=mime_type
        )

        obj.full_clean()
        obj.save()

        return obj


class Item(models.Model):
    bundle = models.ForeignKey(
        Bundle,
        related_name='items',
        on_delete=models.CASCADE
    )

    key = models.SlugField(max_length=255, db_index=True)
    value = models.TextField(null=True, blank=True)
    kind = models.CharField(
        max_length=7,
        choices=[(k, k) for k in settings.BUNDLE_ITEM_KINDS]
    )

    mime_type = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        unique_together = ('key', 'bundle')


class Process(models.Model):
    input_bundle = models.ForeignKey(
        Bundle,
        on_delete=models.CASCADE
    )

    output_bundle = models.ForeignKey(
        Bundle,
        on_delete=models.CASCADE
    )

    meta = models.TextField()

    objects = query.ProcessQuerySet.as_manager()


class Tag(models.Model):
    process = models.ForeignKey(
        Process,
        related_name='tags',
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'process')


class Operation(models.Model):
    process = models.ForeignKey(
        Process,
        related_name='operations',
        on_delete=models.CASCADE
    )

    ordering = models.PositiveIntegerField(default=0)
    namespace = models.SlugField(max_length=50, db_index=True)
    function = models.SlugField(max_length=50, db_index=True)
    verbose_name = models.CharField(max_length=101)
    scheduling = models.CharField(
        max_length=7,
        choices=[(s, s) for s in settings.OPERATION_SCHEDULES],
        default='auto'
    )

    can_fail = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=[(s, s) for s in settings.OPERATION_STATUSES],
        default='pending'
    )

    progress = models.FloatField(null=True, default=None, blank=True)
    expires = models.DateTimeField(null=True, blank=True)

    objects = query.OperationQuerySet.as_manager()

    def __str__(self):
        return '%s.%s' % (self.namespace, self.function)

    class Meta:
        ordering = ('ordering',)


class Restriction(models.Model):
    operation = models.ForeignKey(
        Operation,
        related_name='restrictions',
        on_delete=models.CASCADE
    )

    kind = models.CharField(
        max_length=3,
        choices=(
            ('tag', 'tag')
        ),
        db_index=True
    )

    value = models.CharField(max_length=255, db_index=True)

    class Meta:
        unique_together = ('value', 'kind')


class Message(models.Model):
    operation = models.ForeignKey(
        Operation,
        related_name='messages',
        on_delete=models.CASCADE
    )

    kind = models.CharField(
        max_length=7,
        choices=[(k, k) for k in settings.MESSAGE_KINDS],
        db_index=True
    )

    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        unique_together = ('kind', 'operation')


class WorkRequest(models.Model):
    machine = models.ForeignKey(
        Machine,
        related_name='work_requests',
        on_delete=models.CASCADE
    )

    namespace = models.SlugField(max_length=50, db_index=True)
    function = models.SlugField(max_length=50, db_index=True)
    sent = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=8,
        choices=[(s, s) for s in settings.WORK_REQUEST_STATUSES],
        default='pending'
    )

    expires = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('sent',)
        get_latest_by = 'sent'
