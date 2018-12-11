class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued.",
                   "So I will stop right there."])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#***PRACTICE***
print('_' * 20)
class Lyric:
    def __init__(self, first_lyric, second_lyric):
        self.first_lyric = first_lyric
        self.second_lyric = second_lyric

    def the_first_song(self):
        print("This is my first song: " + self.first_lyric)
        print ("This is the second song: " + self.second_lyric)

p1 = Lyric("Happy Birthday to you", "We wish you a Marry Xmas")
p1.the_first_song()

print("Let's get only Xmas songs")
p1.first_lyric = "Santa tell me"
p1.the_first_song()
