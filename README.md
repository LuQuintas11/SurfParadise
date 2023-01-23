![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome LuQuintas11,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders
# Surf Paradise

 Surf Paradise is a finctional store designed and implemented with Django, Python, HTML, and CSS. It is about surf boards, wetsuit and accesories. Customer can search by category or description any product and purchase it. 

You can find the link to the live website right here

[screenshot]


## Technologies used


* Python 3.2 
* Heroku 
* Gitpod 
* Github/ Github pages
* Am I responsive?
* Django Allauth
* Bootstrap4 
* Font Awesome 
* Crispy Forms
* Stripe
* ElephantSQL 
* Psycopg2
* AWS
* Gunicorn
* Code Institute Template 
* Favicon.io 
* Lighthouse 


## Agile thinking

### User Stories

I used Github user stories to keep track of the features that were already done and the ones I had to do

[screenshoot]





## Features 

### Common to All Pages

#### Navbar

Between Mobile and Desktop there is a slightly difference. Mobile does not have search option. 

Mobile

Desktop


### Footer

It has social media, contact form and links to have access to the products


### All products

[screenshot]

### Product details
As an original custome a create a favourite button
[screenshot]

### Shopping bag


### Product admin



## Social media


## Contact form







## Testing

During the development process, I was manually testing in the following ways:

* I used the devtools to simulate different screen sizes/devices
* The sign up/sign in form field works: requires entry in every field, only accept and email in the email field, and the submit button works.
* I simulate a purchase to check that the checkout funcionality is working 
* Create a profile, log in and log out
* Search for specific productos in search bar
* Try to add a favourite product
* Add a review


## Post Development Testing

### Lighthouse score

I ran the tests for both mobile and desktop.

Mobile:


Desktop:





The perfomance score in both is  low. I read Perfomance Django Documentation to know how to improve the performance. The sujestion were:

1. Reduce unused JavaScript code: I do not have unused code in my project

2. Use an appropriate size for images: The images were reduce 

3. Remove resources that block rendering: it suggests tagging stylesheet link with disable or media attribute but this brings consequences when I want to render the website. 

4. Reduce server response time: DJango documentation suggests several things to improve this like:
     Use caching: I did set caching in the setting file. This improve the perfomance but I have to remove it because it was compromising the log in.
     Reduce Queries: I  went through my code and I did noy find the way to reduce the amount of queries 



