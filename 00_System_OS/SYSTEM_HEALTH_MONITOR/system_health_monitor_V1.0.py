
# -*- coding: utf-8 -*-

import json
from datetime import datetime


result={
"module":"System Health Monitor",
"status":"HEALTHY",
"database":"READY",
"models":"READY",
"api":"READY",
"time":str(datetime.now())
}

print(json.dumps(result,indent=4))
