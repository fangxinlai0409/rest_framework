from rest_framework import serializers
class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    pub_data = serializers.DateField()
    readcount = serializers.IntegerField()