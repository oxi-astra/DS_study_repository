import numpy as np
import game_v2 as g2

#number = np.random.randint(1,101)
count = 0

def range_search(number: int = 1, diap: tuple = (1,100), count: int = 0) -> int:
    count += 1
    variable = round((diap[0]+diap[1])/2)
    #print('number = {}, variable = {}, diap = {}, {}, count - {}'.format(\
 #number, variable, *diap, count))
    if variable == diap[0] or variable == diap[1] or variable == number:
        return count
    elif variable > number:
        count += 1
        range_search(number, (diap[0], variable), count )
        return count
    else:
        count += 1
        range_search(number, (variable, diap[1]), count )
        return count


#count = range_search(number,(1,100))

g2.score_game(range_search)

#print(count)

