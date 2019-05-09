import json


# data = json.loads(open('/home/sayone/Desktop/Test_Events/planbaker/static/country.json').read())
# # print(data)
# # for d in data:
# #     print(d['dial_code'].replace(" ","-"))
# choices=[(d['dial_code'],d['dial_code']) for d in json.loads(open('/home/sayone/Desktop/Test_Events/planbaker/static/country.json').read())]
# print(choices)

#Wed, 06 Feb 2019 16:13:10 +5300
# url = "https://docs.google.com/forms/d/e/1FAIpQLSfEQRfe0ceeo13uiNlaCo52Wa8xUyU7s5DkTbXa_a5y4MReJA/viewform?embedded=true"
#
# print(url.replace("?embedded=true",""))

# https://docs.google.com/forms/d/e/1FAIpQLSfEQRfe0ceeo13uiNlaCo52Wa8xUyU7s5DkTbXa_a5y4MReJA/viewform
# https://docs.google.com/forms/d/1K8IkGlQ-0TWISiesBmutRj2e98MW-ZU30pX8QwlkB-g/edit#responses

# import datetime
# from datetime import timezone
import email.utils
# dt = datetime.datetime.now()
# print(email.utils.format_datetime(dt))

from datetime import datetime
import pytz
tz = pytz.timezone('Asia/Kolkata')
now = datetime.now()
your_now = now.astimezone(tz)
print(your_now)
print(email.utils.format_datetime(your_now))