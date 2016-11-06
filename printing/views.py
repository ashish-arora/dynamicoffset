# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
import ipdb
from printing.mailer import send_mail

def home(request):
	return render_to_response('home_page.html',{},
                              context_instance=RequestContext(request))

def brochures(request):
	return render_to_response('brochures_new.html',{},
                              context_instance=RequestContext(request))

def business_cards(request):
	return render_to_response('business_cards.html',{},
                              context_instance=RequestContext(request))
def envelopes(request):
	return render_to_response('envelopes.html',{},
                              context_instance=RequestContext(request))
def folder_covers(request):
	return render_to_response('folder_cover.html',{},
                              context_instance=RequestContext(request))
def letterheads(request):
	return render_to_response('letterheads.html',{},
                              context_instance=RequestContext(request))
def banners(request):
	return render_to_response('banners.html',{},
                              context_instance=RequestContext(request))
def calendars(request):
	return render_to_response('calendars.html',{},
                              context_instance=RequestContext(request))
def catalogs_booklets(request):
	return render_to_response('catalogs_booklets.html',{},
                              context_instance=RequestContext(request))
def christmas_cards(request):
	return render_to_response('christmas_cards.html',{},
                              context_instance=RequestContext(request))
def flyers_mailers(request):
	return render_to_response('flyers_mailers.html',{},
                              context_instance=RequestContext(request))
def greeting_cards(request):
	return render_to_response('greeting_cards.html',{},
                              context_instance=RequestContext(request))
def marketing_cards(request):
	return render_to_response('marketing_cards.html',{},
                              context_instance=RequestContext(request))
def posters(request):
	return render_to_response('posters.html',{},
                              context_instance=RequestContext(request))
def presentation_folder(request):
	return render_to_response('presentation_folder.html',{},
                              context_instance=RequestContext(request))
def large_quality_merchandise(request):
	return render_to_response('large_quality_merchandise.html',{},
                              context_instance=RequestContext(request))
def promotional_merchandise(request):
	return render_to_response('promotional_merchandise.html',{},
                              context_instance=RequestContext(request))
def canvas_prints(request):
	return render_to_response('canvas_prints.html',{},
                              context_instance=RequestContext(request))

def corporate_calendars(request):
	return render_to_response('corporate_calendars.html',{},
                              context_instance=RequestContext(request))
def cards_stationery(request):
	return render_to_response('cards_stationery.html',{},
                              context_instance=RequestContext(request))
def photo_books(request):
	return render_to_response('photo_books.html',{},
                              context_instance=RequestContext(request))
def promotional_merchandise(request):
	return render_to_response('promotional_merchandise.html',{},
                              context_instance=RequestContext(request))
def folded_brochures(request):
	return render_to_response('folded_brochures.html',{},
                              context_instance=RequestContext(request))
def magzines_booklets(request):
	return render_to_response('magzines_booklets.html',{},
                              context_instance=RequestContext(request))
def graphic_design(request):
	return render_to_response('graphic_design.html',{},
                              context_instance=RequestContext(request))
def request_quote(request):
	return render_to_response('request_quote.html',{},
                              context_instance=RequestContext(request))
def about(request):
	return render_to_response('about.html',{},
                              context_instance=RequestContext(request))
def contact_us(request):
	return render_to_response('contact_us.html',{},
                              context_instance=RequestContext(request))

def worldwide_creations(request):
	return render_to_response('worldwide_creations.html',{},
                              context_instance=RequestContext(request))
def send_email_new(SUBJECT,TEXT):
	import smtplib
        gmail_user = "junuarora@gmail.com"
        gmail_pwd = "jyotiarora29"
        FROM = 'junu@gmail.com'
        TO = ['junuarora@gmail.com'] #must be a list
        #SUBJECT = "Testing sending using gmail"
        #TEXT = "Testing sending mail using gmail servers"
        # Prepare actual message
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            	#server = smtplib.SMTP(SERVER) 
        	server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                #server.quit()
                server.close()
                return 'successfully sent the mail'
        except:
                return "failed to send mail"


def request_quote(request):
	result = ""
	if request.POST:
		comments = request.REQUEST.get("comments","")
		email= request.REQUEST.get("email","")
		company= request.REQUEST.get("company","")
		phone= request.REQUEST.get("phone","")
		required_date= request.REQUEST.get("required_date","")
		product= request.REQUEST.get("custom_product","")
		name= request.REQUEST.get("name","")
		result = send_mail(email,'junuarora@gmail.com', comments)	
	return render_to_response('request_quote.html',{'result':result},
                              context_instance=RequestContext(request))
