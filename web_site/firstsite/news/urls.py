from django.urls import path
from .views import *

urlpatterns = [
    path("", NewsHome.as_view(), name="news_index"),
    # path("base/", base, name="news_index"),
    path("news/<slug:post_slug>/", ShowPosts.as_view(), name="news"),
    path('article/<slug:post_slug>/', ShowArticle.as_view(), name='article'),
    path('category/<slug:category_slug>/', HeadNewsCategory.as_view(), name='category'),
    path('hot_news/', ShowHotNews.as_view(), name='show_hot_news'),
    path("registration/", RegisterUser.as_view(), name="registration"),
    path('news/<slug:post_slug>/del_comment/<int>', del_comment_news, name='del_comment'),
    path("login/", LoginUser.as_view(), name="sign_in"),
    path("logout/", LogOutUser.as_view(), name="logout"),
    path('article/<slug:post_slug>/del_comment/<int>', del_comment_article, name='del_comment'),
    # path("", del_comment, name="del_comment"),
    # path("add/", add_comment, name="aaa"),

]
