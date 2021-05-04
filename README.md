# Stumps and Studs

A fictional ecommerce website selling sports equipment and clothing.  Built using Django's Python framework.  Frontend developed using HTML, CSS & JavaScript with Bootstrap and jQuery libraries.  Backend built with Python (Django) utilising a Postrgres database.

## Demo

The final project is hosted on Heroku and can be found **TBC**

## Contents

1. [**UX**](#ux)
    * [**Project Aim**](#project-aim)
    * [**User Stories**](#user-stories)
    * [**Design Decisions**](#design-decisions)
    * [**Wireframes**](#wireframes)

2. [**Code**](#code)
    * [**Settings**](#settings)
    * [**File Structure**](#file-structure)
    * [**Static Files**](#static-files)    

3. [**Database Schema**](#database-schema)
    * [**Data Scheme**](#data-scheme)

4. [**Features**](#features)
    * [**Existing Features**](#existing-features)
    * [**Features Left To Implement**](#features-left-to-implement)

5. [**Languages**](#languages)

6. [**Services Used**](#services-used)

7. [**Testing**](#testing)
    * [**Bugs Encountered During Development**](#bugs-encountered-during-development)
    * [**Testing Process**](#testing-process)
    * [**Bugs Encountered During Testing**](#bugs-encountered-during-testing)

8. [**Deployment**](#deployment)
    * [**GitPod Environment**](#gitPod-environment)
    * [**Packages Installed**](#packages-installed)
    * [**Create The Django Project**](#create-the-django-project)
    * [**Environment Variables**](#environment-variables)
    * [**Setting Up The Database**](#setting-up-the-database)
    * [**Create Admin Superuser**](#create-admin-superuser)
    * [**Deploy Application To Heroku**](#deploy-application-to-heroku)
    * [**Connecting Django Application To Postrgres Database**](#connecting-django-application-to-postrgres-database)
    * [**Using Flask Template Inheritance**](#using-flask-template-inheritance)

9. [**Credits**](#credits)
    * [**Inspiration**](#inspiration)
    * [**Content**](#content)
    * [**Media**](#media)
    * [**Acknowledgements**](#acknowledgements)

## UX

### Project Aim

The aim of this project was to produce an enticing and fully-functioning e-commerce website.

### User Stories

* As a shopper/visitor to the website, I want to:
    -   Immediately understand the range of products the website sells.
    -   Easily navigate categories and search for products.
    -   View images of the products available to purchase.
    -	View the prices and details of each product.
    -	Select a size of product (where applicable).
    -	Select between right-handed and left-handed equipment (where applicable).
    -	Add multiple products to a basket.
    -	View items in my basket.
    -	Adjust the quantities of items in my product including removing them from the basket entirely.
    -	View the total cost of the items in my basket.
    -	View any delivery cost applicable and understand how much more cost I need to add to my basket in order to qualify for free delivery.
    -	Easily navigate to a checkout page.
    -	Contact the company.

* As a shopper/visitor who has decided to purchase one or more products, I want to:
    -	Exit the checkout process and return to the store so I can amend the products in my basket.
    -	Be able to provide personal details such as name and email address.
    -	Provide a delivery address for my products to be shipped to.
    -	Enter payment card details to complete a secure checkout.
    -	View my order and the total cost of it including delivery throughout the checkout process.
    -	See a confirmation message confirming that the order has been placed.
    -	Receive an email confirmation that the order has been placed.

* As a shopper/visitor who intends to return to the website in future, I want to:
    -	Create an account.
    -	Store my personal and default delivery address details.
    -	Update my account details.
    -	View my past orders.
    -   Sign in and out of my account.

* As an administrator of the website, I want to be able to:
    -	Use the admin panel to add products.
    -	Use the admin panel to update the details of products.
    -	Use the admin panel to delete products.
    -	Use the admin panel to delete users.

### Design Decisions

#### Fonts

The fonts used throughout the website is Crimson Text for headers and Open Sans for all other elements.  I searched Google for some goo font pairings for ecommerce websites.  I came across [this website](https://www.builderfly.com/7-perfect-font-pairing-for-your-ecommerce-website/) and was enticed by the pairing of Crimson Text and Source Sans Pro.  However, whilst I was developing the header and navbar, I decided that Source Sans Pro font wasn't quite right for my website.  I turned to [Google Fonts](https://fonts.google.com/) to identify other fonts which make good partners to Crimson Text.  I ended up choosing Open Sans as the font to partner Crimson Text.

#### Colour Scheme

I visited a number of popular ecommerce websites for inspiration in the colour palette and design.  [Asos.com](https://www.asos.com/men/), [Adidas](https://www.adidas.co.uk/), [New Look](https://www.newlook.com/uk/homepage) and also the [mini-project](https://mini-project-4-boutique-ado.herokuapp.com/) all demonstrate the simple use of predominantly black and white colour palettes with little colour used.  I think this helps ensure product images standout from the page and wanted to mirror this in my project.  I used [Coolors](https://coolors.co/) to help generate a colour scheme which incorporated a strong black but also other strong colours to help make certain sections and buttons of the website stand out.

#### Inspiration

I often find that ecommerce websites are very busy.  The amount of content visible on screen can detract focus away from the product images.  For example, navigation bars, filters and product details (price, description, ratings, etc) all lead to a lot of text on screen at any one time while searching for products.  Although some product information is useful, product images, name and cost are the most essential things a user is looking for in my opinion.  Further product details can be accessed by clicking on a product and viewing all of its information so there is no need to show it all on the main navigation page.  When researching ecommerce website for inspiration, I came across [this website](https://www.hardgraft.com/collections/footwear) which has a very stripped back layout, ensuring the product images take center stage.  This example really appealed to me.  For these reasons, I wanted to keep the real estate of the header and filters to a minimum and ensure the images were not cluttered with additional product information.

#### Home Page Images & Header

On the home page, I utilise jQuery to make the header transparent and remove the margin from the top of the body so that the images take center stage.  I ensured that the images I selected provide a good contrast for the white font color used on the header items.  Furthermore, I chose images which still looked good on screens with a smaller width.  Here is a comparison between the header on the home page (left) and how the header appear throughout the rest of the site on mobile:

![Header on home page vs header on rest of site](media/readme/images/header-mob.png)

On the home page, when the user starts scrolling down, the header remains at the top of the screen and the background returns to black so that the elements continue to stand out:

![Header background colour changes when user scrolls up and down](media/readme/gifs/header-scroll.gif)

#### Navbar

Utilising jQuery, I added a feature which hides the navigation bar when users scroll down but makes it dropdown (reappear) as soon as they begin scrolling up.  This effect is only applied to medium screens upwards since on small screens, the navigation options can be accessed using a menu toggle.  As outlined above, I wanted to maximise the amount of space on screen for the products to take center stage.  I feel this solution offers good user experience since it means they do not need to scroll up to the very top of the page to access the navigation elements.

However, I did decide that there are some navigation elements which should always be visible to the user and hence I included them in the header which is fixed to the top of the screen throughout the website.  The navigation links I wanted visible at all times are the search form, basket, registration, login and account.  These all feature prominently in my user stories hence wanted to ensure visitors to my website can see them at all times and never have to hunt around for them.

#### Toasts

The toast success message includes a preview of the basket and a link to the basket page for users to quickly checkout.  I fixed the height of the toast basket and gave it the Bootstrap overflow-auto class.  This means users have a preview of their basket they can scroll through without too much screen real estate being used up.  I used Bootstrap's grid layout to make the basket preview responsive.  The success message is used to show users when an item has been added to their basket, a quantity amended or an item has been removed from their basket.

I decided that for warning, info and error messages, it was not necessary to show users the contents of their basket.  Furthermore, for the success toast, I decided there was no need to show users the basket preview if they are already on the basket page since they can see the full basket.  Instead I chose to simply display a message to users without the basket preview underneath:

![Toasts basket preview shows except from when on the basket page already](media/readme/gifs/toasts.gif)

NB: In the GIF above, the cricket stumps have a size and gender.  These attributes were added to the product so I could test the messages and basket quantities updated as desited.  In the final project, cricket stumps will not have size or gender attributes.

### Wireframes

## Code

### Settings

The settings.py file is where the global settings for the project are configured.  Django creates a lot of these by default but there were some changes/additions which needed to be made as I developed the project.

*   **Installed Apps**:  For each new Django app I created, the app name needed to be added to the list of installed apps (INSTALLED_APPS).
*   **Django AllAuth**:  AllAuth can be configured in the global settings.py file.  Installation instructions for AllAuth can be found [here](https://django-allauth.readthedocs.io/en/latest/installation.html) and configuration instructions can be found [here](https://django-allauth.readthedocs.io/en/latest/configuration.html).

### File Structure

The project is split into apps.  Each app has files (such as forms, models, urls and html files) which are specific to that app.  However, there are some common files which we want apps to inherit from or which don't necessarily belong within one of the apps.  These are stored in the templates folder.

Each HTML file extends from the base.html file which is saved in the templates folder.

The templates folder contains an 'allauth' subfolder which contains a number of the allauth template html files.  These were copied from the AllAuth site-packages directory using the following command before I then deleted the AllAuth openid and tests templates:
*   *cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth*

### Static Files

## Database Schema

### Data Scheme

#### Basket Variable in Session Memory

The products my website sells includes sports equipment and clothing.  lothing items typically have sizes and there are some sports equipment which are specific to male or female.  Furthermore, some equipment is taylored for either right-handed or left-handed users; golf clubs for example.  As such, the products in my database have 3 booleans properties; has_sizes, has_side, has_gender.  These indicate whether or not that product has that attribute.  The attributes determine the options users have on the product details page when shopping for products.  Products can have none of these attributes, some of them or all of them.

The items a user adds to their basket need to retain the properties they have selected.  To do this, I needed to come up with a structure for storing basket items within a variable called basket which is saved in session memory.  The basket variable is a dictionary where the keys are the unique product ID's.  For items without any attributes, the value is simply the quanity that the user has added to their basket {product_id: quantity}.

For items which do have at least one of the three aforementioned attributes (size, side, gender), a different structure is needed.  Since each item a user adds of the same product could have different attributes and be of varying quantities, I opted to store all of these attributes within a dictionary which in turn is within a list.  This list is the value to the product ID key in the basket dictionary {product_id: [{'size': size, 'side': side, 'gender': gender, 'quantity': quantity},]}.

When adding these attributes to the dictionary, I don't distinguish between products which only have some of these attributes and those which have all.  If a product doesn't have one of the 3 attributes, I asign it the None object.

When adjusting the basket or removing an item, I cycle through the list of dictionary's and check whether the size, side and gender in the dictionary match what the user has submitted and update the quantity or remove the dictionary accordingly.

The view.py file in the bag app contain functions for managing the basket variable; add_to_basket, adjust_basket, remove_from_basket.

The size options users can select from are:
* Junior (jr)
* Extra Small (xs)
* Small (s)
* Medium (m)
* Large (l)
* Extra Large (xl)

The side options users can select from are:
* Right-Handed (right)
* Left-Handed (left)

The gender options users can select from are:
* Male (male)
* Female (female)

#### Contexts

Within the basket app, there is a contexts.py file which is added to the list of context_processors within the global settings.  This makes the variables within it available throughout my website.  Within it, I create variables for the total cost of the items in the basket (total), total number of items in the basket (product_count), cost of delivery (delivery) and the total cost of the items in the basket plus delivery (grand_total).  There is also a list (basket_items) of products which uses the basket variable in session memory to unpack details of the products the user has added to their basket.

The basket_items varable stores the unique product id, the product object from the Products model and a details list.  The details list consists of dictionary's.  If the product has at least of the size, side or gender attributes, the dictionary's will contain all of these attributes.  If the product doesn't have any of these attributes, the details list will only have one dictionary which will be the quantity.

So for products with no size, side or gender, the structure in the basket_items list is:

{'item_id': product_id, 'product': Product(object), 'details': [{'qty': quantity}]}

For products which have at least one attribute (either size, side, gender),  the structure in the basket_items list is:

{'item_id': product_id, 'product': Product(object), 'details': [{'qty': quantity, 'size': size, 'side': side, 'gender': gender}]}

The data structure allows for product details, quanities and where applicable, attributes to be unpacked in the basket page using Jinja.

## Features

### Existing Features

### Features Left To Implement

- Add products which are specifically male/female and provide filter i.e. Clothing -> Men, Clothing -> Women.
- Stock levels including out of stock message 'if stock count == 0'.
- Subscribe to mailing list feature.

## Languages

* HTML
* CSS
* JavaScript
* Python

## Technologies Used

 - [Django](https://www.djangoproject.com/)
 - [Bootstrap5](https://getbootstrap.com/)
 - [jQuery](https://jquery.com/)
 - [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/)
 - Pillow
 - [Crispy Forms for Bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5)

## Services Used

## Testing

### Bugs Encountered During Development

#### Search Placement

Whilst building the header and navbar, I wanted the search box to be appear and disapear via a toggle button.  However, I only wanted this to apply to small screens; on medium screens (768px) upwards, I wanted the search box to remain visible in the header.  I initially tried to achieve this with jQuery applying jQuery UI effects to achieve a smooth dropdown transition.  The problem I encountered here was getting the search box to not be visible by default on small screens but always be visible on large screens.

I added the classes "d-none" and "d-md-block" to the #nav-search element.  This ensure that the elements initial state was correct.  However, getting jQuery to override the "d-none" class on small screens was a challenge.  I tried chaining toggle effects with toggling classes too to add/remove the "d-none" class.  However, this meant the transition was not smooth; the element would show after the effect had been applied or be hidden before the effect had been applied.

I ended up utilising [Bootstrap's collapse](https://getbootstrap.com/docs/5.0/components/collapse/) component to reach a solution.  Applying the "collapse" class to the #nav-search meant I could control have it hidden by default but toggle it's visibility using the #search-button element in the header.  I changed the #search-button to a button rather than a div to ensure semantic rules were followed and then applied some Bootstrap classes and custom CSS to achieve the desired styling.  Finally, I after the "collapse" class, I added the class "d-md-block" to the #nav-search element.  The reason for this is to ensure that it is always visible on medium screens upwards.  Whilst the visibility of this can still be toggled by the #search-button, this element is hidden on medium screens upwards so it cannot be clicked.

![Navbar search functionality](media/readme/gifs/navbar-search.gif)

#### Navbar JavaScript

On medium screens upwards, the navbar sits below the header whilst on small screens, it is shown/hidden using the menu button in the header.  On medium screens, I wanted the navbar to disappear when users scrolled down and then reappear when they scroll up.  The reason I wanted to do this was to preserve real estate space on screen.  To help achieve this, I referenced a solution on [w3schools.com](https://www.w3schools.com/howto/howto_js_navbar_hide_scroll.asp).

However, since I only wanted to apply this effect on medium screens upwards, I check the screen width.  If the screen width is greater than or equal to 768px, the effects are applied depending on the direction of scrolling.  However, when I tested the result of this effect, I noticed a bug.  When scrolling down on a medium screen, the navbar is hidden.  If the user then changes the screen size to a small screen, the navbar remains hidden and can no longer be toggled by the menu button:

![Navbar dropdown not working](media/readme/gifs/navbar-menu-bug.gif)

To resolve this, I searched Google and found another function I could use to resolve the problem.  Since this unique bug only occurs when the user changes the screen width, I created a function which is called every time the screen is resized.  I read up about the resize() method on [w3schools.com](https://www.w3schools.com/jquery/event_resize.asp).  When the screen is resized, I check the screen width again and if it is less than 768px, I show the navbar.  This means it can be toggled by the menu button as desired:

![Navbar dropdown fixed](media/readme/gifs/navbar-menu-fix.gif)

#### Remove from Basket

To remove items from the basket in the Basket page, JavaScript is utilised to post data and remove an item from the basket.  Using if statements, hidden data is included in the post data for the items size, side and gender as applicable.  The remove_from_basket function in the bag app views.py file is called to handle the request.  Within the function, I check whether any size, side or gender has been provided.  If not, I remove (pop) the item from the basket variable stored in session memory.  If it does have any one of these variables, then the product must have details so the value in the basket dictionary will be a list.

I cycle through the list of dictionary's and search for the item with the corresponding details to delete.  To achieve this, I check each dictionary to compare the size, side and gender variables.  When I find a match for all 3, I remove the dictionary from the list.  The issue I encountered when building this function is that where there is no such variable, rather than the None object being passed to the function and None string is passed.

As an example, if I had cricket gloves in my basket which have a size and side but no gender, the size and side passed to the remove_from_basket function were correct but the gender was a None string.  When cycling through the dictionary's in the basket, any cricket gloves in there will have a size and side but the gender is a None object.

When comparing each detail to check for a match, I never achieved one since the gender None string is not equal to the gender None object in the basket.  To overcome this, I inserted a series of if statements at the start of the function.  Once the size, side and gender variables have been retrieved from the request, I check each of them in turn to see whether any of them are equal to a None string (e.g. if size == 'None':), and if so, make the variable equal to the None object (size = None).  This meant that when checking the dictionarys for an item which matched the one the user is trying to delete, a match was found and the dictionary could then be removed.

Finally, to ensure that no empty lists are left in the basket, I check see if there are any of that product left in the basket and if not (e.g. the list is empty), I remove it from basket.

#### Toasts - Positioning

When creating the toast messages, I decided I wanted them to appear beneath the header but with a fixed position on top of existing content.  To achieve this, I gave the toast box a fixed position and z-index of 9999999 to ensure it overlays all other content.  Setting the position relative to the top of the page was a little tricky though.  The header height varies; on small and medium screens it is 53 pixels while on larger screens it varies between 53 pixels and 93 pixels depending on if the navbar is visible.  By setting the position to the top at 93 pixels, there would occasionally be white space between the header and the toast which I don't think looks very good:

![Toast messages with a gap between the header and the toast](media/readme/images/toasts-gap.png)

To resolve this, I utilised jQuery and CSS.  Within my base.css file, I set the toast position to 93 pixels from the top but used a media query to reduce this to 53 pixels on screen sizes up to 768px wide.  Then, using the jQuery functions I created to hide and show the navbar on large screens, I add and remove a class to the toasts called 'toast-up' which changes the position to the top of the page to 53 pixels.  By setting the same transition speed to the navbar hide/show and the toast add/remove class, the toasts move up and down in line with the navbar on large screens but sit under the header on small and medium screens:

![Toast messages position synced to the bottom of header](media/readme/gifs/toasts-up-down.gif)

#### Order Grand Total

As I develpoed the checkout models, I stumbled upon an issue with the format of my order total (order_total) and the delivery total (delivery_cost).  The order total is the sum of all of the order items multiplied by the corresponding quantities.  It uses the Django DecimalField to store the value as a decimal.  The delivery cost comes from the global settings but is a float with value 6.99.  When adding the two values together to get the grand total (grand_total), I received the below error caused by trying to add two variables of different type together:

![Failure message received when adding float type to decimal type](media/readme/images/decimal-plus-float.png)

To overcome this, I turned to Google and found a [simple solution](https://stackoverflow.com/questions/316238/python-float-to-decimal-conversion).  I decided to convert the delivery cost variable into a decimal.  To achieve this, I simply imported the Decimal function (from decimal import Decimal) and passed the delivery cost variable into it.  Doing some further reading, I discovered that simply converting a float to decimal often introduces a rounding error.  Whilst the grand total is stored as decimal too with 2 decimal places so any rounding errors shouldn't cause an issue, I read that best practice is to convert the variable to a string before converting it to decimal.  Using the print function, I compared the outputs when converting the delivery cost to decimal:

6.9900000000000002131628207280300557613372802734375

When converting the delivery cost to a string and then a decimal this was the output:

6.99

I decided it was best practice to convert the delivery cost to a string and and then a decimal.  With the delivery cost now the same variable type as the total cost, both decimal, I was able to successfully add the two variables together.



### Testing Process

*Try to use an Aim, Methodology, Result layout. A user should be able to read the Testing document, carry out the same tests on the live site and get the same results.  Try testing the user stories comprehensively in terms of Features and Responsivity to get a better grade.  Include evaluation of bugs found and their fixes and explanation of any bugs that are left unfixed.  Test the UX thoroughly.*

#### Responsive Design

* Basket page is responsive but the quantity buttons begin to misalign when the screen width is reduced down to 332px wide.  However, I believe this is not an issue since [modern mobiles](http://www.javascriptkit.com/dhtmltutors/cssmediaqueries2.shtml#:~:text=Most%20mobile%20phones%20have%20a,CSS%20pixel%20on%20the%20screen.) are wider than this.

### Bugs Encountered During Testing

## Deployment

*Fully document the deployment procedure in a section in a README file.  Explain all steps taken to deploy project on both GitPod and Heroku.*

### GitPod Environment

I created my GitHub repository (repo) by using the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template).  I named my repo "Stumps-and-Studs-MS4".  I opened this repo in GitPod.

### Packages Installed

From within GitPod, I installed a number of packages:
*   [Django](https://www.djangoproject.com/) - *pip3 install django*
*   [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/) - *pip3 install django-allauth*
*   [Pillow](https://pillow.readthedocs.io/en/stable/index.html) - *pip3 install pillow*
*   [Crispy Forms](https://github.com/django-crispy-forms/crispy-bootstrap5) - *pip3 install django-crispy-forms*
*   [Crispy Forms for Bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5) - *pip3 install crispy-bootstrap5*
*   [Stripe](https://stripe.com/docs/api) - *pip3 install stripe*

The project is deployed on Heroku which will need to know which packages to install in order to correctly host my finished project.  I kept an updated list of all of the installed packages in the requirements.txt file using this command:
* *pip3 freeze > requirements.txt*

### Create The Django Project

With Django installed, I created my project by running this command:
*   *django-admin startproject stumps_and_studs .*

To create the various apps, I used the following command:
*   *python3 manage.py startapp* app_name

### Environment Variables

The Code Institute GitPod template already comes with a .gitignore file so I did not need to create one.  Any files listed in this document are not pushed to GitHub which ensures environment variables which need to remain private and secure are not made publicly available within my repo.

### Setting Up The Database

Django comes with a default database file called db.sqlite3.  For security reasons, this file suffix is listed in the .gitignore file to ensure the database isn't pushed to GitHub.

To update the database when a new models was created, I ran the following commands:
*   *python3 manage.py makemigrations --dry-run* - This tells us what would happen if we actually ran the command.
*   *python3 manage.py makemigrations* - Django sees that we've added a new model to our app so it creates a new Python file in the migrations folder that contains the code to create that database table based on our model.
*   *python3 manage.py showmigrations* - Lists all migrations with [X] indicating those that have been done already and [ ] indicating those that need to be migrated.
*   *python3 manage.py migrate --plan* - Lists all of the changes that will be made to the database and various field settings without executing changes to the database.
*   *python3 manage.py migrate* - Executes the migration and changes to the database are made.

The db.sqlite3 database was used in the development of my project from within the GitPod environement.

### Create Admin Superuser

Django includes a built-in admin function which enables users to log in and look at the tables in our database and make changes to them.  To create a superuser, I ran the following command:
*	 *python3 manage.py createsuperuser*

### Deploy Application To Heroku

### Connecting Django Application To Postrgres Database

### Using Flask Template Inheritance

## Credits

### Inspiration

### Content

For the About Us section in the footer, I referenced the text on [JD Sports website](https://www.jdsports.my/customer-service/about-us/) but tweaked some elements of my fictional companies history.

### Media

I wanted prominent images to be high resolution so sourced them from sites such as [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/):

*   [Home Page Cricketers](https://www.pexels.com/photo/man-people-stadium-game-3718433/)
*   [Home Page Golfer](https://www.pexels.com/photo/man-walking-carrying-black-and-red-golf-bag-on-green-grass-field-1325681/)
*   [Home Page Running Shoes](https://www.pexels.com/photo/people-doing-marathon-618612/)
*   [Home Page Clothing](https://www.pexels.com/photo/three-women-kneeling-on-floor-866023/)

Whilst I would idealy have been able to use high resolution images for my products, I struggled to find suitable images for them.  Instead I downloaded them from a variety of ecommerce stores such as [Amazon](https://www.amazon.co.uk/), [American Golf](https://www.americangolf.co.uk/) and [Decathlon](https://www.decathlon.co.uk/):

I used Google to find a 'no image' image.  The one I chose was sourced from [this website](https://www.allianceplast.com/no-image/).

### Acknowledgements
