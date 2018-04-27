from todoist.api import TodoistAPI
# api = TodoistAPI('d5d6e2718a9f2d3b6c34c57ae389bd763a483f99')
import datetime
import pytz, datetime

def get_todaytask(api):
    tz = pytz.timezone('Asia/Shanghai')
    todaytask = []
    today_date = datetime.datetime.now().date()
    api.sync()
    items = api.items.state['items']
    for item in items:
        task_id = item.data['id']
        due_date_utc= item.data['due_date_utc']
        if due_date_utc is not None:
            task_date = datetime.datetime.strptime(due_date_utc[:],'%a %d %b %Y %H:%M:%S %z').replace(tzinfo=tz).date() #转换时间格式并调整时区
            if task_date==today_date: #筛选 今天 的任务
                date_added = datetime.datetime.strptime(item.data['date_added'][:],'%a %d %b %Y %H:%M:%S %z').replace(tzinfo=tz).isoformat()
                if item.data['priority'] in (3,4):
                    pin = True
                else:
                    pin = False
                todaytask+=[{"description":item.data['content'],'pin':pin}]
    return todaytask

# ,'created_at':date_added,'notice':item.data['labels'],'pin':pin

