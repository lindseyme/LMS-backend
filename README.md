# Library Management System
Library management system enables the librarians to run the library smoothly and be able to get
all the necessary information in just a click.

## Functionality
- Create user accounts.
- Manage the user accounts.
- Add books to the system.
- Check for inventory ie available books and users.
- Borrow books.
- View the most popular books and genres.

## Api end points
| Method  | Endpoint          | Description                      |
| --------|:-----------------:| -------------------------------: |
| POST     | /api/users      | add a user                  |
| GET/PUT/DELETE    | /api/users/<int:user_id>       |    Get details/Edit details/Delete a user         | 
| POST     | /api/books     | Add a new book      |
| GET/PUT/DELETE     | /api/books/<int:book_id>     | Get details/Edit details/Delete a book   |
| POST     | /api/borrow         | Borrow a book                  |
| POST      |/api/return | Return a book |
| GET      |/api/inventory| Available books for borrowing |
| GET      | /api/overdue_books            | Get the list of books that are overdue               |
| GET    | /api/popular_books            | Get a list of the most popular books |
|GET     | /api/popular_genres              | Get a list of the most popular genres                |
## Prerequisites
- Set up the postgresql database.
- Configure the database name, password and portnumber in 'config.py'.

## installed packages
- Python 3.12.2

- Install necessary requirements

  ```
  $ pip install -r requirements.txt
  ```

- Run development server
  ```
  $ python run.py
  ```

This site should now be running at http://localhost:5000

