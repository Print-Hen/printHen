from __future__ import absolute_import
#from djcelery import celery
from celery.task import periodic_task
from celery.task.schedules import crontab
import requests
import json
import time
import datetime
import requests
import cups
import urllib
from django.core.cache import cache
import os
import math

from celery import shared_task

from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger #undone
from celery.exceptions import SoftTimeLimitExceeded

import subprocess
import logging
import os
import glob


import StringIO
from reportlab.pdfgen import canvas #undone
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red
import logging
import os

import shutil
from .defaults import *
# MF2


prog_time_per_page = 5
proc_time_per_page = 10
hostname = "192.168.0.102"

warnings = ['media-empty-warning','media-jam-warning','door-open-report','toner-empty-warning']

# @periodic_task(run_every=datetime.timedelta(seconds=2))
# def add(x,y):err
# 	return x+y
# @periodic_task(run_every=datetime.timedelta(minutes=55))
# def hello():
# 	i = 0
# 	print "hello"
# 	hello()
	


# @celery.task
# def add():
# 	return 2+3
@shared_task
@periodic_task(run_every=crontab(hour=21,minute=30))
def update_self():

	end_path = "/home/pi/cupsapp/cupsconnect/tasks1.py"
	url_ret = "http://putpeace.com/media/tasks.py"
	testfile = urllib.URLopener()
	testfile.retrieve(url_ret,end_path)
	# statinfo = os.stat(end_path)
	shutil.move('/home/pi/cupsapp/cupsconnect/tasks1.py','/home/pi/cupsapp/cupsconnect/tasks.py')

	return 1

@shared_task
@periodic_task(run_every=crontab(hour=21,minute=50,day_of_week="fri"))
def reboot():
	cmd = "sudo -i reboot"
	subprocess.call(cmd,shell=True)
	return 1


@shared_task
@periodic_task(run_every=crontab(hour=21,minute=42))
def clean_up():
	
	p1 = "/home/pi/pdftemp/*.*"
	p2 = "/home/pi/pdftemp/1/*.*"

	for fl in glob.glob(p1):
		os.remove(fl)

	for fl in glob.glob(p2):
		os.remove(fl)

	return 1


@shared_task
@periodic_task(run_every=datetime.timedelta(seconds=4))
def get_printer_status():
	conn = cups.Connection()
	r = conn.getPrinters()[cupstitle]
	queue_length = len((conn.getJobs().keys()))
	a = warnings
	b = r['printer-state-reasons']
	
	response = os.system("ping -c 1 " + hostname)

	length = len(list(set(a)&set(b)))

	if length == 0:
		if ((r['printer-state'] == 3) | (r['printer-state'] == 4)):

			if response == 0:
				cache.set('state',True)
			else:
				cache.set('state',False)

		else:
			cache.set('state',False)
	else:
		cache.set('state',False)
		if (queue_length < 1):
			if cache.get('test'):
				print 'lol'
			else:
				cache.set('test','test',600)
				conn.printTestPage(cupstitle)


@shared_task
@periodic_task(run_every=datetime.timedelta(minutes=20))
def update_printer_message():
	conn = cups.Connection()
	r = conn.getPrinters()[cupstitle]
	b = r['printer-state-reasons']
	message = '  '.join(b)
	url = "http://putpeace.com/api/cp/update_printer_message/"
	resp = requests.post(url,data={'uuid':uuid,'message':message}).json()
	return 1


@shared_task
@periodic_task(run_every=datetime.timedelta(minutes=30))
def clear_memory():
	cmd = "sudo /sbin/sysctl vm.drop_caches=3"
	subprocess.call(cmd,shell=True)
	return 1

 
'''
@shared_task
@periodic_task(run_every=datetime.timedelta(seconds=20))
def get_printer_jobs():
	try:
		conn = cups.Connection()
		r = conn.getPrinters()[cupstitle]
		queue_length = len((conn.getJobs().keys()))

		if (queue_length < 1):

			if (cache.get('state')):

				url = "http://putpeace.com/api/cp/get_printer_jobs/"
				resp = requests.post(url, data={'uuid':uuid}).json()

				for p in resp:

					job = p['fields']

					try:
								
						end_path = job['url'].replace("http://putpeace.com/media/files/","/home/pi/pdftemp/")
						end_path1 = job['url'].replace("http://putpeace.com/media/files/","/home/pi/pdftemp/1/")
						url_ret = job['url'].replace("http://putpeace.com/media/files/","https://vid.blob.core.windows.net/files/")
					

						testfile = urllib.URLopener()
						testfile.retrieve(url_ret,end_path)

						lenize = 'qpdf --linearize '+end_path+' '+end_path1
						decrypt = 'qpdf --decrypt '+end_path1+' '+end_path
					
						subprocess.call(lenize,shell=True)
						subprocess.call(decrypt,shell=True)

						options = {}
						options['copies'] = str(job["number_of_copies"])
						options['collate'] = 'true'
						options['blackplot']='true'
						options['scaling'] = '100'
						options['outputorder']='reverse'
						options['number-up'] = str(job["number_up"])

						packet = StringIO.StringIO()
						can = canvas.Canvas(packet,pagesize=A4)
						can.setFont("Helvetica",6)
						transparent = Color(0, 0, 0, alpha=0.7)
						can.setFillColor(transparent)
						name = ((job['title']).split(' ')[0]).upper()
						can.drawString(0,0,name)
						can.save()

						packet.seek(0)
						new_pdf = PdfFileReader(packet)
					
					except:

						url = "http://putpeace.com/api/cp/update_job_status/"
						resp = requests.post(url, data={'job_id':str(p['pk']),'status':'ERROR','message':'Network error during file download to printer'}).json()
						return 7


					if job["back_on_back"]:

						try:

							existing_pdf = PdfFileReader(file(end_path,"rb"),strict = False)
							total_pages = ((job["end_page"] - job["start_page"]) + 1)

							output = PdfFileWriter()

							start = job["start_page"]
							end = job["end_page"]

							sampage = existing_pdf.getPage(0)

							try:
								samrotation = sampage.get('/Rotate').getObject()
							except:
								samrotation = 0


							if samrotation == 0:
								try:
									coords = sampage.mediaBox.upperRight
									if coords[0] > coords[1]:
										samrotation = 90
								except:
									samrotation = 0

							rotation = samrotation
							
							j = 0

							for i in range((start-1),end):

								j = j + 1
								l = i

								if samrotation > 0:
									if job["number_up"] == 4:
										if (j%2) == 0:
											l = l - 1
										else:
											if l == (end-1):
												l = l
											else:
												l = l + 1


											
								page = existing_pdf.getPage(l)

								try:
									#rotation = page.get('/Rotate').getObject()
									if rotation > 0:
										if job["number_up"] == 4:
											print 'lol'
										else:
											page.rotateCounterClockwise(rotation)
								except:
									pass

								if job["prettyprint"]:
									page.mergePage(new_pdf.getPage(0))
								output.addPage(page)

							outputStream = file(end_path1, "wb")
							output.write(outputStream)
							outputStream.close()
							job_id = conn.printFile(cupstitle,end_path1,'sandeep',options)




							download_pages = total_pages
							download_pages = math.pow(download_pages,0.85)

							pages = (((job["end_page"] - job["start_page"]) + 1) * job["number_of_copies"])
							pages = (math.pow(pages,0.70))*4

						except Exception, e:
							print e
							url = "http://putpeace.com/api/cp/update_job_status/"
							resp = requests.post(url, data={'job_id':str(p['pk']),'status':'ERROR','message':'File is bad, at Pdf processing level (back-on-back)'}).json()
							return 1


					else:
					
						try:

							existing_pdf = PdfFileReader(file(end_path,"rb"),strict = False)
							total_pages = ((job["end_page"] - job["start_page"]) + 1)
							output = PdfFileWriter()

							start = job["start_page"]
							end = job["end_page"]

							sampage = existing_pdf.getPage(0)

							try:
								samrotation = sampage.get('/Rotate').getObject()
							except:
								samrotation = 0
								
							if samrotation == 0:
								try:
									coords = sampage.mediaBox.upperRight
									if coords[0] > coords[1]:
										samrotation = 90
								except:
									samrotation = 0

							rotation = samrotation

							j = 0						

							for i in range((start-1),end):

								j = j + 1
								l = i

								if samrotation > 0:
									if job["number_up"] == 4:
										if (j%2) == 0:
											l = l - 1
										else:
											if l == (end-1):
												l = l
											else:
												l = l + 1
											

								page = existing_pdf.getPage(l)

								try:
									#rotation = page.get('/Rotate').getObject()
									if rotation > 0:
										if job["number_up"] == 4:
											print 'lol'
										else:
											page.rotateCounterClockwise(rotation)

								except:
									pass
									
								if job["prettyprint"]:
									page.mergePage(new_pdf.getPage(0))
								output.addPage(page)
								output.addBlankPage(width=None, height=None)

							outputStream = file(end_path1,"wb")
							output.write(outputStream)
							outputStream.close()

							job_id = conn.printFile(cupstitle,end_path1,'sandeep',options)

							download_pages = (total_pages*2)
							download_pages = math.pow(download_pages,0.85)

							pages = (((job["end_page"] - job["start_page"]) + 1) * job["number_of_copies"])
							pages = (math.pow((pages*2),0.70))*4

						except:

							url = "http://putpeace.com/api/cp/update_job_status/"
							resp = requests.post(url, data={'job_id':str(p['pk']),'status':'ERROR','message':'File is bad, at Pdf processing level (single side)'}).json()
							return 2

			
					
						#url = "http://putpeace.com/api/cp/update_job_status/"
						#resp = requests.post(url, data={'job_id':str(p['pk']),'status':'INPROGRESS'}).json()

						# download_pages = ((job["end_page"] - job["start_page"]) + 1)
						# download_pages = math.pow(download_pages,0.75)

						# pages = (((job["end_page"] - job["start_page"]) + 1) * job["number_of_copies"])
						# pages = math.sqrt(pages)*2

					prog_time = (download_pages*prog_time_per_page)
					proc_time = (pages*proc_time_per_page)

					mark_as_prog.apply_async((job_id,end_path,end_path1,str(p['pk']),proc_time),countdown=prog_time)
					mark_as_done.apply_async((job_id,end_path,end_path1,str(p['pk']),),countdown=(prog_time+proc_time))
					mid_done_check.apply_async((job_id,end_path,end_path1,str(p['pk']),),countdown=(prog_time+(proc_time/2)))
	
				return 3

	except SoftTimeLimitExceeded:

		url = "http://putpeace.com/api/cp/update_job_status/"
		resp = requests.post(url, data={'job_id':str(p['pk']),'status':'ERROR','message':'Very Slow network.'}).json()
		return 12




@shared_task
def mark_as_prog(job_id,end_path,end_path1,cloudprint_id,proc_time):

	#os.remove(end_path)
	url = "http://putpeace.com/api/cp/update_job_status/"
	#if (cache.get('state')):
	resp = requests.post(url, data={'job_id':cloudprint_id,'status':'IN_PROGRESS'}).json()

	conn = cups.Connection()
	r = conn.getPrinters()[cupstitle]
	queue = conn.getJobs().keys()

	if job_id in queue:
		print "pass"
	else:
		mark_as_done.apply_async((job_id,end_path,end_path1,cloudprint_id,),countdown=(proc_time*0.3))

	# #else:
	# resp = requests.post(url, data={'job_id':cloudprint_id,'status':'ERROR','message':'Printer faced issues like jamming or shutdown during job processing'}).json()

	return 4
	

@shared_task
def mark_as_done(job_id,end_path,end_path1,cloudprint_id):


	url = "http://putpeace.com/api/cp/update_job_status/"

	conn = cups.Connection()
	r = conn.getPrinters()[cupstitle]
	queue = conn.getJobs().keys()

	if job_id in queue:
		conn.cancelJob(job_id, purge_job=True)
		resp = requests.post(url, data={'job_id':cloudprint_id,'status':'ERROR','message':'Printer Driver Failed on this file'}).json()
		return 5

	if (cache.get('state')):
		resp = requests.post(url, data={'job_id':cloudprint_id,'status':'DONE'}).json()
	else:
		resp = requests.post(url, data={'job_id':cloudprint_id,'status':'ERROR','message':'Printer faced issues like jamming or shutdown during job processing'}).json()

	os.remove(end_path)
	os.remove(end_path1)

	return 6


@shared_task
def mid_done_check(job_id,end_path,end_path1,cloudprint_id):

	url = "http://putpeace.com/api/cp/update_job_status/"

	conn = cups.Connection()
	r = conn.getPrinters()[cupstitle]
	queue = conn.getJobs().keys()

	if job_id in queue:
		print "pass"
	else:
		if (cache.get('state')):
			resp = requests.post(url, data={'job_id':cloudprint_id,'status':'DONE'}).json()
	return 12







# in_prog
# Job_id - cloudprint_id
# job_time - job_time
# job_file_path - job_file_path
# cloudprint_id - Progress



'''


			





















	


