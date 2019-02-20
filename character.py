# name
# avatar (profile picture)
# inventory

# def do_stuff():
#   pass


class Character():  # classes start with uppercase and usually singular
    # the "dunder init" method is the constructor
    def __init__(self, new_name, new_avatar):
        # `self` is the customary way to refer to the instance being built
        # In some other languages, they use `this`
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
