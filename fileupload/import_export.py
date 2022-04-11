import os
import pandas
from CeleryTasks.settings import BASE_DIR
from todo.models import Todo
from django.contrib.auth.models import User

class SaveFileToDatabase:
    def __init__(self,user_id,url) -> None:
        self.url = url
        self.user_id = user_id
    
    def uplaod_to_database(self):
        try:
            user = User.objects.get(id=self.user_id)
        except User.DoesNotExist:
            return
        url = os.path.join(BASE_DIR, self.url.lstrip('/'))
        text = pandas.read_excel(url)
        data_as_dict = text.to_dict(orient="records")
        print(data_as_dict)
                
        records = list()

        for record in data_as_dict:
            todo = Todo(
                user=user,
                **record
                )
            records.append(todo)
        Todo.objects.bulk_create(records)