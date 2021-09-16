#
#        작성자 : 박지용
#        프로그램 : 계산기
#        작성 프로그램 : Atom
#        사용 프로그램 : python 3.7.0 (Anaconda3)
#        작성 시작 날짜 : 18.11.30
#
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("지용 계산기")#제목
        self.setFixedSize(260,300)
        #self.setGeometry(1600,500,300,400)#300,300 위치에 300,400크기로 생성

        #Text
        self.text_output=QLabel()
        self.sub_output=QLabel()
        self.text_contents=""
        #self.full_contents_list=[""]
        self.full_contents_join=""
        self.cal_contents_list=[""]
        self.operater=[43,45,42,47,37,"+","-","*","/","%"," + "," - "," * "," / "," % "]
        #self.bracket=[[40,123,91,"(","{","["],[41,125,93,")","}","]"]]#모둠괄호
        self.bracket=[[40],[41]]
        self.bracket_count_l=0
        self.bracket_count_r=1

        self.cal_stack=[""]
        self.cal_exp=[]

        self.text_output.setText('<p align="right"><font size=6><b>'+"0"+'</b></font></p>')
        self.myframe=QGroupBox()

        #Buttons
        self.btn_bs=QPushButton("←")
        self.btn_C=QPushButton("C")
        self.btn_7=QPushButton("7")
        self.btn_8=QPushButton("8")
        self.btn_9=QPushButton("9")
        self.btn_div=QPushButton("/")
        self.btn_remain=QPushButton("%")
        self.btn_4=QPushButton("4")
        self.btn_5=QPushButton("5")
        self.btn_6=QPushButton("6")
        self.btn_1=QPushButton("1")
        self.btn_2=QPushButton("2")
        self.btn_3=QPushButton("3")
        self.btn_0=QPushButton("0")
        self.btn_dot=QPushButton(".")
        self.btn_mul=QPushButton("*")
        self.btn_sub=QPushButton("-")
        self.btn_pl=QPushButton("+")
        self.btn_eq=QPushButton("=")


        #main layout
        layout = QGridLayout()
        layout.addWidget(self.myframe,0,0,2,4)
        layout.addWidget(self.sub_output, 0, 0, 1, 4)
        layout.addWidget(self.text_output, 1, 0, 1, 4)

        layout.addWidget(self.btn_bs,3,0)
        layout.addWidget(self.btn_C,3,1)
        layout.addWidget(self.btn_7,4,0)
        layout.addWidget(self.btn_8,4,1)
        layout.addWidget(self.btn_9,4,2)
        layout.addWidget(self.btn_4,5,0)
        layout.addWidget(self.btn_5,5,1)
        layout.addWidget(self.btn_6,5,2)
        layout.addWidget(self.btn_1,6,0)
        layout.addWidget(self.btn_2,6,1)
        layout.addWidget(self.btn_3,6,2)
        layout.addWidget(self.btn_dot,7,2)
        layout.addWidget(self.btn_remain,3,3)
        layout.addWidget(self.btn_div,4,3)
        layout.addWidget(self.btn_mul,5,3)
        layout.addWidget(self.btn_sub,6,3)
        layout.addWidget(self.btn_pl,7,3)
        layout.addWidget(self.btn_eq,3,2)
        layout.addWidget(self.btn_0,7,0,1,2)

        self.setLayout(layout)


        #Buttons clicked
        self.btn_1.clicked.connect(self.btn_1_clicked)
        self.btn_2.clicked.connect(self.btn_2_clicked)
        self.btn_3.clicked.connect(self.btn_3_clicked)
        self.btn_4.clicked.connect(self.btn_4_clicked)
        self.btn_5.clicked.connect(self.btn_5_clicked)
        self.btn_6.clicked.connect(self.btn_6_clicked)
        self.btn_7.clicked.connect(self.btn_7_clicked)
        self.btn_8.clicked.connect(self.btn_8_clicked)
        self.btn_9.clicked.connect(self.btn_9_clicked)
        self.btn_0.clicked.connect(self.btn_0_clicked)
        self.btn_bs.clicked.connect(self.btn_bs_clicked)
        self.btn_C.clicked.connect(self.btn_C_clicked)
        self.btn_eq.clicked.connect(self.btn_eq_clicked)
        self.btn_remain.clicked.connect(self.btn_remain_clicked)
        self.btn_div.clicked.connect(self.btn_div_clicked)
        self.btn_mul.clicked.connect(self.btn_mul_clicked)
        self.btn_sub.clicked.connect(self.btn_sub_clicked)
        self.btn_pl.clicked.connect(self.btn_pl_clicked)
        self.btn_dot.clicked.connect(self.btn_dot_clicked)


    def btn_1_clicked(self):
        self.update_text_output("1")
    def btn_2_clicked(self):
        self.update_text_output("2")
    def btn_3_clicked(self):
        self.update_text_output("3")
    def btn_4_clicked(self):
        self.update_text_output("4")
    def btn_5_clicked(self):
        self.update_text_output("5")
    def btn_6_clicked(self):
        self.update_text_output("6")
    def btn_7_clicked(self):
        self.update_text_output("7")
    def btn_8_clicked(self):
        self.update_text_output("8")
    def btn_9_clicked(self):
        self.update_text_output("9")
    def btn_0_clicked(self):
        self.update_text_output("0")
    def btn_bs_clicked(self):
        self.bs_pressed()
    def btn_C_clicked(self):
        self.esc_pressed()
    def btn_eq_clicked(self):
        self.eq_pressed()
    def btn_remain_clicked(self):
        self.update_sub_output(37)
    def btn_div_clicked(self):
        self.update_sub_output(47)
    def btn_mul_clicked(self):
        self.update_sub_output(42)
    def btn_sub_clicked(self):
        self.update_sub_output(45)
    def btn_pl_clicked(self):
        self.update_sub_output(43)
    def btn_dot_clicked(self):
        self.update_text_output(".")


    def is_number(self,str):
        try:
            float(str)
            return True
        except ValueError:
            return False



    def update_text_output(self,new_contents):#밑쪽에 현재 입력 값 출력

        if new_contents=="reset":
            self.text_contents=""
            return

        if self.text_contents=="0":
            self.text_contents=""

        if new_contents==".":
            if "." in self.text_contents:#점 연속입력 방지
                return
            if self.text_contents=="":
                self.text_contents="0"

        if len(self.text_contents)<16:
            new_contents=str(new_contents)
            self.text_contents=self.text_contents+new_contents
            self.text_output.setText('<p align="right"><font size=6><b>'+self.text_contents+'</b></font></p>')

        elif len(self.text_contents)>=16:
            print("\a")

    def update_sub_output(self,new_contents):#위쪽에 계산식 출력

        if new_contents=="esc":#ESC인자 들어와서 초기화 할때
            new_contents=""
            self.text_contents=""
            self.cal_contents_list=[""]

        elif new_contents=="cal":#cal인자 들어와서 엔터,이퀄등의 이유로 계산할 때
            if self.text_contents!="":
                self.cal_contents_list.append(self.text_contents)#피연산자 받아옴

        if new_contents in self.operater:#입력 값이 연산자일 때

            if self.text_contents=="" and len(self.cal_contents_list)<=1:#이건 맨 처음에 연산자 쓰면 앞에 0 써지는거
                self.text_contents="0"

            if self.text_contents!="":
                self.cal_contents_list.append(self.text_contents)#입력돼있던 피연산자 가져오는 것

            if self.cal_contents_list[-1] in self.operater:#연산자 뒤에 연산자 또 올때 앞 연산자 삭제
                del self.cal_contents_list[-1]

            if self.text_contents=="" and self.cal_contents_list[-1]!=")" and self.cal_contents_list[-1]!="0":#괄호 바로뒤에 연산자오는거 생각
                self.text_contents="0"


            self.cal_contents_list.append(chr(new_contents))

        if new_contents in self.bracket[0]:#왼쪽 괄호일 때
            if self.text_contents!="":
                self.cal_contents_list.append(self.text_contents)#피연산자 받아옴
            self.cal_contents_list.append(chr(new_contents))
            self.bracket_count_l+=1

        elif new_contents in self.bracket[1]:#오른쪽 괄호일 때
            if self.cal_contents_list[-1]=="(":return
            if self.text_contents!="":
                self.cal_contents_list.append(self.text_contents)#피연산자 받아옴
            if self.bracket_count_r<=self.bracket_count_l:
                self.cal_contents_list.append(chr(new_contents))
                self.bracket_count_r+=1

        max=len(self.cal_contents_list)-1#괄호에 붙어있는 숫자 곱하기처리하려고
        for i in range(1,max):
            if self.cal_contents_list[i]=="(" and (self.is_number(self.cal_contents_list[i-1])):
                self.cal_contents_list.insert(i,"*")
            elif self.cal_contents_list[i]==")" and (self.is_number(self.cal_contents_list[i+1])):
                self.cal_contents_list.insert(i+1,"*")

        self.full_contents_join="".join(self.cal_contents_list)#이거는 단순히 출력용 실제론 cal에있음
        #print("self.cal_contents_list:",self.cal_contents_list)
        #print("중위변환식:",self.full_contents_join)
        #print("리스트:",self.cal_contents_list)

        if len(self.full_contents_join)>31:
            over_contents="＜＜"+self.full_contents_join[-30:-1]
            self.sub_output.setText('<p align="right"><font size=3><b>'+over_contents+'</b></font></p>')
        else:
            self.sub_output.setText('<p align="right"><font size=3><b>'+self.full_contents_join+'</b></font></p>')

        self.update_text_output("reset")


    def keyPressEvent(self,event):
        key_input=event.key()
        #print(key_input)#뭐눌렀는지 보여주는곳

        #ESC input
        if key_input==16777216:
            self.esc_pressed()

        #BackSpace input
        elif key_input==16777219:
            self.bs_pressed()

        #numbers input :피연산자
        elif key_input>=48 and key_input<=57:
            if len(self.text_contents)<16:
                key_input-=48
                self.update_text_output(key_input)

            elif len(self.text_contents)>=16:
                print("\a")#칸 넘어가게 입력하면 비프음나옴

        elif key_input==46:#점
            self.update_text_output(".")

        #operater input :연산자
        elif key_input in self.operater:
            self.update_sub_output(key_input)

        #bracket input : 괄호
        elif key_input in self.bracket[0] or key_input in self.bracket[1]:
            self.update_sub_output(key_input)

        #equal or Enter input
        elif key_input==61 or key_input==16777220 or key_input==16777221:#=
            self.eq_pressed()


    #esc input func
    def esc_pressed(self):
        self.text_contents=""
        self.full_contents_list=[""]
        self.full_contents_join=""
        self.cal_contents_list=[""]
        self.update_text_output("0")
        self.update_sub_output("esc")

    #backspace input func
    def bs_pressed(self):
        if len(self.text_contents)>1:
            temp=self.text_contents[0:-1]
            self.text_contents=""
            self.update_text_output(temp)

        elif len(self.text_contents)==1:
            self.text_contents="0"
            self.update_text_output("0")

    #equal input func =이나 엔터쳐서 이제 계산들어가는부분
    def eq_pressed(self):

        rank={"(":10, ")":10, "+":20, "-":20, "*":30, "/":30, "%":30}

        if len(self.cal_contents_list)<3:
            if self.cal_contents_list[-1] in self.operater:
                self.cal_contents_list.append(self.cal_contents_list[-2])
            else:
                self.cal_contents_list=[""]
                self.text_contents=""
                return
        else:
            self.update_sub_output("cal")

        if self.cal_contents_list[-1] in self.operater:
            self.cal_contents_list.pop()

        print("중위변환식:","".join(self.cal_contents_list))

        max=len(self.cal_contents_list)
        #print("리스트:",self.cal_contents_list)
        for i in range(1,max):#리스트 길이전체 반복

            if self.cal_contents_list[1]=="-":
                self.cal_contents_list[i]="-"+self.cal_contents_list[i+1]
                #del self.cal_contents_list[i+1]
                self.cal_contents_list[i+1]=""

            # "-"앞에 숫자가 아닐때
            elif self.cal_contents_list[i]=="-":
                #if not(self.cal_contents_list[i-1].isdigit()):
                if not(self.is_number(self.cal_contents_list[i-1])):
                    self.cal_contents_list[i]="-"+self.cal_contents_list[i+1]
                    self.cal_contents_list[i+1]=""
        temp=""
        minus = False
        
        for i in range(max):
            target=self.cal_contents_list[i]
            #print("스택:",self.cal_stack)
            #print("식:",self.cal_exp)

            if target=="":
                continue

            if self.is_number(target):#피연산자는 스택에 넣지않고 식에넣음
                if minus:
                    if target[0] == "-":
                        target = target[1:]
                    else:
                        target = "-"+target
                    minus = False
                
                self.cal_exp.append(target)

            elif target[0]=="-" and len(target)>1:#이건 피연산자가 음수일때 식에넣음
                self.cal_exp.append(target)

            elif target=="(":#여는 괄호는 무조건 스택에 넣음
                self.cal_stack.append(target)

            elif target==")":#닫는 괄호는 스택에서 여는괄호가 나올때까지 식에 넣음
                while True:
                    temp=self.cal_stack.pop()
                    if temp=="(":
                        #self.cal_exp.append(temp)
                        break
                    self.cal_exp.append(temp)

            elif target=="+"or target=="-"or target=="*"or target=="/"or target=="%":#타겟이 연산자일때
                print("이거", self.cal_contents_list[i+1])
                if target=="-":
                    target = "+"
                    minus = True

                if self.cal_stack[-1]=="":#스택이 비었을때
                    self.cal_stack.append(target)

                else:#스택이 안비었을때
                    temp=self.cal_stack[-1]
                    if rank.get(target)<=rank.get(temp):#스택에있는 연산자우선순위가 같거나 더 클때
                        self.cal_exp.append(self.cal_stack.pop())
                        self.cal_stack.append(target)
                    else:
                        self.cal_stack.append(target)

        while self.cal_stack:#마지막으로 스택에있는거 식으로 다뺌
            temp=self.cal_stack.pop()
            if temp=="":
                pass
            elif temp=="(":
                pass
            else:
                self.cal_exp.append(temp)

        self.esc_pressed()
        print("후위변환식:"," ".join(self.cal_exp))
        #여기까지 후위변환식으로 변환완료

        #여기 아래부터 이제 계산부분
        self.cal_stack=[""]
        max=len(self.cal_exp)

        for i in range(max):
            target=self.cal_exp.pop(0)

            if target=="":continue

            #if target.isdigit():#피연산자일때
            if self.is_number(target):
                self.cal_stack.append(target)

            elif target[0]=="-" and len(target)>1:#이건 피연산자가 음수일때 식에넣음
                self.cal_stack.append(target)

            elif target in self.operater:#연산자일때
                temp2=float(self.cal_stack.pop())
                temp1=float(self.cal_stack.pop())

                if target=="+":
                    temp3=float(temp1+temp2)
                if target=="-":
                    temp3=float(temp1-temp2)
                if target=="*":
                    temp3=float(temp1*temp2)
                if target=="/":
                    if temp2==0:
                        self.text_output.setText('<p align="right"><font size=4><b>'+"0으로 나눌 수 없습니다."+'</b></font></p>')
                        return
                    temp3=float(temp1/temp2)
                if target=="%":
                    temp3=float(temp1%temp2)

                self.cal_stack.append(temp3)

        temp4=self.cal_stack.pop()
        if type(temp4)==str:
            temp4=float(temp4)
        if not(temp4-int(temp4)):
            temp4=int(temp4)

        output=str(temp4)
        #if len(output)>16:

        self.text_output.setText('<p align="right"><font size=6><b>'+output+'</b></font></p>')

        self.cal_stack=[""]
        self.cal_exp=[]
        self.text_contents=output

if __name__=="__main__":
    app = QApplication(sys.argv)
    my_window=MainWindow()
    my_window.show()
    app.exec_()
