import sys

person_list = []


class Family_tree():

    def __init__(self):
        self.family_tree = {"sibling": [], "parent": [], "half-sibling": [], "cousin": [], "children": [], 'spouse': [],
                            "ancestor": []}


class Person:

    def __init__(self, name):
        self.name = name
        self.family_tree = Family_tree().family_tree

        # person_list.append(self)

    def add_parents(self, parent_one, parent_two):
        self.family_tree['parent'].append(parent_one)
        if parent_one not in parent_two.family_tree['spouse']:
            parent_two.family_tree['spouse'].append(parent_one)
        self.family_tree['parent'].append(parent_two)
        if parent_two not in parent_one.family_tree['spouse']:
            parent_one.family_tree['spouse'].append(parent_two)

        parent_one.add_children(self)
        parent_two.add_children(self)

        self.add_siblings(parent_one, parent_two)

        if parent_one not in self.family_tree['ancestor']:
            self.family_tree['ancestor'].append(parent_one)
        for ancestor in parent_one.family_tree['ancestor']:
            if ancestor not in self.family_tree['ancestor']:
                self.family_tree['ancestor'].append(ancestor)

        if parent_two not in self.family_tree['ancestor']:
            self.family_tree['ancestor'].append(parent_two)
        for ancestor in parent_two.family_tree['ancestor']:
            if ancestor not in self.family_tree['ancestor']:
                self.family_tree['ancestor'].append(ancestor)

        self.add_cousins(parent_one, parent_two)

    def add_children(self, child):
        self.family_tree['children'].append(child)

    def add_spouse(self, spouse):
        if spouse not in self.family_tree['spouse']:
            self.family_tree['spouse'].append(spouse)
        if self not in spouse.family_tree['spouse']:
            spouse.family_tree['spouse'].append(self)

    def add_siblings(self, parent_one, parent_two):
        for child in parent_one.family_tree['children']:
            if child not in self.family_tree['sibling'] and self.name is not child.name:
                if child in parent_two.family_tree['children']:
                    self.family_tree['sibling'].append(child)
                    child.add_siblings(parent_one, parent_two)

            # if self not in child.family_tree['cousin']:
            #     child.family_tree['cousin'].append(self)
            # if child not in self.family_tree['cousin']:
            #     self.family_tree['cousin'].append(child)

        for child in parent_two.family_tree['children']:
            if child not in self.family_tree['sibling'] and self.name is not child.name:
                if child in parent_one.family_tree['children']:
                    self.family_tree['sibling'].append(child)
                    child.add_siblings(parent_one, parent_two)

            # if self not in child.family_tree['cousin']:
            #     child.family_tree['cousin'].append(self)
            # if child not in self.family_tree['cousin']:
            #     self.family_tree['cousin'].append(child)

    def add_cousins(self, parent_one, parent_two):
        for p in person_list:
            for ancestor in self.family_tree['ancestor']:
                if p not in self.family_tree['cousin'] and p.name != self.name and p not in self.family_tree[
                    'sibling'] and ancestor not in self.family_tree['ancestor']:
                    self.family_tree['cousin'].append(p)
                    if self not in p.family_tree['cousin']:
                        p.family_tree['cousin'].append(self)

        for cousin in parent_one.family_tree['cousin']:
            if cousin not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(cousin)
            if self not in cousin.family_tree['cousin']:
                cousin.family_tree['cousin'].append(self)

        for cousin in parent_two.family_tree['cousin']:
            if cousin not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(cousin)
            if self not in cousin.family_tree['cousin']:
                cousin.family_tree['cousin'].append(self)
        for p_s in parent_one.family_tree['sibling']:
            for toBeCousin in p_s.family_tree['children']:
                if toBeCousin not in self.family_tree['cousin']:
                    self.family_tree['cousin'].append(toBeCousin)
                    if self not in toBeCousin.family_tree['cousin']:
                        toBeCousin.family_tree['cousin'].append(self)

        # for sibling in parent_one.family_tree['sibling']: TODO parent siblingleri kuzen olamaz
        #     if sibling not in self.family_tree['cousin']:
        #         self.family_tree['cousin'].append(sibling)
        #     if self not in sibling.family_tree['cousin']:
        #         sibling.family_tree['cousin'].append(self)

        # for sibling in parent_two.family_tree['sibling']:
        #     if sibling not in self.family_tree['cousin']:
        #         self.family_tree['cousin'].append(sibling)
        #     if self not in sibling.family_tree['cousin']:
        #         sibling.family_tree['cousin'].append(self)


class Operations():

    def list_relation(self, person_name, relation):
        sorted_relations = []
        for person in person_list:
            if person_name == person.name:
                for family_member in person.family_tree[relation]:
                    # print(person.family_tree[relation])
                    sorted_relations.append(family_member.name)
        for member in sorted(sorted_relations):
            if member != person_name:
                print(member)

    def is_relation(self, person_name_one, person_name_two, relation):
        for person in persoadd_siblingswn_list:
            if person_name_one == person.name:
                for person_2 in person_list:
                    if person_name_two == person_2.name:
                        if person_2 in person.family_tree[relation]:
                            print("Yes")
                            return
                        else:
                            print("No")
                            return
        print("No")

    def mom_list(self, person_one, mom: Person):
        if person_one in mom.family_tree['sibling']:
            if person_one.gender == 'M':
                print('Dayi')
            else:
                print('Teyze')
        for p in mom.family_tree['sibling']:
            if len(p.family_tree['spouse']) > 0:
                if person_one.name == p.family_tree['spouse'][0]:
                    if person_one == "F":
                        print("Yenge")
                    else:
                        print('Eniste')
                return

    def search_in_law(self, spouse, person, person_two):
        for p in spouse.family_tree['sibling']:
            if p.name == person.name:
                if p.gender == 'F':
                    if person_two.gender == 'F':
                        print('Elti')
                        return True
                    print('Baldiz')
                else:
                    print('Kayinco')
                return True
            if len(p.family_tree['spouse']) > 0:
                if p.family_tree['spouse'][0].name == person.name:
                    if p.gender == 'F':
                        print('Bacanak')
                    else:
                        print('Elti')
                    return True
        if person in spouse.family_tree['parent']:
            if person.gender == 'F':
                print('Kayinvalide')
            else:
                print('Kayinpeder')
            return True
        return False

    def search_in_law_down(self, me, person):
        for p in me.family_tree['children']:
            if len(p.family_tree['spouse']) > 0:
                if p.family_tree['spouse'][0].name == person.name:
                    if person.gender == 'F':
                        print('Gelin')
                    else:
                        print('Damat')
                    return True
        return False

    def closest_relation(self, person_two, person_one):
        if person_two in person_one.family_tree["spouse"]:
            print("spouse")
            return
        if len(person_one.family_tree['spouse']) > 0:

            for p in person_one.family_tree['spouse'][0].family_tree['sibling']:
                if person_two.name == p.name:
                    if p.gender == 'M':
                        print('Kayinbirader')
                        return
                    # else:
                    #     print('Elti')
                    #     return

        for par in person_one.family_tree['parent']:
            if person_two in person_one.family_tree["parent"]:
                if person_two.gender == 'F':
                    print('Anne')
                else:
                    print('Baba')
                return
            if person_two in par.family_tree['sibling']:
                if par.gender == "F":
                    self.mom_list(person_two, par)
                if par.gender == 'M':
                    if person_two.gender == "F":
                        print('Hala')
                    else:
                        print('Amca')
                    return
        if person_two in person_one.family_tree["sibling"]:
            if person_two.gender == 'F':
                if person_two.birthDate < person_one.birthDate:
                    print('Abla')
                else:
                    print('Baci')
            else:
                if person_two.birthDate < person_one.birthDate:
                    print('Abi')
                else:
                    print('Erkek Kardes')
            return
        if person_two in person_one.family_tree["ancestor"]:
            print("ancestor")
            return
        if person_two in person_one.family_tree["cousin"]:
            print("cousin")
            return
        if person_two in person_one.family_tree['children']:
            if person_two.gender == 'F':
                print('Kiz')
            else:
                print('Ogul')
        if len(person_two.family_tree['spouse']) > 0:
            if self.search_in_law(person_two.family_tree['spouse'][0], person_one, person_two):
                return
        if self.search_in_law_down(person_two, person_one):
            return
        else:
            for p in person_one.family_tree['sibling']:
                if person_two in p.family_tree['children']:
                    print('Yegen')
        return
        # else:
        #     print("Unrelated")
        #     return


def retrieve_person(person_name, gender=None, birthDate=None, death=None):
    for person in person_list:
        if person.name == person_name:
            return person

    x = Person(person_name)
    x.gender = gender
    x.birthDate = birthDate
    x.death = death
    person_list.append(x)
    return x


def fileRead():
    op = Operations()
    x = 'input.txt'
    with open(x, 'r') as f:
        input_list = f.readlines()

    text = input_list
    for line in text:
        line.rsplit()
        commands = line.split()

        if commands[0] == "E":
            if True:
                person_one = retrieve_person(commands[1], commands[2], commands[3], commands[4])
                person_two = retrieve_person(commands[5], commands[6], commands[7], commands[8])
                person_three = retrieve_person(commands[9], commands[10], commands[11], commands[12])
                person_three.add_parents(person_one, person_two)

        elif commands[0] == "W":
            person_one = retrieve_person(commands[2])
            relation = commands[1]
            print("\n" + line)
            op.list_relation(person_one.name, relation)

        elif commands[0] == "R":
            person_one = retrieve_person(commands[1])
            person_two = retrieve_person(commands[2])
            print("\n" + line)
            op.closest_relation(person_one, person_two)

        elif commands[0] == "X":
            person_one = retrieve_person(commands[1])
            relation = commands[2]
            person_two = retrieve_person(commands[3])
            print("\n" + line)
            op.is_relation(person_one.name, person_two.name, relation)


def main():
    fileRead()


main()
