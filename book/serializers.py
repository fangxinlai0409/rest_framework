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

class PeopleInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    password = serializers.CharField()
    description = serializers.CharField()
    is_delete=serializers.BooleanField()
    # book_id=serializers.IntegerField()
