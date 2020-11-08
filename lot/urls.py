from django.urls import path
from .views import LotViews,LotPutDelete

urlpatterns = [
    #path('price/', PriceViews.as_view()),
    #path('category/', CategoryViews.as_view()),
    path('lot/', LotViews.as_view()),
    path('lot/<int:id>', LotPutDelete.as_view()),
    path('lot/delete/<int:id>', LotPutDelete.as_view()),
]
