import re

def strip_mail(body):
    body = re.sub(r'(?i)(?<=[0-9])-(?=[0-9])'," to ",(body))
    body = re.sub(r'forwarded message','',body,flags=re.IGNORECASE)
    body = re.sub(r'date?.\:.*\n','',body,flags=re.IGNORECASE)
    body = re.sub(r'subject?.\:.*\n','',body,flags=re.IGNORECASE)
    body = re.sub(r'[\w\.-]+@[\w\.-]+','',body,flags=re.IGNORECASE)
    body = re.sub(r'from?.\:.*\n','',body,flags=re.IGNORECASE)
    body = re.sub(r'to?.\:.*\n','',body,flags=re.IGNORECASE)
    body = re.sub(r'\n','',body,flags=re.IGNORECASE)
    body = re.sub(r'\b\-\-\b(\w*)','',body,flags=re.IGNORECASE)
    body = re.sub(r'regards.*','',body,flags=re.IGNORECASE)
    body = re.sub(r'thank.*','',body,flags=re.IGNORECASE)
    body = re.sub(r'(\-|\=)*','',body,flags=re.IGNORECASE)
    return body





if __name__ == "__main__":
    body = '''
    
============ Forwarded message ============
From : Raghuram Iyer <ragzzyr@putpeace.com>
To : "printhen77"<printhen77@gmail.com>
Date : Fri, 23 Dec 2016 00:45:10 +0530
Subject : hello
============ Forwarded message ============

print me one copy from 133-5642222



---------- Forwarded message ----------
From: Raghuram Iyer <raghuram8892@gmail.com>
Date: Thu, Dec 22, 2016 at 7:26 PM
Subject: 
To: printhen77@gmail.com


one copy



-- 
Regards
Raghuram Iyer "Ragzzy-R"
Lead Developer,
Putpeace
http://ragzzyr.com




"I'm Trying to change the world,but i cant find the Source Code".




-- 
Regards
Raghuram Iyer "Ragzzy-R"
Lead Developer,
Putpeace
http://ragzzyr.com




"I'm Trying to change the world,but i cant find the Source Code".


            '''
    # body = raw_input("Enter your Command")
    strip_mail(body)
    #print strip_mail(body)
