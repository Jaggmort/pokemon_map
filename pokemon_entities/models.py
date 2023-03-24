from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Изображение', null=True, blank=True)
    description = models.TextField('Описание', blank=True)
    title_en = models.CharField('Название на английском', blank=True, max_length=100)
    title_jp = models.CharField('Название на японском',blank=True, max_length=100)
    parent = models.ForeignKey('self', verbose_name= 'Из кого появился',on_delete=models.SET_NULL, null=True, blank=True, related_name='childs')

    def __str__(self):
        return self.title
     
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE, related_name='specified_pokemon')    
    lat = models.FloatField('Широта', null=True)
    lon = models.FloatField('Долгота', null=True)
    appeared_at = models.DateTimeField('Появиться в', null=True)
    disappeared_at = models.DateTimeField('Исчезнет в', null=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Жизни', null=True, blank=True)
    strength = models.IntegerField('Сила', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)     