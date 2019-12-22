import sys
import random
import pdb

try:
    _first = sys.argv[1]
    _last = sys.argv[2]
except:
    try:
        _first = int(input("What is the first number of the range: "))
        _last= int(input("What is the first number of the range: "))
    except:
        raise("Error application is exiting...")
        


class RandomGame:

    def __init__(self,first,last):
         try:
            pdb.set_trace()
            self.first = int(first)
            self.last = int(last)
            self.localrange = range(self.first,self.last)
         except:
            raise ValueError('Use only numbers please for your range')

    def _gen_random_number(self,local_range):
        return random.choice(local_range)

    def RandomGame(self):
        _random_num = self._gen_random_number(self.localrange)
        print(_random_num)
        while True:
            try:
                number = int(input(f"Please guess the number: between {self.first} and {self.last} "))
                if(number == _random_num):
                    print('Well done')
                    break
                else:
                    if(number != 0):
                        print('Try again')
            except:
                print('Please use a real integer only')
                number = -1
                continue
            finally:
                
                if number == 0:
                    print('good-bye')
                    break
                
            

if(__name__ == "__main__"):
    game = RandomGame(_first,_last)
    game.RandomGame()
    