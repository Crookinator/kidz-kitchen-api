# App Description

Kids Kitchen is an app for aspiring young cooks to keep track of their recipes. It is designed to be a fun and supportive tool for children to be inspired to love cooking and to be creative.

## Related Links
### Live Site
https://crookinator.github.io/kidz-kitchen

### API
Heroku App: https://kidz-kitchen.herokuapp.com 

### Client
GitHub client site: https://github.com/Crookinator/kidz-kitchen

## Installation

1. Fork and clone this repo.
1. Switch to the new directory in terminala
1. Create and checkout to a new branch.
1. Run `pipenv shell` to step into the python virtual environment.
1. Run `pipenv install` to install dependencies.
2. Create a psql database on your local machine for your testing
    1. Edit `settings.sql` then run `psql -U postgres -f settings.sql`
    OR:
    1. Type `psql` to get into interactive shell.
    2. Run `CREATE DATABASE "project_db_name";` where `project_db_name` is the name you want for your database.
1. Add the database name to the `.env` file using the key `DB_NAME_DEV`.
2. Generate a secret key using [this tool](https://djecrety.ir) and add it to the `.env` file using the key `SECRET`.

## Commands

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |

## About

Kidz Kitchen was created with love. My son in very much into cooking and this was a request straight from him. This app is built with the thought that kids can have a place to keep track of there recipes and also gain inspiration from the generate recipe feature found in the recipe dropdown. This feature is querying a third party API called recipepuppy.

## User Stories

As a user I would like to sign-up, sign-in, change my password, and sign-out.
As a user I would like to create a recipe with a title, description, instructions, ingredients, cuisine.
As a user I would like to see, update, or delete my created recipe.

## ERD
User -|< Recipe

## Planning and Problem Solving

For this project I relied heavily on my prior knowledge throughout the course. I used what I learned in past projects to better prep and complete features I wanted. I fully thought out the app and styles I wanted and also pre planned some of the code to make the development time faster.

## Unsolved / Future Features

In the future versions of this app I would like to have a second resource called profile. This would be a OneToOneField in django. This resource would be to let each user to set an about me, favorite cuisine, and name. I would also like to include images for food. 

### Catalog of routes

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-up/`             | `users#signup`    |
| POST   | `/sign-in/`             | `users#signin`    |
| PATCH  | `/change-pw/` | `users#changepw`  |
| DELETE | `/sign-out/`        | `users#signout`   |
| GET    | `/recipes/`            | `recipes#index`     |
| GET    | `/recipes/:id`        | `recipes#show`      |
| POST   | `/recipes/`            | `recipes#create`    |
| PATCH  | `/recipes/:id/`        |  `recipes#update`   |
| DELETE | `/recipes/:id/`        | `recipes#delete`    |


## Technologies Used
django
python
postgresql
heroku
GIT
GitHub