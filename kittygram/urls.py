 # ВЕРСИЯ 4 для роутера 

from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

# Создаётся роутер, экземпляр класса
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами: URL-префикс и название вьюсета
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]






# # ВЕРСИЯ 3 для дженерика 
# from django.urls import path

# from cats.views import CatList, CatDetail

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]





# ВЕРСИЯ 2 Обновлённый urls.py для вью на классах
# from django.urls import path

# from cats.views import APICat

# urlpatterns = [
#     path('cats/', APICat.as_view()),
# ]





# ВЕРСИЯ 1 urls.py для вью на функциях
# from django.urls import path

# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]


