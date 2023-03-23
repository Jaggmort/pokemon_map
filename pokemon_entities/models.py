from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)    
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=timezone.now())
    disappeared_at = models.DateTimeField(default=timezone.now())
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)

    def get_lat(self):
        return self.lat
    
    def get_lon(self):
        return self.lon

    def get_image_url(self):
        return "{0}{1}".format('http://127.0.0.1:8000', self.pokemon.image.url)        

    def get_pokemon_title(self):
        return  self.pokemon.title
    
    def get_appear_at(self):
        return self.appeared_at
    
    def get_disappeared_at(self):
        return self.disappeared_at

    def get_id(self):
        return self.pokemon.pk        