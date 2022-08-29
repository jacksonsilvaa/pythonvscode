from django.db import models
from uuid import uuid4

# Create your models here.

class hqs(models.Model):
    id_hq = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    estado = models.CharField(max_length=50)
    paginas = models.IntegerField()
    selo = models.CharField(max_length=100)
    
