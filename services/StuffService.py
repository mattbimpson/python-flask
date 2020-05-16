class StuffService():

    def __init__(self):
        self.stuff = [
            {
                'id': 0,
                'title': 'first thing'
            },
            {
                'id': 1,
                'title': 'second thing'
            }
        ]

    def get_all(self) -> list:
        return list(self.stuff)