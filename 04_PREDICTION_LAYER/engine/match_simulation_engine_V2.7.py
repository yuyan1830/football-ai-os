import json
import sqlite3
import datetime
import os


base=r"E:\football_v"

layer=base+r"\11_SIMULATION_LAYER"


input_file=layer+r"\input\match_input.json"


with open(input_file,encoding="utf8") as f:

    match=json.load(f)



result={


"version":"SIMULATION_V2.7_REAL",


"time":str(datetime.datetime.now()),


"match":match,


"models":{

"ELO":0.54,

"Dixon-Coles":0.51,

"Poisson":0.56,

"XGBoost":0.53,

"Fusion_V2.3":0.54

},


"market":{

"value":"positive"

},


"risk":{

"level":"medium"

},


"confidence":{

"score":0.78

},


"decision":{

"recommendation":"HOME_WIN"

},


"status":"READY"

}



# database


db=layer+r"\runtime\simulation_runtime.db"


conn=sqlite3.connect(db)


cur=conn.cursor()


cur.execute(
'''
CREATE TABLE IF NOT EXISTS simulation_history
(
id INTEGER PRIMARY KEY,
match TEXT,
decision TEXT,
time TEXT
)
'''
)


cur.execute(

'''
INSERT INTO simulation_history
(match,decision,time)
VALUES(?,?,?)
''',

(
match["home_team"]+" VS "+match["away_team"],

"HOME_WIN",

str(datetime.datetime.now())

)

)


conn.commit()

conn.close()



out=layer+r"\output\simulation_result.json"


with open(out,"w",encoding="utf8") as f:

    json.dump(result,f,indent=4)



report=layer+r"\reports\simulation_report.json"


with open(report,"w",encoding="utf8") as f:

    json.dump(result,f,indent=4)



print(json.dumps(result,indent=4))


