from watchlist_app.api.serializers import WatchlistSerializer,StreamPlatformSerializer,ReviewSerializer
from watchlist_app.models import Watchlist,StreamPlatform,Review
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from watchlist_app.api.permissions import IsAdminOrReadOnly, ReviewUserOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from user_app.api.pagination import WatchlistPagination

class ReviewList_AV(generics.ListAPIView):
   #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'valid']
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetail_AV(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'review-detail'
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    
    
class ReviewCreate_AV(generics.CreateAPIView):
    throttle_scope = 'review-create'
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist= watchlist, review_user = review_user)
        if review_queryset.exists():
            raise ValidationError("This watchlist have already been reviewed")
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating+serializer.validated_data['rating']) / 2
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        serializer.save(watchlist=watchlist, review_user = review_user)
'''class ReviewDetail_AV(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
class ReviewList_AV(mixins.ListModelMixin,mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)'''
class Watchlist_Test(generics.ListAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer  
    pagination_class = WatchlistPagination 
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['title','platform__name']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['avg_rating']


class Watchlist_AV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        movielist = Watchlist.objects.all()
        serializer = WatchlistSerializer(movielist,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = WatchlistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_403_FORBIDDEN)
class WatchlistDetail_AV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        try:
            serializer = WatchlistSerializer(movie)
            return Response(serializer.data)
        except movie.DoesNotExist:
            return Response({'Error movie not found'}, status = status.HTTP_403_FORBIDDEN)
    def put(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'Error editing the movie'}, status = status.HTTP_403_FORBIDDEN)
    def delete(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete
        return Response({'Deleted'}, status = status.HTTP_202_ACCEPTED)
    
class StreamPlatform_VS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
class StreamPlatform_AV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self,request):
        stream = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"Error saving it"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
class StreamPlatformDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self,request,pk):
        stream = StreamPlatform.objects.get(pk=pk)
        try:
            serializer = StreamPlatformSerializer(stream)
            return Response(serializer.data)
        except stream.DoesNotExist:
            return Response({"This streaming platform doesn't exist"},
                            status=status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"This platfrom can't be edited"}, status=status.HTTP_403_FORBIDDEN)
    def delete(self,request,pk):
        stream = StreamPlatform.objects.get(pk=pk)
        stream.delete
        return Response({'Done'},status = status.HTTP_202_ACCEPTED)
        

'''@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request,pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response( status = status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == 'PUT':
       movie = Movie.objects.get(pk=pk)
       serializer = MovieSerializer(movie,data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors)
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status = status.HTTP_404_NOT_FOUND)'''
        
       