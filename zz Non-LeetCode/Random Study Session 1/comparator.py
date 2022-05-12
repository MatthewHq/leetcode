from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "{} {}".format(name, score)

    def comparator(a, b):
        print(a,"a")
        print(b,"b")
        if a.score > b.score:
            return 1
        elif a.score < b.score:
            return -1
        elif a.score==b.score:
            if a.name>b.name:
                return 1
            elif a.name<b.name:
                return -1
            else:
                return 0


n = int(5)
data = []
s = "amy 100\ndavid 100\nheraldo 50\naakansha 75\naleksa 150"
s = s.split('\n')
for i in range(n):
    name, score = s[i].split(' ')
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
print("======")
for i in data:
    print(i.name, i.score)
