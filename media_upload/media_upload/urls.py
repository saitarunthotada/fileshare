from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from uploader.views import MediaFileDeleteView, MediaFileUploadView, SuperuserMediaFileList, UserLoginView, UserRegisterView
from uploader.serializers import MediaFileList

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    #for_ops
    path('ops/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('ops/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('ops/upload-file/', MediaFileUploadView.as_view(), name='file-upload'),
    path('ops/uploads/', MediaFileList.as_view(), name='mediafile-list'),
    path('ops/mediafiles/<int:pk>/delete/', MediaFileDeleteView.as_view(), name='mediafile-delete'),

    #for_users
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('users/login/', UserLoginView.as_view(), name='user-login'),
    path('users/downloads/', SuperuserMediaFileList.as_view(), name='superuser-mediafile-list'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

