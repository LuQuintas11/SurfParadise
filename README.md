
# Surf Paradise

 Surf Paradise is a fiypctional store designed and implemented with Django, Python, HTML, and CSS. It is about surf boards, wetsuit and accesories. Customer can search by category or description any product and purchase it. 

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


### Project Sprints

[screenshot]

### User Stories

I used Github user stories to keep track of the features that were already done and the ones I had to do

[screenshoot]


#### As a shopper I want to be able to: 
                                            register a profile 
                                            log in and log out
                                            search products in the website
                                            filter products by category and price
                                            see a list of products
                                            see the details of a products
                                            see/edit/delete reviews 
                                            add favourites products
                                            add products in my bag by quantity and size
                                            edit/delete products in my bag
                                            edit quantities in my bag
                                            checkout and set delivery and payments details 
                                            receive confirmation of my payment
#### As a admin I want to be able to:
                                            add/edit/delete products

                 

## Estructure

### Site Map

[screentshot]



## Marketing and Seo

I listed short and long tail words:

Short-tail words:




Long-tail words:



I used word tracker and Google search to narrow them down. I chose the ones with more relevance. I included this words in headers and meta tags



[screenshot]


### Social Media

I created a facebook page:
[screnshot]









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


## Bugs

1. The checkout form did not have the option to scroll through countries. I fixed it importing countryfield in models.py 
2. Favourtie button funcionality it was not working. The filter to determine if favorite exists was wrong and the product detail page was rendering template without favorite context variable.
3. The review section was not displaying the edit and delete option. The edit/detele code was not part of the {review in product.reviews.all} loop. 



## Code Validation 



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



## Deployment 

### Elephant SQL


