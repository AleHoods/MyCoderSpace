from django.urls import path
from MyCoderSpace import views

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path("pages", views.BlogList.as_view(), name = "home"),
=======
=======
>>>>>>> refs/remotes/origin/main
    path("login/", views.BlogLogin.as_view(), name = "login"),
<<<<<<< HEAD
    path("pages", views.BlogList.as_view(), name = "home"),
=======
    path("", views.BlogList.as_view(), name = "home"),
>>>>>>> refs/remotes/origin/main
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e
    path("create/", views.BlogCreate.as_view(), name = "create"),
    path("pages/<pk>/", views.BlogDetail.as_view(), name = "detail"),
    path("update/<pk>/", views.BlogUpdate.as_view(), name = "update"),
    path("delete/<pk>/", views.BlogDelete.as_view(), name = "delete"),
<<<<<<< HEAD
<<<<<<< HEAD
    path('About/', views.About, name="about"),
    path('', views.Home, name="principal"),
]

=======
    path("logout", views.BlogLogout.as_view(), name='logout'),
<<<<<<< HEAD
    path('About/', views.About, name="about"),
    path('', views.Home, name="principal"),
]

=======
    path('About/', views.About, name="about")
]
>>>>>>> refs/remotes/origin/main
=======
    path("logout", views.BlogLogout.as_view(), name='logout'),
    path('About/', views.About, name="about")
]
>>>>>>> refs/remotes/origin/main
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e
