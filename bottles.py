class BottleSong:
    """Sing the Bottles of Beer song

    sing -- Return the song's full lyrics
    sing_one -- Return one verse of the lyrics
    """

    def __init__(self, n=99, container="bottle", drink="beer"):
        """Constructor

        Keyword arguments:
        n -- Number of bottle to start singing from (default: 99)
        container -- Type of container (default: bottle, must singular)
        drink -- Type of drink (default: beer)
        """
        self.n = n
        self.container = container
        self.drink = drink

    def sing(self, display=True):
        """Returns and displays the song's lyrics

        Keyword arguments:
        display -- print out the result to the console (default: true)
        """
        full_lyrics = ""

        for bottle_count in range(self.n, -1, -1):
            full_lyrics += self.sing_one(bottle_count, display=False)

        if display:
            print(full_lyrics)

        return full_lyrics

    def sing_one(self, bottle_count, display=True):
        """Display one verse of the lyrics

        Keyword arguments:
        bottle_count -- The line and bottle number to return (required)
        display -- print out the result to the console (default: true)
        """
        if bottle_count == 0:
            verse = self.get_no_bottles()
        else:
            verse = f"{bottle_count} {self.check_container_plural(bottle_count)} of {self.drink} on the wall. {bottle_count} {self.check_container_plural(bottle_count)} of {self.drink}. Take one down, pass it around, {bottle_count - 1} {self.check_container_plural(bottle_count - 1)} of {self.drink} on the wall\n"

        if display:
            print(verse)

        return verse

    def get_no_bottles(self):
        """Returns the corresponding verse when there are no more bottles"""
        return f"No more {self.check_container_plural(0)} of {self.drink} on the wall, no more {self.check_container_plural(0)} of {self.drink}. Go to the store and buy some more, {self.n} {self.check_container_plural(0)} of {self.drink} on the wall..."

    def check_container_plural(self, bottle_count):
        """Returns correct format on container depending on count"""
        container = self.container
        if bottle_count != 1:
            container = f"{container}s"

        return container


if __name__ == "__main__":

    bottle = BottleSong(drink="milk", container="can", n=89)
    bottle.sing()
    # bottle.sing_one(3)
    # bottle.sing_one(2)
    # bottle.sing_one(1)
    # bottle.sing_one(0)
