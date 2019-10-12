# Voice-Mail :mailbox: :ear: :speaker:
### Introduction
Visually impairment is ability loss for someone’s eyes. It is known that life gets harder when people cannot see around. It cannot be restricted in daily life, so even technology becomes hard to use for visually impaired person. Because of these, an email application which takes commands with speech and serves emails as a speech is our subject. This is large subject that anybody can implement in different areas like Mobile Applications, Desktop Applications or Web Applications. In this project, I choosed to create a Web Application.

Basically, a web application that works on only **Chrome**. It uses **Speech to Text** and **Text to Speech** API for managing application with voice. For email service, it uses **Gmail API**.

### Project Structure
<img width="788" alt="Ekran Resmi 2019-10-13 01 13 23" src="https://user-images.githubusercontent.com/32219894/66708296-fc74e380-ed56-11e9-9f2d-b309f2bfb867.png">

### How to Run ?

#### *Enabling API*

Application uses Gmail API for mail server. So, you need to enable your Gmail API from https://console.developers.google.com/. If you don’t have a project create it.

<img width="300" src="https://user-images.githubusercontent.com/32219894/66708338-ad7b7e00-ed57-11e9-9a65-86955f9649a8.png" >

After that you need to create a secret key from your identity access management (iam) and administrator tab then download it to application directory. Don’t forget to give owner role.  Note that don’t share anywhere your downloaded file which contains your secret key. 

<img width="700" src="https://user-images.githubusercontent.com/32219894/66708390-83768b80-ed58-11e9-8a24-d772609a5cc2.png" >

Put the file into your application directory with name “credentials.json”.

<img width="300" src="https://user-images.githubusercontent.com/32219894/66708402-a7d26800-ed58-11e9-8d91-de1f987d77cc.png" >

#### *Requirements*

You can install these required packages to your app using pip install <package>
  
      Django==2.1.5
      django-crispy-forms==1.7.2
      django-bootstrap4==0.0.7
      word2number==1.1
      google-api-core==1.14.3
      google-api-python-client==1.7.11
      google-auth==1.6.3
      google-auth-httplib2==0.0.3
      google-auth-oauthlib==0.4.0
      google-cloud-core==1.0.3
      google-cloud-speech==1.2.0
      google-cloud-storage==1.20.0
      google-cloud-texttospeech==0.5.0
      google-resumable-media==0.4.1
      googleapis-common-protos==1.6.0

#### *Make Migrations*

I used one database table to manage attachments. You need to make migrations to use it. Follow these commands.

<img width="300" src="https://user-images.githubusercontent.com/32219894/66708497-d866d180-ed59-11e9-8e80-83e8f02e6569.png">
<img width="300" src="https://user-images.githubusercontent.com/32219894/66708505-ee749200-ed59-11e9-8937-8f7890d390f0.png">

After migrations, you can reach database table form http://127.0.0.1:8000/admin. Give username and password that you created as a super user. 

#### *Run Application*

You must know that you need to use Google Chrome to use this application properly. For Mac users Safari and other browsers do not support WebKitSpeechRecognition.
For running application follow the commands. 

     python manage.py runserver

In first launch, Google opens a new tab to authenticate the application and waiting permission from user to manage its mail account.

<img width="500" src="https://user-images.githubusercontent.com/32219894/66708529-46ab9400-ed5a-11e9-90b2-9b4da864f7ab.png">

Trust it and allow what needs to application.

<img width="300" src="https://user-images.githubusercontent.com/32219894/66708532-6478f900-ed5a-11e9-9d67-885236c212fd.png">

After that app starts and allow microphone

<img width="500" src="https://user-images.githubusercontent.com/32219894/66708540-82def480-ed5a-11e9-9309-249fdba1e79a.png">

Note that; you must specify your application running port as 8000 because we used some static code written in a brute force way.

#### *Commands That Application Understands For Inbox Page*
    
    Create an email -> Goes to email creation page
    Send an email -> Goes to email creation page
    Go to inbox -> Goes to inbox
    Open inbox -> Goes to inbox 
    Read email with number <say a number> -> Goes to Read Email Page

#### *Commands That Application Understands For Email Creation Page*

    Go to inbox -> Goes to inbox
    Open inbox -> Goes to inbox 
    Receiver -> Starts to fill receiver area
    Subject -> Starts to fill subject area
    Message -> Starts to fill message area
    Send this email -> Submits email and returns inbox

#### *Commands That Application Understands For Read Email Page*
	
    In this page voice commands are not allowed. Just wait to message reading to stop and it immediately returns to inbox page. Also in this page, it downloads attachments automatically and when you click anywhere on the page you can listen whole message again.

#### *Result*

    I will provide a video which shows how to manage interface with voice using Google Translate Voice. Because I am not a native speaker and sometimes misunderstandings happen.




