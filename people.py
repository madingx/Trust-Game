
class People:
    def __init__(self,name='someone'):
        self.score = 20    # 成绩
        self.last_dicision = True
        self.opponent_last = True
        self.name = name

    def decide_trust(self,cost):
        self.last_dicision = True
        self.score -= cost
        return True
    def decide_betray(self,cost):
        self.last_dicision = False
        return False

    def decide(self,cost):
        self.last_dicision = True
        return True


    def get_gain(self,gain):
        self.score += gain
        return self.score
    def is_alive(self):
        return  self.score >= 0

    def knew_opponent(self,opponent):
        self.opponent_last = opponent.last_dicision


class LittlePink(People):
    def decide(self,cost):
        return self.decide_trust(cost)

class BadGay(People):
    def decide(self,cost):
        return self.decide_betray(cost)


class Repeater(People):
    def decide(self,cost):
        return self.decide_trust(cost) if self.opponent_last else self.decide_betray(cost)















#**********************************************#


class Battle:
    def __init__(self,peopleA,peopleB):
        self.peopleA = peopleA
        self.peopleB = peopleB
        self.cost = 1
        self.once_gain = {
            'both-win':3,
            'both-lose':0,
            'other':1
        }


    def cal_result(self):
        self.peopleA.knew_opponent(self.peopleB)
        self.peopleB.knew_opponent(self.peopleA)
        print('before:  score of %s is %d,  score of %s is %d'%(self.peopleA.name,self.peopleA.score,self.peopleB.name,self.peopleB.score))
        a = self.peopleA.decide(self.cost)
        b = self.peopleB.decide(self.cost)

        if a and b:
            self.peopleA.get_gain(self.once_gain['both-win'])
            self.peopleB.get_gain(self.once_gain['both-win'])
        if not a and not b:
            self.peopleA.get_gain(self.once_gain['both-lose'])
            self.peopleB.get_gain(self.once_gain['both-lose'])
        elif a:
            self.peopleB.get_gain(self.once_gain['other'])
        elif a:
            self.peopleA.get_gain(self.once_gain['other'])


        print('after:   score of %s is %d,  score of %s is %d'%(self.peopleA.name,self.peopleA.score,self.peopleB.name,self.peopleB.score))




class GroupBattle:
    def __init__(self,people_list):
        self.people_list = people_list
        self.cost = 1
        self.once_gain = {
            'both-win':3,
            'both-lose':0,
            'other':1
        }
