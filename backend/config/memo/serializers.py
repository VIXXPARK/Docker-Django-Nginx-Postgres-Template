from rest_framework import serializers


class MemoSerializer(serializers.Serializer):
    content = serializers.CharField(required=False)
    
    def update(self, instance, validated_data):
        instance.content = validated_data('title', instance.content)
        instance.save()
        return instance
