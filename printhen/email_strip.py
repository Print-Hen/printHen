import re

def strip_mail(body):
    body = re.sub(r'\n','',body)
    body = re.sub(r'\-\-(.*)','',body)
    body = re.sub(r'(r|R)egards.*','',body)
    body = re.sub(r'(t|T)hank.*','',body)
    
    #line = lines[0]
    print body
    return body





if __name__ == "__main__":
    body = '''
    
    print me two copies of page 3


Hitesh Verma
Software Engineer
PutPeace.com
http://hiteshverma.in

On Wed, Nov 23, 2016 at 10:57 PM, sandeep mederametla <deepu730@gmail.com> wrote:
hey guys check this out,

https://razorpay.com/ecod/
            '''
    # body = raw_input("Enter your Command")
    strip_mail(body)