import requests
import json
import time

url = 'https://oapi.dingtalk.com/robot/send?access_token=00d00be016ed8a184627543a971d882f9f9c2c7b4da4a0a625bbbbe8ec80d1a8'

ups = ['37663924','437316738','390461123','517327498','254463269','163637592']

yday = time.time() - 3600 * 24 * 2 # 昨天
"""
test

obj = {
    "msgtype": "text", 
    "text": {
        "content": 'bilibili:'+'bilibili邀请你来摸鱼', 
    }
}

requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)
"""

# bilibili爬虫
for bid in ups:
    bili_url = 'https://api.bilibili.com/x/space/arc/search?mid='+bid+'&pn=1&ps=25&jsonp=jsonp'

    r = requests.get(bili_url)
    videos = r.json()['data']['list']['vlist']
    for video in videos:
        if(video['created']>yday):
            obj = {
                "msgtype": "link", 
                "link": {
                    "text": video['description']+'bilibili', 
                    "title": video['title'], 
                    "picUrl": 'http:'+video['pic'], 
                    "messageUrl": "https://www.bilibili.com/video/av%s" %(video['aid'])
                }
            }
            requests.post(url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(obj)
            )
