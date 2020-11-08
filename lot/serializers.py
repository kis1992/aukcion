from rest_framework import serializers
from lot import models


class RecursiveSerializers(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        fields = ('id', 'step_price', 'final_price', 'auto_price', 'last_owner')


class CategorySerializers(serializers.ModelSerializer):
    children = RecursiveSerializers(many=True)

    class Meta:
        model = models.Category
        fields = ('id', 'category_name', 'parent', 'children')



class CategoryForLotSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'category_name','slug')


class LotSerializers(serializers.ModelSerializer):
    price = PriceSerializers
    #category = CategoryForLotSerializers(many=True)
    
    class Meta:
        model = models.Lot
        fields = '__all__'