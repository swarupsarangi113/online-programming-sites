class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber,scores = None):
        return super(Student, self).__init__(firstName, lastName, idNumber)
        if scores is None :
            self.scores = []
        else :
            self.scores = scores
    
    def calculate(self) :
        avg_score = sum(scores)//len(scores)

        if avg_score >= 90 and avg_score <= 100 :
            return 'O'
        elif avg_score >= 80 and avg_score < 90 :
            return 'E'
        elif avg_score >= 70 and avg_score < 80 :
            return 'A'
        elif avg_score >= 55 and avg_score < 70 :
            return 'P'
        elif avg_score >= 40 and avg_score < 50 :
            return 'D'
        else :
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
