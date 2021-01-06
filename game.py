import random
from drawings import hangman

class Game():
    def __init__(self):
        self.secret_word = random.choice(list(open('words.txt')))
        self.guess_word = []
        self.letter_used = []
        self.word = ' '
    nr_incercari = 8
    Hangman_contor  = 0

    def ghiceste_cuvant(self,cuvant):
        print("\n")
        if cuvant == self.secret_word.split("\n")[0]:
            return True

    def incorrect_letter(self):
        Game.Hangman_contor += 1
        Game.nr_incercari -= 1

        if len(self.letter_used) > 0:
            self.Litere_Folosite()

        if Game.nr_incercari > 0:
            print("Litera nu se afla in cuvant! ")
            self.word = ''.join(self.guess_word)
            print(self.word)
            print("Mai ai: ", Game.nr_incercari, "incercari")
            print(hangman(Game.Hangman_contor))
        else:
            print("Ai pierdut jocul! ")
            print("\n")
            self.play_again()
            input()

    def correct_letter(self,litera):
        if len(self.letter_used) > 0:
            self.Litere_Folosite()
        for i in range(len(self.secret_word.split("\n")[0])  ):
            if self.guess_word[i] == "_ ":
                if self.secret_word[i] == litera:
                    self.guess_word[i] = litera
                    self.word = ''.join(self.guess_word)

        print("Mai ai: ", Game.nr_incercari, "incercari")
        print(hangman(Game.Hangman_contor))
        print(self.word)
        print("\n")

    def Litere_Folosite(self):
        print("Literele folosite pana acum sunt: ", ' , '.join(set(self.letter_used)))

    def joaca(self):

        if len(self.guess_word) == 0:
            for i in range(len(self.secret_word.split("\n")[0]) ):
                self.guess_word.append("_ ")
        print("Sa inceapa jocul: ")
        print("cuvantul este ",''.join(self.guess_word))

        while "_ " in self.guess_word and Game.nr_incercari > 0:
            print("\n")
            litera = input("Introduceti o litera sau Apasati enter pentru introducerea cuvantului! ")
            if litera in "abcdefghijklmnopqrsruyvtxzywz":
                self.letter_used.append(litera)

                print("\n")
                if self.letter_used.count(litera) > 1:
                    print("Litera este deja ghicita,alegeti alta litera")


                if litera in self.secret_word:
                    self.correct_letter(litera)

                if litera not in self.secret_word:
                    self.incorrect_letter()


            if litera == "":
                cuvant = input("Introdu cuvantul: ")

                if self.ghiceste_cuvant(cuvant):
                    print("Bravo, acesta era cuvantul:  ")






                    print("\n")
                    input()
                    break

                else:
                    self.incorrect_letter()
                    print("Mai incearca, esti f aproape!")
                    print("\n")

            if litera not in  "abcdefghijklmnopqrsrutvxzywz":
                print("Ce ati introdus nu este o litera, incercati altceva")

            if "_ " not in self.guess_word:
                print("Bravo! ")

g = Game()
g.joaca()

