from .util import *


class __THMUser(object):
    def user_exists(self, username) -> bool:
        """
        Checks if a username is taken

        :param username: Username to check
        :return:
        """

        return http_get(self.session, f'/api/user/exist/{username}')['success']

    def user_created_rooms(self, username) -> list:
        """
        Gets a list of rooms created by a user

        :param username: Username to check
        :return: List of rooms created by this user
        """

        return http_get(self.session, f'/api/created-rooms/{username}', has_success=True)['rooms']

    def user_all_completed_rooms(self, username) -> list:
        """
        Gets all rooms completed by a user

        :param username: Username to check
        :return: List of rooms (with all data) completed by this user
        """

        return http_get(self.session, f'/api/all-completed-rooms?username={username}')

    def user_badges(self, username) -> list:
        """
        Gets the list of badges a user has

        :param username: Username to check
        :return: List of badges
        """

        return http_get(self.session, f'/api/badges/get/{username}')

    def user_activity(self, username) -> list:
        """
        Gets the user's activity feed

        :param username: Username to check
        :return: List of events
        """

        return http_get(self.session, f'/api/activity-events?username={username}', has_success=True)['data']

    def user_discord(self, token) -> dict:
        """
        Gets the user's data from his discord integration token

        :param token: Discord integration token
        :return: User data
        """

        return http_get(self.session, f'/discord/user/{token}', has_success=True)

    def user_rank(self, username) -> int:
        """
        Gets the user's rank

        :param username: Username to check
        :return: User's rank
        """

        return http_get(self.session, f'/api/user/rank/{username}')

