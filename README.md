
# Surf Paradise

 Surf Paradise is a fictional store designed and implemented with Django, Python, HTML, and CSS. It is about surf boards, wetsuit and accesories. Customer can search by category or description any product and purchase it. 

You can find the link to the live website right here

![screenshot](/media/website.png)


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


### Project Sprints

![screenshot](/media/userstories.png)

### User Stories

I used Github user stories to keep track of the features that were already done and the ones I had to do


#### As a shopper I want to be able to: 
                                            Register a profile 
                                            Log in and log out
                                            Search products in the website
                                            Filter products by category and price
                                            See a list of products
                                            See the details of a products
                                            See/edit/delete reviews 
                                            Add favourites products
                                            Add products in my bag by quantity and size
                                            Edit/delete products in my bag
                                            Edit quantities in my bag
                                            Checkout and set delivery and payments details 
                                            Receive confirmation of my payment
#### As a admin I want to be able to:
                                            Add/edit/delete products

                 

## Estructure

### Site Map

![screentshot](/media/SITE%20MAP.png)



## Marketing and Seo

I listed short and long tail words:

Short-tail words:

* Surf Shop
* Surf Board
* Surf Accesories
* Beach
* Holidays
* Wetsuits
* Waves

Long-tail words:

* Where can I buy a surfboard?
* What I need to start surfing?
* How much surf suppliers cost?
* Which activities can I do on holidays?
* Surf shops near me


I used word tracker and Google search to narrow them down. I chose the ones with more relevance. I included this words in headers and meta tags


![This is an image](/media/WordTracker.png)
![This is an image](/media/GoogleSearch.png)


### Social Media

I created a facebook page:
[screnshot]









# Wireframes and Features 

## Common to All Pages

### Navbar

#### Features:
* Home page logo
* Login/logout links
* Search bar
* Shopping bag
* Product management links ( as a admin user)
 
Desktop:

![This is a image](/media/navdesktop.png)

Mobile:

![This is a image](/media/navmobile.png)

### Footer

#### Features:
* Home page logo
* All products list
* Contact us form
* Social media link

Desktop:
![This is a image](/media/footerdesktop.png)

Mobile:

![This is a image](/media/footermobile.png)


### All products

#### Features:
* List of products
* Summary of each products 
* Edit/delete button(log in as a admin)

Desktop:

![This is a image](/media/allproductsdesktop.png)

Mobile:

![This is a image](/media/allproductsmobile.png)

### Product details

#### Features:
* Product details listed discription, sizes and quantity. As an original custome a create a favourite button
* Edit/delete button (login as admin)
* Add/edit/delete review


![This is a image](/media/addfavourite.png)

![This is a image](/media/removefavourite.png)

![This is a image](/media/review.png)

### Shopping bag

#### Features:
* List of products
* Quantity button
* Update/remove product button
* Keep shopping button
* Checkout button 

Desktop:
![This is a image](/media/shoppingbag.png)


Mobile:

![This is a image](/media/shoppingbagmobile.png)


### Checkout page

#### Features:
* Form to fill out payment method
* Form to fill out delivery address
* Checkout button
* Adjust bag button

Desktop:

![This is a image](/media/checkout.png)

Mobile:

![This is a image](/media/checkoutmobile.png)

### Product admin

#### Features:
* Add/edit/delete products

![This is a image](/media/admin.png)

Desktop:

![This is a image](/media/admin.png)

Mobile:

![This is a image](/media/adminmobile.png)


### Profile

#### Features:
* Update profile information
* View purchase history 


Desktop:

![This is a image](/media/myprofile.png)

Mobile:

![This is a image](/media/profilemobile.png)



## Contact form

Desktop:

![This is a image](/media/contactusdesktop.png)

Mobile:

![This is a image](/media/Contactus.png)




## Testing

During the development process, I was manually testing in the following ways:

* I used the devtools to simulate different screen sizes/devices
* The sign up/sign in form field works: requires entry in every field, only accept and email in the email field, and the submit button works.
* I simulate a purchase to check that the checkout funcionality is working 
* Create a profile, log in and log out
* Search for specific productos in search bar
* Try to add a favourite product
* Add a review


## Bugs

1. The checkout form did not have the option to scroll through countries. I fixed it importing countryfield in models.py 
2. Favourtie button funcionality it was not working. The filter to determine if favorite exists was wrong and the product detail page was rendering template without favorite context variable.
3. The review section was not displaying the edit and delete option. The edit/detele code was not part of the {review in product.reviews.all} loop. 



## Code Validation 

* HTML validator:
![This is a image](/media/baseIndex.png)

* CSS validator:
![This is a image](/media/cssvalidator.png)

* I run python3 -m flake8  and psycodestyle to validate python:
It recommended shortening lines of code. Not all could be shortened



## Post Development Testing

### Lighthouse score

I ran the tests for both mobile and desktop.

Mobile:

![This is a image](/media/LigthouseMobile.png)


Desktop:

![This is a image](/media/LigthouseDesktop.png)

The perfomance score in mobile is low. I read Perfomance Django Documentation to know how to improve the performance. The sujestion were:

1. Reduce unused JavaScript code: I do not have unused code in my project

2. Remove resources that block rendering: it suggests tagging stylesheet link with disable or media attribute but this brings consequences when I want to render the website. 

3. Reduce server response time: DJango documentation suggests several things to improve this like:
     Use caching: I did set caching in the setting file. This improve the perfomance but I have to remove it because it was compromising the log in.
     Reduce Queries: I  went through my code and I did noy find the way to reduce the amount of queries 



## Deployment 

### Elephant SQL

1. Create a data-base:
 * Log in ElephantSQL.com 
 * Create New Intance: Give a name
                       Select the Tiny Turtle (free) plan

#### Heroku

1. Create new app
2. Add the config var DATABASE_URL. Value: database url from ElephantSQ
3. Open your app page -> Settings -> "Reveal Config Vars" and add the following:
* DISABLE_COLLECTSTATIC, value :1 Remove this before deployed.
* SECRET_KEY, value : use Djecrety to generate a random secret key.
4. In settings.py:
* DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
* SECRET_KEY = os.environ.get('SECRET_KEY')
5. In order to be able to run the application on localhost, add SECRET_KEY and DATABASE_URL and their values to env.py
6. Connect GitHub Repo to Heroku App



#### Amazon Web Services (AWS) Storage

1. All static and media files are stored with AWS S3

2. Added to settings the next:
![This is a image](/media/AWS.png)



### Credits

* The icons in the footer were taken from Font Awesome  https://fontawesome.com/start
* The font-family was imported from https://fonts.google.com/
* The pictures were taken from https://www.pexels.com/es-es/ 
* I want to give credits to my tutor Sandeep Aggarwal and Oisin from tutoring sessions


