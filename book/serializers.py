from rest_framework import serializers

from book.models import BookInfo


class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    pub_date = serializers.DateField()
    readcount = serializers.IntegerField()
    commentcount = serializers.IntegerField()
    def validate_readcount(self,value):
        if value<0:
            raise serializers.ValidationError('readcount can not be negative')


    def validate(self,data):
        readcount = data.get('readcount')
        commentcount = data.get('commentcount')
        if commentcount>readcount:
            raise serializers.ValidationError('comment can not greater than read')
        return data

    def create(self, validated_data):
        return BookInfo.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data('name',instance.name)
        instance.pub_date = validated_data('pub_date',instance.pub_date)
        instance.readcount = validated_data('readcount',instance.readcount)
        instance.commentcount = validated_data('commentcount',instance.commentcount)
        instance.save()
        return instance


class PeopleInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    password = serializers.CharField()
    description = serializers.CharField()
    is_delete=serializers.BooleanField()
    # book_id=serializers.IntegerField()

class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields='__all__'
