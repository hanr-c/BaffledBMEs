#username
username='spencergambrell@letu.edu'

#api
api_key= '83282F6C-1318-A031-7DD5-DE73ECC94486'

#sending message to
toNum= '+12817866186'
fromNum= ''

message= 'This is a test message'

import json, subprocess

request= {"messages" : [{"source":"rpi", "from":fromNum, "to":toNum, "body":message}]}
request=json.dumps(request)

cmd= "curl https://rest.clicksend.com/v3/sms/send -u " + username + ":" + api_key + " -H \"Content-Type: application/json\" -X POST --data-raw '" + request + "'"

p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
(output,err) = p.communicate()
print(output)