from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Category, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CategorySerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = serializers.StringRelatedField() #read_only

    # Esse campo serve só para mostrar
    user = UserSerializer(read_only=True)

    #write_only = somente para escrita
    #source = O user_id serve para o campo do modelo
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'user', 'user_id')

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                       write_only=True,
                                                       source='categories',
                                                       many=True)
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('id', 'name', 'price', 'categories', 'categories_id')

#campos de leitura - serializar
#campos de escrita - deserializar
