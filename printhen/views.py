
import json
import easyimap
import cups
import itertools
import smtplib
from email.mime.text import MIMEText
from .forms import AdminForm
from . import printhen_nltk
from pprint import pprint
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
def index(request):
    try:
        with open('/home/pi/printhen/credentials.json') as data_file:
           data = json.load(data_file)
        pprint(data)
    except Exception,err:
        print err
        return
    host = data["imap_hostname"]
    user = data["username"]
    password = data["password"]
    mailbox = "inbox"
    imapper = easyimap.connect(host, user, password, mailbox)
    from_addr = ""
    op = {}
    mail1 = imapper.unseen(1)
    print "HELLO"
    print mail1
    for mail in mail1:
        title = mail.title.encode("utf-8")
        body = mail.body.encode("utf-8")
        from_addr = mail.from_addr.encode("utf-8")

        print "Checking for title =>" + title
        title = title.upper()
        if "PRINTHEN" in title:
            print "MAGIC TITLE PASSED"
            #printhen_response(data["username"], from_addr, "MAGIC TITILE PASSED")
        else:
            print "MAGIC TITLE FAILED"
            printhen_response(data["username"], from_addr, "[no-reply]PRINTHEN-INVALID SUBJECT", "Hey buddy kindly send mail with PRINTHEN as subject in order to initiate the print")
            return


        from_addr = from_addr[from_addr.find("<")+1:from_addr.find(">")]
        print "====================="
        print "NEW MAIL "
        print "====================="
        print "from    : " + from_addr
        print "Message : " + body
        # if "begin print" not in body or "end print" not in body or "from" not in body or "to" not in body or "copies" not in body:
        #     printhen_response(data["username"], from_addr, "[no-reply] PRINTHEN. SYNTAX ERROR", "Syntax error. The correct syntax is: begin print from x to y copies z end print")
        #     return

        # else:
        #body = body[body.find("begin print")+11:body.find("end print")]
        op = parseBody(body)
        conn = cups.Connection()
        print body
        print op
        if not mail.attachments:
            printhen_response(data["username"], from_addr, "[no-reply]PRINTHEN-NO ATTACHMENT FOUND", "Hey Buddy, I guess you forgot to attach a document for printing")
            return

        if int(op['from']) > int(op['to']):
            printhen_response(data["username"], from_addr, "[no-reply] PRINTHEN-START PAGE GREATER THAN END PAGE", "hey buddy it seems like the from value is greater that to value kindly check it")
            return
        for attachment in mail.attachments:
            filename = settings.MEDIA_PATH + attachment[0]
            with open(filename, 'wb') as f:
                f.write(attachment[1])
            #conn = cups.Connection()
            options = {}
            options['copies'] = op['copies']
            s = []
            s.append(op['from'])
            s.append("-")
            s.append(op['to'])
            s1 = ''.join(s)
            options['page-ranges'] = s1
            print options
            printers = conn.getPrinters()
            for printer in printers:
                print printers.items()
                print printer, printers[printer]["device-uri"]
                conn.printFile("printhen", filename, "print", options)
                print "SUCCESS"
    #printhen_response(data["username"], from_addr, "[no-reply] PRINTHEN",str(op))
            
    return HttpResponse("SUCCESS");
    
def printhen_response(from_addr, to_addr, subject, msg):
    msg1 = MIMEText(msg)
    msg1['Subject'] = subject
    msg1['From'] = from_addr
    msg1['To'] = to_addr
    try:
        with open('credentials.json') as data_file:
            data = json.load(data_file)
        pprint(data)
    except:
        print "CREDENTIALS NOT FOUND"
        return
    s = smtplib.SMTP_SSL(data["smtp_hostname"], 465)
    #s.starttls()
    s.login(data["username"], data["password"])
    s.sendmail(from_addr, [to_addr], msg1.as_string())
    s.quit()

def parseBody(body):
    d = printhen_nltk.extract_information(body)
    return d

@csrf_exempt
def admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            with open('credentials.json', 'w') as outfile:
                json.dump(form.cleaned_data, outfile)
            return HttpResponse(json.dumps(form.cleaned_data))

    else:
        form = AdminForm()

    return render(request, 'printhen/admin.html', {'form': form})