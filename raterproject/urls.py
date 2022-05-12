from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from raterprojectapi.views import register_user, login_user
from raterprojectapi.views.CategoryView import CategoryView
from raterprojectapi.views.GameRatingView import GRatingView
from raterprojectapi.views.GameReviewView import GameReviewView
from raterprojectapi.views.GameView import GameView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')
router.register(r'gamereviews', GameReviewView, 'gamereview')
router.register(r'gameratings', GRatingView, 'gamerating')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]