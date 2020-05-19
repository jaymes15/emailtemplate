from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def homepage(request):
	return render(request,"mailtemplate/homepage.html")


def sendmail(request):
	user = settings.EMAIL_HOST_USER
	to=['jamesoluwatomisinomotosho@gmail.com']
	message = "hello"
	email_body = """\
    <html>
      <head></head>
      <body>
        <h2>%s</h2>
        <p style='color:red'>%s</p>
        <h5></h5>
      </body>
    </html>
    """ % (user, message)
	email = EmailMessage('A new mail!', email_body,to=to)
	email.content_subtype = "html"
	try: 
		pass
		email.send()
		return render(request,"mailtemplate/homepage.html")
	except Exception as error:
		context =  {"error" : error}
		return render(request,"mailtemplate/error.html", context)


def sendtemmail(request):
	subject = 'Subject'
	hello = 'hello'
	context ={"hello":"hello"}
	html_message = render_to_string('mailtemplate/emailbody.html', context)
	plain_message = strip_tags(html_message)
	from_email = settings.EMAIL_HOST_USER
	to = 'jamesoluwatomisinomotosho@gmail.com'
	mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
	return render(request,"mailtemplate/homepage.html")

