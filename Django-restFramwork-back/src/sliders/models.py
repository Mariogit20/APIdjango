from django.db import models

# Create your models here.
class Slider(models.Model):
    # image , description , titre
    titre = models.CharField(max_length=100)
    description = models.TextField()
    # prix = models.DecimalField(max_digits=10,decimal_places=2)
    # image = models.ImageField(upload_to="static/image/produits")
    image = models.ImageField(upload_to="static/image/sliders")    
    # date_ajout = models.DateTimeField(auto_now_add=True)
    
    
    