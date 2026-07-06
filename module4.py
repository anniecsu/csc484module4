"""
User Management Module.
Provides the User class for representing user accounts
with id, username, and
email.

"""

class User:
    """
    Represents a user account.
    Attributes:
    id (int): Unique identifier
    username (str): Account username
    email (str): User email address
    """
    def __init__(self, id: int, username: str, email: str):
        """
        Initialize a User instance.
        Args:
        id: Unique user identifier (positive integer)
        username: Account username (non-empty string)
        email: User email address
        """
        self.id = id
        self.username = username
        self.email = email

    def get_id(self) -> int:
        """
        Return the user's ID.
        """
        return self.id

    def get_username(self) -> str:
        """
        Return the username.
        """
        return self.username

    def get_email(self) -> str:
        """
        Return the email address.
        """
        return self.email

# Usage Example
user = User(1, "johndoe", "johndoe@example.com")
user_id = user.get_id()
print(f"User ID: {user_id}")