# Python API Development Assignment

## Short description

In this coding assignment I have implemented a CRUD (Create, Read, Update, Delete) API with a database deployed in Heroku Postgresql.
To implement this assignment I have used Django framework and have deployed the API on Heroku cloud hosting provider. I have created a sample dataset for books with name, isbn,  authors, country, number_of_pages, publisher release_date as its attributes.

You can access the API using following API call:

```sh
https://balajibookmanagementapp.herokuapp.com/api/book/
```

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/balaji2245/django_project_externalapi.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/balaji2245/`.


## Walkthrough

I have deployed the working API on Heroku, you can see use following website to look at its woking:

```sh
https://balajibookmanagementapp.herokuapp.com/api/book/
```

The backend dataset which I have used is postgresql deployed on Heroku cloud platform. You can add, read, update or delete any record from the dataset. Below I have given examples for the CRUD operations which you can perform on the dataset.


### Create
For creating a new Book record, you can either use above mentioned website and add the record as shown in the adjacent screenshot using UI provided or you can as well use an API testing tool like Postman.

![1](https://user-images.githubusercontent.com/40818500/141831935-6280ec51-4bf0-44a5-85b8-a2dd1d71a776.png)

Or you can use Postman as shown below to create a new book record:

![2](https://user-images.githubusercontent.com/40818500/141832711-92423c3e-96b5-46db-a70c-cade76eb10bf.png)


### Read
For reading the book dataset which I have uploaded on Heroku postgresql cloud services, we can hit the API using above given link and can get the response in JSon as shown below:

![3](https://user-images.githubusercontent.com/40818500/141833122-ac98973c-5993-40af-a757-a84f4b18fa2d.png)

Or you can use Postman as shown below to read the books dataset:

![4](https://user-images.githubusercontent.com/40818500/141834742-7700e1ba-d0f0-4734-be82-95decea76d68.png)

You can also fetch a particular book info with by providing the book id as below:

![6](https://user-images.githubusercontent.com/40818500/141839409-35de71c6-cb3f-4fb5-a4df-9b5c9b4830d3.png)

Same thing we can do using Postman or any other API testing tool as well:

![5](https://user-images.githubusercontent.com/40818500/141833854-75abf427-1d09-446e-8aad-654d1156483b.png)


### Update

As shown below, we can update a record by calling the API by "https://balajibookmanagementapp.herokuapp.com/api/book/4/" and using PUT option given at the bottom as follows:

![7_1](https://user-images.githubusercontent.com/40818500/141838896-6b2da5b9-c48b-4685-a7cf-8ba8b5ddb62d.png)

To update a record in our dataset we can call our API using PUT method as shown below, here I have changed the ISBN number of book named "balaji book".

![7](https://user-images.githubusercontent.com/40818500/141835248-992b75f3-2f47-444a-bd16-7bf98744201e.png)


### Delete

We can delete a record from the dataset by by calling the API as follows, for example here I've tried deleting the book record with id 1 by calling 
```sh
https://balajibookmanagementapp.herokuapp.com/api/book/1/
```
we get an option to delete it as shown in the screenshot below:

![8_1](https://user-images.githubusercontent.com/40818500/141837803-f5f0f7b7-c51f-439d-9ee5-e36c4ccb4067.png)

Or we can also use Postman to delete a record from our dataset, we need to call our API using DELETE method which I have shown below:

![8](https://user-images.githubusercontent.com/40818500/141837480-74085288-1bf2-4bb2-bd6b-c754d11f982c.png)

Thus, after deleting 8th record we have our dataset as follows:

![9](https://user-images.githubusercontent.com/40818500/141839766-6a0480d4-a0da-4274-b6b8-5ee4a6c8fb81.png)


