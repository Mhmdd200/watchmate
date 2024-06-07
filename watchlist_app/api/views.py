from watchlist_app.api.serializers import WatchlistSerializer,StreamPlatformSerializer,ReviewSerializer
from watchlist_app.models import Watchlist,StreamPlatform,Review
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework import status # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import mixins # type: ignore
from rest_framework import generics # type: ignore
class ReviewList_AV(generics.ListAPIView):
   #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetail_AV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
     
class ReviewCreate_AV(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        movie = Watchlist.objects.get(pk=pk)
        serializer.save(watchlist=movie)


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
class Watchlist_AV(APIView):
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
            return Response(serializer.errors)
class WatchlistDetail_AV(APIView):
    def get(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        try:
            serializer = WatchlistSerializer(movie)
            return Response(serializer.data)
        except movie.DoesNotExist:
            return Response({'Error movie not found'}, status = status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'Error editing the movie'}, status = status.HTTP_405_METHOD_NOT_ALLOWED)
    def delete(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete
        return Response({'Deleted'}, status = status.HTTP_202_ACCEPTED)
class StreamPlatform_AV(APIView):
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
        
       