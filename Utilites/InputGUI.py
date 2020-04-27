'''
@ Author - Karan Pandya
@ Creation date - 08/20/2018
@ Description - Create Input User Interface...
'''
import easygui
from tkinter import *
from Utilites import AppConstants
class InputGUI:

    def window_creation(self):
        self.Master = Tk()
        self.username_flag = 0
        self.team_flag = 0
        self.task_type_flag = 0

        self.team_list = AppConstants.TEAM_LIST
        self.selected_team = StringVar()
        self.task_type_list = AppConstants.TRACK_LIST
        self.selected_task_type = StringVar()


        self.Master.geometry('500x500')
        self.Master.title("Input Form")

        self.label_0 = Label(self.Master, text="Input form", width=20, font=("bold", 20))
        self.label_0.place(x=90, y=53)

        self.label_1 = Label(self.Master, text="UserName", width=20, font=("bold", 10))
        self.label_1.place(x=80, y=130)

        self.Entry = Entry(self.Master)
        self.Entry.place(x=240, y=130)


        self.droplist = OptionMenu(self.Master, self.selected_team, *self.team_list)
        self.droplist.config(width=15, font=("bold", 10))
        self.selected_team.set('Select Team')
        self.droplist.place(x=180, y=180)


        self.droplist = OptionMenu(self.Master, self.selected_task_type, *self.task_type_list)
        self.droplist.config(width=15, font=("bold", 10))
        self.selected_task_type.set('Select Task Type')
        self.droplist.place(x=180, y=230)

        self.my_button = Button(self.Master, text='Submit', width=20, bg='brown', fg='white', command=self.Return).place(x=180,
                                                                                                                y=280)
        self.Master.mainloop()
        self.Master.destroy()


    def Return(self):
        self.username = self.Entry.get()

        if len(self.username) == 0:
            self.username_flag = 1
        self.team = self.selected_team.get()
        if self.team == "Select Team":
            self.team_flag = 1
        self.task_type = self.selected_task_type.get()
        if self.task_type == "Select Task Type":
            self.task_type_flag = 1
        self.Master.quit()

    def validation(self, username_flag, team_flag, task_type_flag):
        if username_flag != 0:
            easygui.msgbox("Enter Valid Username and Rerun the script")
            exit(1)
        if team_flag != 0:
            easygui.msgbox("Select Valid Team and Rerun the script")
            exit(1)
        if task_type_flag != 0:
            easygui.msgbox("Select Valid Task Type and Rerun the script")
            exit(1)



