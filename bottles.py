class BottleSong:
    """Sing the Bottles of Beer song

    sing -- Return the song's full lyrics
    sing_one -- Return one verse of the lyrics
    """

    def __init__(self, n=99):
        self.n = n

    def sing(self, display=True):
        """Returns and displays the song's lyrics

        Keyword arguments:
        display -- print out the result to the console (default: true)
        """
        full_lyrics = ""

        for bottle_count in range(self.n, 0, -1):
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
        verse = f"{bottle_count} bottles of beer on the wall. {bottle_count} bottles of beer. Take one down, pass it around, {bottle_count - 1} bottles of beer on the wall\n"

        if display:
            print(verse)

        return verse


if __name__ == "__main__":

    bottle = BottleSong()
    bottle.sing()
    # bottle.sing_one(4)
