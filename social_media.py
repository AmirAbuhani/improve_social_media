from user import User, posts


class SocialMediaPlatform:
    def __init__(self):
        """
        the SocialMediaPlatform class has a list of all the users in the platform
        """
        self.users = []

    # Time complexity: O(n*m) because this function called the _is_username_taken that has O(n*m) time complexity.
    #                 Creating a new user and appending it to the list is 0(1) operation. so the O(n*m) is the dominant
    def register_user(self, username):
        """
        Args:
             param username: a certain user to resister it
        This function is using the _is_username_taken to check if there is user in the platform.
        if not, it created a new user(username) and append it to the platform users list
        """
        if not self._is_username_taken(username):
            user = User(username)
            self.users.append(user)

    # Time complexity: O(n*m) because the function iterate over the list users(n size) and for each item in the size
    #                  it pass over the length of the user.username(m)
    def _is_username_taken(self, username):
        """
        Args:
            param username: a specific user that we well check
        return:
            True if this user exists in the users list
            False if not
        """
        for user in self.users:
            if user.username == username:
                return True
        return False

    # Time complexity: O(n*m), see the above explain
    def get_user_by_username(self, username):
        """
        Arge:
            param username: user that we check
        return:
            user: The function return the user object if it exists
            None: if the user not found
        """
        for user in self.users:
            if user.username == username:
                return user
        return None

    # Time complexity: O(n^2), because we have a nested for loop for each follower_user we iterate  his posts
    def generate_timeline(self, username):
        """
        Args:
             param username: the username that we want to check about
        return:
            timeline: list of all the posts of the user following
        """
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        for followed_user in user.following:
            for post in posts:
                if post['username'] == followed_user:
                    timeline.append(post)
        return timeline

    # Time complexity: O(n)
    def improved_generate_timeline(self, username):
        """
        Args:
             param username: the username that we want to check about
        return:
            timeline: list of all the posts of the user following
        """
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        # Dictionary to store posts by username
        user_posts = {}

        # Populate user_posts dictionary
        for post in posts:
            user_posts.setdefault(post['username'], []).append(post)

        # Retrieve posts for followed users from user_posts dictionary
        for followed_user in user.following:
            timeline.extend(user_posts.get(followed_user, []))

        return timeline
