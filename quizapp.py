class quiz():

    def __init__(self,q1,q2,q3):

        self.q1=q1

        self.q2=q2

        self.q3=q3

        self.questions=["python","c#","java","Javascript","css"]

        self.answers=["python","Javascript","css"]

        self.score=0
    
    def askquestion(self):

        print(self.q1+"\n")

        for i in range(5):
            
            print("-"+self.questions[i]+"\n")
        
        answer1 = input("Cevap : ")

        if answer1 == self.answers[0]:

            self.score+=10

        print(self.q2+"\n")

        for i in range(5):

            print("-"+self.questions[i]+"\n")
        
        answer2 = input("Cevap : ")

        if answer2 == self.answers[1]:

            self.score+=10

        print(self.q3+"\n")

        for i in range(5):

            print("-"+self.questions[i]+"\n")
        
        answer3 = input("Cevap : ")

        if answer3 == self.answers[2]:

            self.score+=10

        print("Sınav bitti.")

        print("Sınav skorunuz : "+str(self.score))

q1=quiz("En güzel programlama dili?","En kolay öğrenilebilecek programlama dili?","En çok kazandıran programlama dili?")

q1.askquestion()