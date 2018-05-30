import random

def click(obj, cordinates):
    '''
    func that simulates mouse clicks in areas as Bot
    '''
    heihgt = cordinates[1]
    width = cordinates[0]

    obj[width][heihgt].click()


def find_Wey(obj):
    '''func that fount all true place_ability in area
    and return list of tuple cordinates'''
    Ten = list(range(0,10))
    res = []

    for Row in Ten:
        for Col in Ten:
            if obj[Row][Col].place_ability:
                res.append((Row,Col))
            else:
                pass
    return res


def random_build(obj):
    '''func that build ships randomly'''
    the_wei = find_Wey(obj)
    Build = random.choice(the_wei)
    click(obj,Build)

