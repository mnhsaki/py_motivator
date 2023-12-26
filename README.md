# py_motivator

Introduction
This is a Python program that intends to send motivational quotes on WhatsApp on a daily basis. These quotes are motivational by default but can be changed to funny, sports related, etc if required.

Purpose
This project add value by sending/receiving motivational quotes everyday.

Intended Audience
Anyone who wants daily Motivational quotes on WhatsApp.

Overall Description
This project will have two main modules, one would fetch a quote from a Quote of the Day API
and send a WhatsApp text using a Third Party Service. The other module will be a cron scheduler that will schedule these WhatsApp texts for everyday.

System Features and Requirements
	Functional Requirements
Python 3.12.1 / 3.8 (For heroku Deployment)
Requests
Twilio
APScheduler
	External Interface Requirements
Quotes of the Day API
Twilio Dashboard for WhatsApp
Visual Studio Code
GitHub
Heroku

	System Features
get_quote_of _the_day
	- takes category as parameter and returns the quote of the day

      -    set_twilio_connection
		- takes account_sid and account_token as parameter and returns client object

      - 	send_whatsapp_text
      		- takes quote and twilio client connection as parameters and returns message ID      

background_cron_job
	- takes send_whatsapp_text as a job to execute everyday in background
Assumptions and Dependencies
As the service for sending and receiving Quotes depends on Third party applications, it is assumed that they are always Up and Running.
The Project initially python version to 3.8 for supporting heroku deployment.
Other Non Functional Requirements
Security - All the keys and passwords to be stored as Environment variables
Quality - Code quality and PEP8 Standards
Performance - Deployment on Heroku for scaling, newer Python version with updated Libraries

