import folium
import json

from django.http import HttpResponseNotFound, request
from django.shortcuts import render
from .models import PokemonEntity, Pokemon
from django.utils.timezone import localtime

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_entity = PokemonEntity.objects.filter(appeared_at__lte=localtime(), disappeared_at__gte=localtime())
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for entity in pokemons_entity:   
        add_pokemon(folium_map, entity.lat, entity.lon, request.build_absolute_uri(entity.pokemon.image.url))

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.pk,
            'img_url': request.build_absolute_uri(pokemon.image.url),
            'title_ru':pokemon.title
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon_db = Pokemon.objects.get(pk=pokemon_id)
    try:
        child = pokemon_db.childs.get()
    except:
        print('no childs')
    pokemon = {"pokemon_id": pokemon_id,
               'img_url':f'{request.build_absolute_uri(pokemon_db.image.url)}',
               'title_ru':pokemon_db.title,
               'description':pokemon_db.description,
               'title_en':pokemon_db.title_en,
               'title_jp':pokemon_db.title_jp,           
               }
    if pokemon_db.parent:
        pokemon['previous_evolution'] =  {"title_ru": pokemon_db.parent.title,
                                          "pokemon_id": pokemon_db.parent.pk,
                                          "img_url": f'{request.build_absolute_uri(pokemon_db.parent.image.url)}'
                                          }
    try:
        child = pokemon_db.childs.get()
        pokemon['next_evolution'] =  {"title_ru": child.title,
                                      "pokemon_id": child.pk,
                                      "img_url": f'{request.build_absolute_uri(child.image.url)}'
                                      }       
    except:
        print('no childs')           
            
    pokemons_entity = PokemonEntity.objects.filter(pokemon=pokemon_id, appeared_at__lte=localtime(), disappeared_at__gte=localtime())
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in pokemons_entity:  
        add_pokemon(folium_map, entity.lat, entity.lon, request.build_absolute_uri(entity.pokemon.image.url))    
     

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
