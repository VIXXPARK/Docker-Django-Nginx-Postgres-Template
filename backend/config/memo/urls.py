from django.urls import path
from .views import MemoViewSet

memo_list = MemoViewSet.as_view({"get": "list", "post": "create"})
memo_detail = MemoViewSet.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"})
urlpatterns = [
    path("memo", memo_list, name="memo_list"),
    path("memo/<int:pk>", memo_detail, name="memo_detail"),
    path("memo/update/", memo_detail, name="memo_update"),
    path('memo/delete/<int:pk>', memo_detail, name="memo_delete")
]
