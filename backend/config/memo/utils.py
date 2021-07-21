from datetime import datetime
from .models import Memo


def insert_memo_db(request, data):
    content = data.validated_data['content']
    today = datetime.today()
    obj = Memo.objects.create(content=content, created_at=today,
                              updated_at=today)
    obj.save()


def update_memo_db(request, data):
    memo_id = request.query_params['id']
    obj = Memo.objects.get(id=memo_id)
    obj.updated_at = datetime.today()
    if 'content' in data.validated_data:
        obj.content = data.validated_data['content']
    obj.updated_at = datetime.today()
    obj.save()
