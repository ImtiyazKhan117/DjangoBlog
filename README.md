# Django-Blog
Web application framework for blog written in Python3.x-Django 1.9 by Imtiyaz <br />
## note:
this is Django application not an Django project <br />
these installation is done by assuming you already have installed python3.x in your system<br>
 
# Prerequisites:
  Python3.x<br/>
  Django 1.9<br/>
  django-widget-tweaks<br/>
# installation
  you can clone repository by execuating following commands in your cmd/terminal<br/>
  git clone https://github.com/ImtiyazKhan117/DjangoBlog.git<br/>
   
 ### Django installation
  pip install Django==1.9  
 ### widget-tweaks installation
  pip install django-widget-tweaks
  
# How to Run application:
  ### step01: add your application into your project
  first extract/un-zip the 'DjangoBlog' then go inside the 'DjangoBlog' folder and copy the 'Blog' folder <br/> 
  and paste it into your Django Project folder<br/>
  then list your application in setting.py module<br/>
 
 ## For example: your setting.py module
 
 #### &emsp;&emsp;&emsp;INSTALLED_APPS = (<br>
 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;'.....other apps.....',<br/>
 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;'blog',<br/>
 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;'widget_tweaks')<br/>
 
 ### Important! add this two methods in your setting.py module for uploading and dwonloading media
 
 #### &emsp;&emsp;&emsp;&emsp;&emsp;Setting.py
 #### &emsp;&emsp;&emsp;MEDIA_URL = '/media/'
 #### &emsp;&emsp;&emsp;MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite/media')
 
 ### step02: set-up urls.py modlue to route your web-app on server
 ## Import modlues and method from setting.py
  ### &emsp;&emsp;&emsp;&emsp; Urls.py module
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; from django.conf.urls.static import static<br/>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; from django.conf import settings<br/>
 
  ### list your application url into urlpatterns
  ### &emsp;&emsp;&emsp;&emsp; Urls.py module
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; urlpatterns = [<br/>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;url(r'^admin/', include(admin.site.urls)),<br/>
	&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;url(r'^blog/',include('blog.urls'))<br/>
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)<br/>
  ## step03 Django Admin setup
  #### If you already have django super-user then you can escape this part.<br/>
  ### commands for setting up super-user
  #### &emsp;&emsp;&emsp;&emsp; python manage.py createsuperuser
  #### put the user-name,e-mail,password
  ### Note: super user is requird becuase of posting and managing forms
  ## Final step
  #### run the following commands in you terminal/cmd to make migration for database
  ### commands:
  #### &emsp;&emsp;&emsp;&emsp; python manage.py makemigrations
  #### &emsp;&emsp;&emsp;&emsp; python manage.py migrate
  ## now Run the server
  #### &emsp;&emsp;&emsp;&emsp; python manage.py runserver
  ## This template is created by Imtiyaz
