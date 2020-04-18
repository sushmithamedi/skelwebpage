from django.urls import path,include
from . import views
urlpatterns = [
    path( 'signup/', views.SignUpView.as_view(), name="signup" ),
    path( 'aboutus/', views.AboutUsView.as_view(), name="aboutus" ),
    path('createblog/',views.CreateBlogView.as_view(),name="createblog")

]
