# print-hen
*printing made easy!!!*

Printhen is an opensource project which is meant for printing documents in small offices. The final product is a raspberrypi that runs django/celery on its core and polls a user given user id and password for new mails. The user who wishes to print needs to send a mail to:\<emailid\>

with the following syntax

begin print from \<pageno\> to \<pageno\> copies \<no of copies\> end print

once this is done. the raspberry Pi will initiate the print using pycups. 


for more details contact: team@putpeace.com
