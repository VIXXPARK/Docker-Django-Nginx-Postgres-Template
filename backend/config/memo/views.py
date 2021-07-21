from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from .serializers import MemoSerializer
from memo.models import Memo
from .utils import insert_memo_db, update_memo_db


class MemoViewSet(ModelViewSet):
    serializer_class = MemoSerializer
    queryset = Memo.objects.all()

    def create(self, request, *args, **kwargs):
        data = MemoSerializer(data=request.data)
        if not data.is_valid():
            return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
        insert_memo_db(request, data)
        return Response({'success': True})

    def update(self, request, *args, **kwargs):
        data = MemoSerializer(data=request.data)
        if not data.is_valid():
            return Response({'success': False, 'msg': data.errors}, status=status.HTTP_400_BAD_REQUEST)
        update_memo_db(request, data)
        return Response({'success': True})

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)
