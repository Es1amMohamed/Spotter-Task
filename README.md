# Library Management System with Django

This project is a Django RESTful API for managing books and authors, including user authentication, search functionality, and a recommendation system. It is designed to help users manage a library system, with endpoints for CRUD operations on books and authors, as well as user registration and login.

## Features

- **Books API**:
  - **GET /books**: Retrieve a list of all books.
  - **GET /books/:id**: Retrieve a specific book by ID.
  - **POST /books**: Create a new book (protected, admin only).
  - **PUT /books/:id**: Update an existing book (protected, admin only).
  - **DELETE /books/:id**: Delete a book (protected, admin only).

- **Authors API**:
  - **GET /authors**: Retrieve a list of all authors.
  - **GET /authors/:id**: Retrieve a specific author by ID.
  - **POST /authors**: Create a new author (protected, admin only).
  - **PUT /authors/:id**: Update an existing author (protected, admin only).
  - **DELETE /authors/:id**: Delete an author (protected, admin only).

- **Authentication**:
  - **POST /register**: User registration with JWT authentication.
  - **POST /login**: User login with JWT authentication.
  - Protected endpoints for creating, updating, and deleting books/authors.

- **Search Functionality**:
  - Search books by title or author name using query parameters.

- **Recommendation System**:
  - Users can add/remove books from their favorites list.
  - Recommendations for similar books based on the entire favorites list.
  - Maximum of 20 favorite book titles.
  - Recommendations returned in less than 1 second.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Es1amMohamed/Spotter-Task.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Spotter-Task
    ```

3. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

7. **Create a superuser (for admin access)**:
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## API Documentation

- **Books Endpoints**:
  - **GET /books**: Lists all books.
  - **GET /books/:id**: Retrieves a book by ID.
  - **POST /books**: Creates a new book (admin only).
  - **PUT /books/:id**: Updates a book (admin only).
  - **DELETE /books/:id**: Deletes a book (admin only).

- **Authors Endpoints**:
  - **GET /authors**: Lists all authors.
  - **GET /authors/:id**: Retrieves an author by ID.
  - **POST /authors**: Creates a new author (admin only).
  - **PUT /authors/:id**: Updates an author (admin only).
  - **DELETE /authors/:id**: Deletes an author (admin only).

- **Authentication**:
  - **POST /register**: Register a new user.
  - **POST /login**: Login a user.

- **Search**:
  - **GET /books?search=query**: Search for books by title or author.

- **Recommendations**:
  - **POST /favorites**: Add a book to favorites and receive recommendations.
  - **DELETE /favorites/:id**: Remove a book from favorites.

## Recommendation System

The recommendation system uses TF-IDF vectorization and cosine similarity to suggest similar books based on a user's favorites list. Recommendations are generated quickly to ensure a responsive user experience.

## Testing

- **Testing Response Times**: Use tools like `curl` or Postman to test the response times of the recommendations endpoint and ensure they meet the requirement of less than 1 second.

## Contributing

Feel free to fork this repository and submit pull requests. If you encounter any issues or have suggestions, please open an issue on GitHub.


## Contact

For any inquiries, please contact [your email](mailto:eslammohamemetwaly@gmail.com).


