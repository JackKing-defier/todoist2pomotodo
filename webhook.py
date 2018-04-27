import todoist
from todoist_api import *
from pomoto_api import *

import datetime,pytz,pprint
tz = pytz.timezone('Asia/Shanghai')
today_dttm=datetime.datetime.now(tz)
today_date_str=today_dttm.date()

todoist_token = 'd5d6e2718a9f2d3b6c34c57ae389bd763a483f99' #todoist api接口的个人访问密钥
pomotodo_token = 'Q3oWHvXZgB1c1LzzLyDhTlq3TVuYs5jAcDQ8iMvb05jGBnCM40GHW8oghfyrjYUPOBOSsh2BP15M0hNZZou9mdIXafyvyZCC' #pomotodo api接口的个人访问密钥
api = todoist.TodoistAPI(todoist_token)

todaytasks = get_todaytask(api)
add_todo_from_todoist(todaytasks,pomotodo_token)

