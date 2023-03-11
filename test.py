import unittest
from bottles import BottleSong


class TestBottleSong(unittest.TestCase):

    bottles = BottleSong()

    def test_full_song(self):
        result = self.bottles.sing(display=False)

        verses = result.split("\n")
        verses.pop()

        for bottle_count in range(99, 1, -1):
            self.assertEqual(
                self.bottles.sing_one(bottle_count, display=False).replace("\n", ""),
                verses[99 - bottle_count],
            )

    def test_one_verse(self):
        result = self.bottles.sing_one(4, display=False)
        self.assertEqual(
            result,
            "4 bottles of beer on the wall. 4 bottles of beer. Take one down, pass it around, 3 bottles of beer on the wall\n",
        )


if __name__ == "__main__":
    unittest.main()
