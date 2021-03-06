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
    the_wey = find_Wey(obj)
    Build = random.choice(the_wey)
    click(obj,Build)

def find_shot(obj):
    '''find all shot posibilities in area(obj)'''
    Ten = list(range(0,10))
    res = []

    for Row in Ten:
        for Col in Ten:
            if not obj[Row][Col].was_shot or not obj[Row][Col].new_shot:
                res.append((Row,Col))
            else:
                pass
    return res

def random_shot(obj):
    print('random shot')
    '''func that shots randomly'''
    the_wey = find_Wey(obj)
    Build = random.choice(the_wey)
    click(obj,Build)