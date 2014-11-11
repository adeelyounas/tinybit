tinybit
=======
Setup
-----
* Create Virtualenv
* pip install -r requirments.txt
* Run management script inorder to populate data ```python manage.py populate_initial_data```, this will copy all the data from text file to database

Accessing Application
---------------------
* Once the setup is done, runserver ```python manage.py runserver```
* Goto link on the browser ```http://localhost:8000/url/trimmer/```, there you will see the form with input field for URL you want trim (shorten), once you submit the form you will be redirected to same page along with the short link for the requested URL.


Further Improvements
--------------------
* Use cache when creating short url (store list of available names and build regex based on that instead of query DB on every request)

Know Issues
-----------
* Can encounter raise conditions, when request is made same time for same url 
