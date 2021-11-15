# Python API Development Assignment (Ice and Fire API)

## Short description

In this coding assignment I have implemented a REST API that calls an external API service of Ice and Fire and gets information about the books. 

Mainly there are two kinds of works this REST API call does, 1. Getting the information of all the books available in the Ice and Fire dataset and 2. Getting the information about a particular book provided its name in the url in the format required " .../?name=nameOfBook".

You can access the API using following API call:

```sh
https://balajiiceandfireapi.herokuapp.com/
```


## Walkthrough

I have deployed the working API on Heroku, you can see use following website to look at its woking:

```sh
https://balajiiceandfireapi.herokuapp.com/
```

### Getting whole dataset

The REST API call above calls the Ice and Fire API and showcases the complete book dataset of it as follows:

![1_1](https://user-images.githubusercontent.com/40818500/141842098-3d750ac5-da58-4d5f-9aa3-85f573d0f4eb.png)

Thus showcasing the whole book dataset with required attributes as requested in the assignment name, isbn, authors, number_of_pages, publisher, country rerlease date.
Here, in this API, I have worked on removing the unwanted attributes recieved from the Ice and Fire API call which were url, characters, mediaType and povCharacters.


The backend dataset which I have used is postgresql deployed on Heroku cloud platform. You can add, read, update or delete any record from the dataset. Below I have given examples for the CRUD operations which you can perform on the dataset.


### Getting information of a particular book by it's name

The following REST API call designed by me fetches the information of the only book requested by it's name. Here, in the example below, I have tried fetching the information of book named "The Princess and the Queen".

```sh
https://balajiiceandfireapi.herokuapp.com/?xsxs=The%20Princess%20and%20the%20Queen
```

I have attached the screenshot wherein we can see that we have got the information of the particular book in the desired format below:

![1_2](https://user-images.githubusercontent.com/40818500/141843435-160deacf-1088-486f-8737-a67249c7ab10.png)


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


