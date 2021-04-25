class UserInfo:
    def __init__(self, name):
        self.login = name
        self.stars = 0
        self.repositories = []

    def count_stars(self):
        return sum(item.get('stars') for item in self.repositories)

    def return_user_info(self):
        self.stars = self.count_stars()
        return {'login': self.login, 'all_stars': self.stars, 'repositories': self.repositories}

    def return_stars(self):
        return {'all_stars': self.count_stars()}

    def return_repos(self):
        return self.repositories
