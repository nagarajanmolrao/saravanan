from django.db import models
# Create your models here.


class Saravanan(models.Model):
    AV_AGENTS = (
        ('PNR', 'PNR'),
        ('NAR', 'ANMOL'),
        ('MAD', 'MADHU'),
        ('KAR', 'KARTHICK'),
    )
    avName = models.CharField(max_length=100)
    avlUsers = models.IntegerField(default=1)
    avlYears = models.IntegerField(default=1)
    avlKey = models.TextField(max_length=500, unique=True)
    avlEmail = models.CharField(max_length=100, default=' ')
    avAgent = models.CharField(max_length=3, choices=AV_AGENTS, default='NAR')
    avActivated = models.BooleanField(default=False)
    avClient = models.CharField(max_length=100, default=' ')
    avExpiry = models.CharField(max_length=100)
