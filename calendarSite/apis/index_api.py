from django.http import JsonResponse
from calendarSite.models import Task


def get_tasks(request):
    subject_id = '0'
    task_id = '0'
    if 'subject' in request.GET:
      subject_id = request.GET['subject']

    if 'task' in request.GET:
      task_id = request.GET['task']
    
    response_data = {
        "subject_id": subject_id,
        "task_id":task_id,
        "tasks": [],
        "datas": [],
        "task":'0',
    }
    objs = Task.objects.filter(subject_id=subject_id).all()
    for obj in objs:
        response_data["tasks"].append(to_dict(obj))

    if task_id!= '0':
        task = Task.objects.get(id=task_id)
        response_data["task"]=(to_detail_dict(task))

    return JsonResponse(response_data)



def to_dict(data):

    return {"id":data.id,"subject": data.subject_id.name, "task": data.name,"updated_at":data.updated_at}

def to_detail_dict(data):
  
    return {
        "id":data.id,
        "subject": data.subject_id.name,
        "task": data.name,
        "contents":data.contents,
        "author":data.author,
        "created_at":data.created_at,
        "updated_at":data.updated_at,
    }
