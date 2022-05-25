from urllib import response
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, MovieComment
from rest_framework import serializers, status
from .serializers import *
from django.http import JsonResponse




@api_view(['GET'])
def now_playing_movies(request):
    if request.method == 'GET':
        if Movie.objects.exists():
            movie = get_list_or_404(Movie)
            serializer = MovieListSerializer(movie, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            results = requests.get('https://api.themoviedb.org/3/movie/now_playing?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR&page=1')
            results = results.json().get('results')
            for result in results:
                nowplaying_ids = result.get('id')
                nowplaying_detail = requests.get(f'https://api.themoviedb.org/3/movie/{nowplaying_ids}?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR').json()
                genres_list = nowplaying_detail.get('genres')
                genres_str = ' '.join(list(g['name'] for g in genres_list))
                now_movie = Movie(title=nowplaying_detail.get('title'), overview=nowplaying_detail.get('overview'), release_date=nowplaying_detail.get('release_date'), poster_path=nowplaying_detail.get('poster_path'),genres=genres_str, vote_average=nowplaying_detail.get('vote_average'), vote_count=nowplaying_detail.get('vote_count'), movie_num=nowplaying_detail.get('id'), popularity=nowplaying_detail.get('popularity'))
                if not Movie.objects.filter(title=now_movie.title):
                    now_movie.save()
            movie = get_list_or_404(Movie)
            serializer = MovieListSerializer(movie, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)





# client에서 영화 id 보내주면 해당하는 영화의 detail정보 db에 저장 안하고 json파일 반환
# @api_view(['GET'])
# def movie_detail(request, movie_num):
#     if request.method == 'GET':
#         result = requests.get(f'https://api.themoviedb.org/3/movie/{movie_num}?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR')
#         result = result.json()
#         return JsonResponse(result, status=status.HTTP_200_OK, safe=False)
@api_view(['GET'])
def movie_detail(request, movie_num):
    if request.method == 'GET':
        if Movie.objects.filter(movie_num=movie_num).exists():
            movie = get_object_or_404(Movie, movie_num=movie_num)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            result = requests.get(f'https://api.themoviedb.org/3/movie/{movie_num}?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR')
            result = result.json()
            genres_list = result.get('genres')
            genres_str = ' '.join(list(g['name'] for g in genres_list))
            detail = Movie(title=result.get('title'), overview=result.get('overview'), release_date=result.get('release_date'), poster_path=result.get('poster_path'),genres=genres_str, vote_average=result.get('vote_average'), vote_count=result.get('vote_count'), movie_num=result.get('id'), popularity=result.get('popularity'))
            detail.save()
            movie = get_object_or_404(Movie, movie_num=movie_num)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)









# 영화검색결과
@api_view(['POST'])
def search(request):
    if request.method == 'POST':
        query = request.data.get('searchdata')
        result = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR&query={query}&page=1&include_adult=false')
        result = result.json().get('results')
        return JsonResponse(result, status=status.HTTP_200_OK, safe=False)






# ----------------------------------------------------------------





# @api_view(['GET'])
# def comment_list(request):
#     comments = get_list_or_404(MovieComment)
#     serializer = MovieCommentSerializer(comments, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'DELETE', 'PUT'])
# def comment_detail(request, comment_pk):
#     comment = get_object_or_404(MovieComment, pk=comment_pk)
    
#     if request.method == 'GET':
#         serializer = MovieCommentSerializer(comment)
#         return Response(serializer.data) 

#     elif request.method == 'DELETE':
#         comment.delete()
#         data = {
#             'delete': f'데이터 {comment_pk}번이 삭제되었습니다.',
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = MovieCommentSerializer(comment, request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)



@api_view(['PUT', 'DELETE'])
def comment_detail(request, movie_num, comment_pk):
    movie = get_object_or_404(Movie, movie_num=movie_num)
    comment = get_object_or_404(MovieComment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = MovieCommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = movie.comments.all()
                serializer = MovieCommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = movie.comments.all()
            serializer = MovieCommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()



# 댓글 작성, 댓글 목록 불러오기
@api_view(['POST', 'GET'])
def movie_comment(request, movie_num):
    movie = get_object_or_404(Movie, movie_num=movie_num)
    if request.method =='POST':
        rank = request.data.get('rank')
        content = request.data.get('content')
        comment = MovieComment(movie=movie, rank=rank, content=content, user=request.user, movie_num=movie_num)
        comment.save()
        serializer = MovieCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = MovieComment.objects.all().filter(movie_num=movie_num)
        serializer = MovieCommentSerializer(comments, many=True)
        return Response(serializer.data)


# ==================================================================

@api_view(['POST'])
def like_movie(request, movie_num):
    movie = get_object_or_404(Movie, movie_num=movie_num)
    user = request.user
    if movie.movie_like.filter(pk=user.pk).exists():
        movie.movie_like.remove(user)
        movie.like_count -= 1
        movie.save()
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.movie_like.add(user)
        movie.like_count += 1
        movie.save()
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def my_popular_movie(request):
    movies = Movie.objects.order_by('-like_count')[:23]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def my_recommend_movie(request):
#     user = request.user
#     for other in movies