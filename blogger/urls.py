from django.urls import path
from blogger import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
<<<<<<< HEAD
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup", views.register, name = "create_user"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
=======
>>>>>>> refs/remotes/origin/main
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e

urlpatterns = [
    path("signup", views.register, name = "create_user"),
    path("profile/<pk>/", views.BloggerProfile.as_view(), name="profile"),
    path('editar/<pk>/', views.BloggerUpdate.as_view(), name = "update_profile"),
<<<<<<< HEAD
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
<<<<<<< HEAD
]
>>>>>>> refs/remotes/origin/main
=======
]
>>>>>>> refs/remotes/origin/main
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e
