# Social Media App Backend

This repository contains the backend implementation of a social media application, focusing on creating a set of APIs for various functionalities such as user registration, post creation, interaction, group management, and more.

## Features

- User Registration and Login
- User Profile Management
- Create, Update, and Delete Posts (Text, Images, Videos)
- Like and Unlike Posts
- Share (Repost) Posts from Other Users
- Follow/Unfollow Other Users
- Create, Manage, Join, and Leave Groups
- Comment on Posts and Reply to Comments
- List Followers and Following
- Search for Users, Posts, and Groups

## Technology Stack

- Django (Web Framework)
- Django REST Framework (API Framework)
- SQLite (Database)
- Token Authentication

# Usage

1. Access the API endpoints through the provided URL routes.
2. Use tools like Postman or curl to interact with the APIs.
3. Register users, create posts, interact with posts, join groups, and more.

## API Endpoints

- `/register/`: User registration endpoint.
- `/login/`: User login endpoint.
- `/profile/`: User profile management endpoint.
- `/posts/`: List and create posts endpoint.
- `/posts/<int:pk>/`: Retrieve, update, and delete a specific post.
- `/posts/<int:pk>/like/`: Like a post.
- `/posts/<int:pk>/share/`: Share (repost) a post.
- `/follow/`: Follow another user.
- `/comments/post/`: Comment on a post.
- `/replies/comment/`: Reply to a comment.
- `/groups/`: List and create groups.
- `/group-memberships/`: Manage group memberships.
- `/followers/` and `/following/`: List followers and following.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, and suggest improvements.
