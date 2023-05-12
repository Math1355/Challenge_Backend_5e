from rest_framework import serializers
from videos.models import Video, Categoria
from videos.validator import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    def validate(self, data):
        if not titulo_valido(data['titulo']):
            raise serializers.ValidationError({'titulo': 'O titulo e muito pequeno!'})
        
        if not url_valida(data['url']):
            raise serializers.ValidationError({'url': 'A url e invalida!'})
        
        return data

class VideoSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    def validate(self, data):
        if not titulo_valido(data['titulo']):
            raise serializers.ValidationError({'titulo': 'O titulo e muito pequeno!'})
        
        if not url_valida(data['url']):
            raise serializers.ValidationError({'url': 'A url e invalida!'})
        
        return data

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    def validate(self, data):
        if not titulo_categoria_valido(data['titulo']):
            raise serializers.ValidationError({'titulo': 'O campo titulo é obrigatório'})
        
        if not cor_categoria_valido(data['cor']):
            raise serializers.ValidationError({'cor': 'O campo cor é obrigatório'})
        
        return data
    
class CategoriaSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    def validate(self, data):
        if not titulo_categoria_valido(data['titulo']):
            raise serializers.ValidationError({'titulo': 'O campo titulo é obrigatório'})
        
        if not cor_categoria_valido(data['cor']):
            raise serializers.ValidationError({'cor': 'O campo cor é obrigatório'})
        
        return data
    
class ListaVideosCategoriaSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source='categoria.titulo')
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'url', 'categoria']
