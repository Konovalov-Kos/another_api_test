from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')
urlpatterns = router.urls

# from django.urls import path
#
# from .views import ArticleView
# # from .views import SingleArticleView
#
# app_name = 'articles'
#
# urlpatterns = [
#     path('articles/', ArticleView.as_view({'get': 'list'})),
#     # path('articles/<int:pk>', SingleArticleView.as_view()),
#     path('articles/<int:pk>', ArticleView.as_view({'get': 'retrieve'})),
# ]