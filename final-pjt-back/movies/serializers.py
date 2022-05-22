from rest_framework import serializers
from .models import Movie, MovieComment



# 영화리스트
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'movie_id',)



# 영화상세정보
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'



# 영화코멘트입력
class GetCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieComment
        fields = '__all__'



# 영화코멘트
class MovieCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieComment
        fields = '__all__'