class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash(self.id)


if __name__ == '__main__':0
    s1 = Student(123123, "tamuz")
    s2 = Student(123123, "tamuz")
    s3 = s2
    d = dict()
    d[s1] = True

    print(s2 in d)
    d[s2] = True
    # a = 5
    # print(s1 is s2)
    # print(s3 is s2)
    # print(s1 == s2)
    # print(s3 == s2)

    # conclusion
    # eq - used when searching for a class in the dataset,
    # for example: if eq checks only if the id's are the same it will return true when searching
    # for s1 because s2 is inside and has the same id
    # but if eq checks id and name it will return false when checked if s1 is in inside
    # because s2 has different name then s1
