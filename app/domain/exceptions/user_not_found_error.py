class UserNotFoundError(Exception):
    def __init__(self):
        self.message = "User could not be found in database"
        super().__init__(self.message)
