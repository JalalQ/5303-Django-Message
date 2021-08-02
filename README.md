# Introduction
This project was completed as part of HTTP5303 course, during which I had to learn a new web programming language of my choice and implement it. I choose to work with Django Python to create a simple message board app. The following book was used for my independent self-study.

> Vincent, William S. Django for Beginners: Build websites with Python and Django. WelcomeToCode, 2020.

**The final deployment with CSS rendering can be found from [this weblink](https://whispering-cove-79249.herokuapp.com/).**

## Technical notes
* To verify whether Python is installed on my laptop, type the following command.```$ python --version```

* After installing django, its installation can be verified as,```$ django-admin --version```

* Install pipenv. Run the folowing using the Anaconda environment ``pip install pipenv``

* To ensure that the djngo localserver is working, ```$ python manage.py runserver```

* And type the following address in the browser address bar. ```http://127.0.0.1:8000/```

![django](https://user-images.githubusercontent.com/58306478/120021622-4dcbf800-bfb9-11eb-810a-edfba64d8dc4.jpg)

## Task lists
Django uses the concept of projects and apps to keep code clean and readable. For example, a real-world Django e-commerce site might have one app
for user authentication, another app for payments, and a third app to power item. The following is a summary of some of the major steps during my project.

- [x] Using Template to display multiple pages.
- [x] Reusing the header.html view on multiple pages as a navigation bar.
- [x] Create a new folder, and run a virtual environment on that folder.
  * ``pipenv install django``
  * ``pipenv shell``
- [x] **Virtual Environments**: They are an isolated container containing all the software dependencies for a given project. The virtualenv tool is a utility that separates all the Python projects in their own realms. **Pipfile** is the dedicated file used by the Pipenv virtual environment to manage project dependencies.
- [x] create an initial database based on Django's default settings, ``python manage.py migrate``. This will create a SQLite database.
- [x] Create a database model in models.py file.
- [x] Activating models. 
 * ``python manage.py makemigrations posts``
 * ``python manage.py migrate posts``
- [x] Create an admin superuser. ``python manage.py createsuperuser``.
- [x] Added additional fields in the message (Post) table.
- [x] Connected the Post table with the auth.User table.
- [x] Used CSS style file to improve the presentation of the view home page.
- [x] Used values from multiple tables by appropriately setting up the model view, to display on a single view page.
- [x] Deployment on Heroku
  * ``git init``
  * ``git add .``
  * ``git commit -m "Deployment"``
  * ``heroku login``
  * Add the Procfile file at the root file. Ensure that the project name is reflected in the file name.
  * ``pipenv install gunicorn``
  * ``heroku create ``
  * ``heroku git:remote -a #APP-NAME#`` Where APP-NAME will need to be based on the name used on Heroku.
  * ``heroku config:set DISABLE_COLLECTSTATIC=1``
  * ``git push heroku main``
  * ``heroku ps:scale web=1``
  
## Task Challenge
The challenge which I faced was that on my localserver view the CSS file was getting rendered, but it was not getting rendered when deployed on the Heroku server. I was able to resolve this issue by looking up for resource on internet. [This resource](https://devcenter.heroku.com/articles/django-assets) in particular was most helpful to me in debugging the issue.

## Screenshots
![post](https://user-images.githubusercontent.com/58306478/121212539-753d8300-c84b-11eb-990e-975586540204.jpg)

![admin_user](https://user-images.githubusercontent.com/58306478/121213125-f85ed900-c84b-11eb-8765-19bb5aefed13.jpg)

![list-posts](https://user-images.githubusercontent.com/58306478/121213616-64414180-c84c-11eb-9df4-471db6965aa7.jpg)

![message-board](https://user-images.githubusercontent.com/58306478/121213917-ad919100-c84c-11eb-905d-da6d2ee17dcd.jpg)

![DB-Browser-SQLite](https://user-images.githubusercontent.com/58306478/121988750-e52a9c80-cd68-11eb-89a7-e80a088faeb1.jpg)

![message-board](https://user-images.githubusercontent.com/58306478/121988752-e5c33300-cd68-11eb-861c-9cfa19dd05a2.jpg)
