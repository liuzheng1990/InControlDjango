from rest_framework import serializers
from .models import Tag, Diary


class TagField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name
    def to_internal_value(self, data):
        # data should be a str of the tag name
        return self.get_queryset().get_or_create(name=data)[0]


class DiarySerializer(serializers.ModelSerializer):
    tags = TagField(many=True, queryset=Tag.objects.all())
    
    class Meta:
        model = Diary
        fields = ("id", "author", "body", "created_at", "updated_at", "tags")
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    # def create(self, validated_data):
    #     tag_names = validated_data.pop("tags", [])
    #     new_diary = Diary.objects.create(**validated_data)
    #     new_diary.tags.set(self.get_tags_by_names(tag_names))
    #     new_diary.save()
    #     return new_diary

    # def update(self, instance, validated_data):
    #     tag_names = validated_data.pop("tags", [])
    #     instance.author = validated_data['author']
    #     instance.body = validated_data['body']
    #     instance.tags.set(self.get_tags_by_names(tag_names))
    #     return instance

    # def get_tags_by_names(self, tag_names):
    #     return [
    #         Tag.objects.get_or_create(name=tag_name) for
    #         tag_name in tag_names
    #     ]