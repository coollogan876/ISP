from TrueRandom.cameraHandler import cameraHandler
from TrueRandom.TrueRandom import TrueRandom
from enum import Enum

random = TrueRandom(cameraHandler(True))
#print(random.random(2, minValue=0, maxValue=(1 << 31) - 1))

letters = Enum('letters', 
               [
                   ('a', 1),
                   ('b', 2),
                   ('c', 3),
                   ('d', 4),
                   ('e', 5),
                   ('f', 6),
                   ('g', 7),
                   ('h', 8),
                   ('i', 9),
                   ('j', 10),
                   ('k', 11),
                   ('l', 12),
                   ('n', 13),
                   ('m', 14),
                   ('o', 15),
                   ('p', 16),
                   ('q', 17),
                   ('r', 18),
                   ('s', 19),
                   ('t', 20),
                   ('u', 21),
                   ('v', 22),
                   ('w', 23),
                   ('x', 24),
                   ('y', 25),
                   ('z', 26),
                   ('A', 27),
                   ('B', 28),
                   ('C', 29),
                   ('D', 30),
                   ('E', 31),
                   ('F', 32),
                   ('G', 33),
                   ('H', 34),
                   ('I', 35),
                   ('J', 36),
                   ('K', 37),
                   ('L', 38),
                   ('N', 39),
                   ('M', 40),
                   ('O', 41),
                   ('P', 42),
                   ('Q', 43),
                   ('R', 44),
                   ('S', 45),
                   ('T', 46),
                   ('U', 47),
                   ('V', 48),
                   ('W', 49),
                   ('X', 50),
                   ('Y', 51),
                   ('Z', 52),
                   ('1', 53),
                   ('2', 54),
                   ('3', 55),
                   ('4', 56),
                   ('5', 57),
                   ('6', 58),
                   ('7', 59),
                   ('8', 60),
                   ('9', 61),
                   ('0', 62),
                   ('!', 63),
                   ('@', 64),
                   ('#', 65),
                   ('$', 66),
                   ('%', 67),
                   ('^', 68),
                   ('&', 69),
                   ('*', 70),
                   ('(', 71),
                   (')', 72)])

numbers = [0 for x in range(20)]

password = ''

for number in numbers:
    number = random.random(2, minValue=1, maxValue=72)
    letter = letters(number).name
    password += letter
    print(number)
    print('\n')

print(f'Password: {password}')