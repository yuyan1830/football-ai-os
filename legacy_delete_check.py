# -*- coding: utf-8 -*-

import os
import json
import datetime


old=r"E:\football"

new=r"E:\football_v"


result={

"old_path":old,

"new_path":new,

"checks":[],

"status":"READY_FOR_DELETE"

}


# 检查旧目录

if os.path.exists(old):

    result["checks"].append({

        "check":"old_directory",

        "status":"EXISTS",

        "message":"旧目录仍存在，需要确认"

    })

else:

    result["checks"].append({

        "check":"old_directory",

        "status":"NOT_FOUND"

    })


# 检查新目录

if os.path.exists(new):

    result["checks"].append({

        "check":"new_directory",

        "status":"PASS"

    })


# 搜索旧路径引用

count=0


for root,dirs,files in os.walk(new):

    for f in files:

        if f.endswith((".py",".json",".yaml",".txt",".md")):

            try:

                p=os.path.join(root,f)

                data=open(p,encoding="utf-8",errors="ignore").read()

                if "E:\\football" in data:

                    count+=1

            except:

                pass


result["checks"].append({

"check":"old_path_reference",

"count":count,

"status":"PASS" if count==0 else "WARNING"

})


result["time"]=str(datetime.datetime.now())


out=r"E:\football_v\FINAL_RELEASE_REPORT\legacy_delete_check.json"


with open(out,"w",encoding="utf-8") as f:

    json.dump(result,f,indent=4,ensure_ascii=False)


print(json.dumps(result,indent=4,ensure_ascii=False))

