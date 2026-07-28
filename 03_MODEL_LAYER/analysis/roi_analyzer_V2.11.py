
import json
import datetime


def roi(odds,result):

    if result=="WIN":

        return odds-1

    return -1



data={

"version":
"ROI_ANALYZER_V2.11",

"time":
str(datetime.datetime.now()),


"sample":

{

"odds":1.85,

"result":"WIN",

"profit":roi(1.85,"WIN"),

"roi":85

},


"status":"READY"

}


print(json.dumps(data,indent=4))


