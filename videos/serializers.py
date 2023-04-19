from rest_framework import serializers
from videos.models import Video
from videos.validator import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    def validate(self, data):
        if not titulo_valido(data['titulo']):
            raise serializers.ValidationError({'titulo': 'O titulo e muito pequeno!'})
        
        #if not descricao_valida(data['descricao']):
        #    raise serializers.ValidationError({'descricao': 'A descricao do video e muito pequena!'})
        
        if not url_valida(data['url']):
            raise serializers.ValidationError({'url': 'A url e invalida!'})
        
        return data

class VideoSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    def validate(self, data):
        if not titulo_valido(data['titulo']):
            raise serializers.ValidationError({'titulo': 'O titulo e muito pequeno!'})
        
        if not descricao_valida(data['descricao']):
            raise serializers.ValidationError({'descricao': 'A descricao do video e muito pequena!'})
        
        if not url_valida(data['url']):
            raise serializers.ValidationError({'url': 'A url e invalida!'})
        
        return data
