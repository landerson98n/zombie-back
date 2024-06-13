from rest_framework import serializers
from base.models import Survivor, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'quantity']

class SurvivorSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Survivor
        fields = ['id', 'name', 'age', 'sex', 'latitude', 'longitude', 'infected', 'is_infected' ,'items', 'created']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        survivor = Survivor.objects.create(**validated_data)
        for item in items_data:
            Item.objects.create(survivor=survivor, **item)
        return survivor
    
    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if items_data is not None:
            for item_data in items_data:
                Item.objects.update_or_create(
                    survivor=instance,
                    name=item_data.get('name'),
                    defaults={'quantity': item_data.get('quantity')}
                )

        return instance