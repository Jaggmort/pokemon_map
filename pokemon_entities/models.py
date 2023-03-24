from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
    title = models.TextField('Название')
    image = models.ImageField('Изображение', null=True)
    description = models.TextField('Описание', null=True)
    title_en = models.TextField('Название на английском', null=True)
    title_jp = models.TextField('Название на японском',null=True)
    parent = models.ForeignKey('self', verbose_name= 'Из кого появился',on_delete=models.CASCADE, null=True, related_name='child')

    def __str__(self):
        return self.title
     
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE)    
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Появиться в', default=timezone.now())
    disappeared_at = models.DateTimeField('Исчезнет в', default=timezone.now())
    level = models.IntegerField('Уровень', default=0)
    health = models.IntegerField('Жизни', default=0)
    strength = models.IntegerField('Сила', default=0)
    defence = models.IntegerField('Защита', default=0)
    stamina = models.IntegerField('Выносливость', default=0)

    def get_lat(self):
        return self.lat
    
    def get_lon(self):
        return self.lon      

    def get_pokemon_title(self):
        return  self.pokemon.title
    
    def get_appear_at(self):
        return self.appeared_at
    
    def get_disappeared_at(self):
        return self.disappeared_at

    def get_id(self):
        return self.pokemon.pk        