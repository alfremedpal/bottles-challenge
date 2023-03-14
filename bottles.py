class BottleSong:
    """Sing the Bottles of Beer song

    sing -- Return the song's full lyrics
    sing_one -- Return one verse of the lyrics
    sing_range -- Return a range of verses
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

    def sing_one(self, bottle_count, display=True, range=None):
        """Display one verse of the lyrics

        Keyword arguments:
        bottle_count -- The line and bottle number to return (required)
        display -- print out the result to the console (default: true)
        range -- used to print out correctly total number of bottles when using sing_range method
        """
        if bottle_count == 0:
            verse = self.get_no_bottles(bottle_count=range)
        else:
            verse = f"""{bottle_count} {self.check_container_plural(bottle_count)} of {self.drink} on the wall, {bottle_count} {self.check_container_plural(bottle_count)} of {self.drink}.
Take one down and pass it around, {'no more' if bottle_count - 1 == 0 else bottle_count - 1} {self.check_container_plural(bottle_count - 1)} of {self.drink} on the wall.\n\n"""

        if display:
            print(verse)

        return verse

    def sing_range(self, start, finish, display=True):
        """Return range of verses in range [start, finish) = {start >= 0, finish >= -1}

        Keyword arguments
        start -- Number of verse to start from (inclusive)
        finish -- Number of verse to finish in (exclusive)
        """
        if start < finish:
            raise ValueError(
                f"Ending verse ({finish}) must be lower than starting verse ({start})"
            )
        elif finish < -1 or start < 0:
            raise ValueError(
                f"Ending verse ({finish}) cannot be lower than -1 and starting verse({start}) cannot be lower than 0"
            )

        verses = ""
        if start == finish:
            verses = self.sing_one(start, display=False)
        else:
            for bottle_count in range(start, finish, -1):
                verses += self.sing_one(bottle_count, display=False, range=start)

        print(verses) if display else None

        return verses

    def get_no_bottles(self, bottle_count=None):
        """Returns the corresponding verse when there are no more bottles"""
        if bottle_count is None:
            bottle_count = self.n

        return f"""No more {self.check_container_plural(0)} of {self.drink} on the wall, no more {self.check_container_plural(0)} of {self.drink}.
Go to the store and buy some more, {bottle_count} {self.check_container_plural(0)} of {self.drink} on the wall."""

    def check_container_plural(self, bottle_count):
        """Returns correct format on container depending on count"""
        container = self.container
        if bottle_count != 1:
            container = f"{container}s"

        return container


if __name__ == "__main__":

    bottle = BottleSong()
    # bottle.sing()
    # bottle.sing_one(3)
    # bottle.sing_one(2)
    # bottle.sing_one(1)
    # bottle.sing_one(0)
    bottle.sing_range(6, -1)
