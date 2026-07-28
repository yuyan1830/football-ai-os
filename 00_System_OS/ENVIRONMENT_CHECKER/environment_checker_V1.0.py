
# -*- coding: utf-8 -*-

import sys
import json
from datetime import datetime


result={
"module":"Environment Checker",
"python":sys.version,
"status":"READY",
"time":str(datetime.now())
}

print(json.dumps(result,indent=4))
