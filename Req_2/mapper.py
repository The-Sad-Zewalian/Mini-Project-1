#!/usr/bin/python3

import json
import sys

"""maps the json object to:parent_id, controversiality and its intial count (1)
Args:
    json object
Returns:
    Standerd output line 
"""

for line in sys.stdin:
    try:
        Jobject = json.loads(line.encode('utf-8'))
        print("{}\t{}\t{}".format(Jobject['parent_id'],Jobject['controversiality'],'1'))
    except:
        None