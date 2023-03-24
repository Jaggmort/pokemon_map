from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Изображение', null=True, blank=True)
    description = models.TextField('Описание', blank=True)
    title_en = models.CharField('Название на английском', blank=True, max_length=100)
    title_jp = models.CharField('Название на японском',blank=True, max_length=100)
    parent = models.ForeignKey('self', verbose_name= 'Из кого появился',on_delete=models.CASCADE, null=True, blank=True, related_name='childs')

    def __str__(self):
        return self.title
     
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE)    
    lat = models.FloatField('Широта', null=True)
    lon = models.FloatField('Долгота', null=True)
    appeared_at = models.DateTimeField('Появиться в', default=timezone.now(), null=True)
    disappeared_at = models.DateTimeField('Исчезнет в', default=timezone.now(), null=True)
    level = models.IntegerField('Уровень', default=0, null=True, blank=True)
    health = models.IntegerField('Жизни', default=0, null=True, blank=True)
    strength = models.IntegerField('Сила', default=0, null=True, blank=True)
    defence = models.IntegerField('Защита', default=0, null=True, blank=True)
    stamina = models.IntegerField('Выносливость', default=0, null=True, blank=True)

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