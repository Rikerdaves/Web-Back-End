from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (Hello, TarefasList, DetailUpdateDelete,
                    UserSignup)

urlpatters = [
    path('hello/', Hello.as_view(), name='hello'),
    
    # User
    path('signup', UserSignup.as_view(), name='signup'),

    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API Filmes
    path('tarefas', TarefasList.as_view(), name='create-tarefas'),
    path('tarefas/<int:pk>', DetailUpdateDelete.as_view(),
         name='detail-update-delete-filme')
]