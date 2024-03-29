class User:
    def __init__(self, username):
        """
        This is the constructor for the User class
        Args:
           param username: username: the name of the user
        The object has a list of following
        """
        self.username = username
        self.following = []

    # Time complexity: O(n) because we iterate over the list(that include n following)
    def follow(self, other_user):
        """
        Args:
         param other_user: the user that we want to add to the following list
        if the other_user is not in the username list, it appended to this list
        """
        if other_user not in self.following:
            self.following.append(other_user)

    # Time complexity: O(1) because we have just append item in the end of the list - one operation
    def post_message(self, message):
        """
        Args:
            param message: the message that the user posted
        every message that the user posted,it will append to the post dictionary
        """
        post = {'username': self.username, 'message': message}
        posts.append(post)


# Assume posts are stored in a global list
posts = []
