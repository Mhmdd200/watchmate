from django.urls import path,include # type: ignore
#from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import Watchlist_AV,WatchlistDetail_AV,StreamPlatform_VS
#from watchlist_app.api.views import StreamPlatform_AV, StreamPlatformDetail
from watchlist_app.api.views import ReviewList_AV, ReviewDetail_AV, ReviewCreate_AV
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatform_VS, basename='Stream')
urlpatterns = [
    path('list/', Watchlist_AV.as_view(), name='watchlist'),
    path('list/<int:pk>', WatchlistDetail_AV.as_view(), name='watchlist_detail'),
    #path('stream/', StreamPlatform_AV.as_view(), name='stream_list'),
    #path('stream/<int:pk>', StreamPlatformDetail.as_view(), name='stream_detail'),
    path('', include(router.urls)),
    path('<int:pk>/reviews', ReviewList_AV.as_view(), name='review'),
    path('review/<int:pk>', ReviewDetail_AV.as_view(), name='review_detail'),
    path('<int:pk>/review-create', ReviewCreate_AV.as_view(), name="review_create")
]