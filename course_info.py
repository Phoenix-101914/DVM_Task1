admin_pass='1234'
class Course(Section):
    def __init__(self,Subject,MidSem,Compre,Lec=None,Tut=None,Lab=None): #Lec,Tut,Lab are respective classes, MIdSem and Compre are dates in YYYY-MM-DD format
        if Lec==None:
            self.Lec={}
        else: 
            self.Lec=Lec
        if Tut==None:
            self.Tut={}
        else: 
            self.Tut=Tut
        if Lab==None:
            self.Lab={}
        else: 
            self.Lab=Lab
        self.Subject=Subject
        self.MidSem=MidSem
        self.Compre=Compre
    def __str__(self):
        return '{}-\nLec: {}\nTut: {}\nLab: {}\nMid Semester Date: {}\nCompre Date: []'.format(self.Subject,self.Lec,self.Tut,self.Lab,self.MidSem,self.Compre)
    def get_all_sections(self):
        return 'Lec: {}\nTut: {}\nLab: {}'.format(self.Lec,self.Tut,self.Lab)
    def populate_section():
        if admin():
            choice=menu_ps()
            if choice==1:
                pass
            if choice==2:
                pass
            if choice==3:
                pass
        else:
            print("Incorrect password")
class Section():
    def __init__(self,day,time,instructor,Course):
        self.day=day
        self.time=time
        self.instructor=instructor
        self.Subject=Course
class Lec(Section):
    pass
class Tut(Section):
    pass
class Lab(Section):
    pass
class Timetable:
    def __init__(self):
        pass
def populate_course():
    pass
def menu_ps():
    choice=int(input('Enter 1 to populate Lec\nEnter 2 to populate Tut\nEnter 3 to populate Lab'))
    return choice
def admin():
    a=int(input('Enter admin password '))
    if a==admin_pass:
        return 1
    return 0
M1=Course("M1",'2023-12-22','2023-11-11',M1_l,{"Tuesday":"6:00-8:00"},{"Tuesday":"5:00-8:00"})
M1_l=Lec('Tuesday','8:00-9:00','Anirudh',M1)
print(M1)
print(M1.Subject)
print(M1.Lab)
print(M1.Tut)
print(M1.Lec)
print(M1_l.Subject)