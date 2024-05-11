import random
from PyQt5 import QtCore, QtGui, QtWidgets as qtw
from math import lcm,gcd
from function import Draw, Priority_rm, Priority_dm
import PyQt5.QtGui as qtg
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory, QWidget, QVBoxLayout, QPushButton

def set_dark_theme(app):
    app.setStyle(QStyleFactory.create("Fusion"))
    palette = app.palette()
    palette.setColor(app.palette().Window, QtGui.QColor(53, 53, 53))
    palette.setColor(app.palette().WindowText, QtGui.QColor(255, 255, 255))
    palette.setColor(app.palette().Base, QtGui.QColor(25, 25, 25))
    palette.setColor(app.palette().AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(app.palette().ToolTipBase, QtGui.QColor(255, 255, 255))
    palette.setColor(app.palette().ToolTipText, QtGui.QColor(255, 255, 255))
    palette.setColor(app.palette().Text, QtGui.QColor(255, 255, 255))
    palette.setColor(app.palette().Button, QtGui.QColor(53, 53, 53))
    palette.setColor(app.palette().ButtonText, QtGui.QColor(255, 255, 255))
    palette.setColor(app.palette().BrightText, QtGui.QColor(255, 0, 0))
    palette.setColor(app.palette().Highlight, QtGui.QColor(142, 45, 197))
    palette.setColor(app.palette().HighlightedText, QtGui.QColor(255, 255, 255))
    app.setPalette(palette)

class MainWindow(qtw.QWidget):
    #tasks الصفحة الرئيسية الخاصة بوضع عدد ال  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TP_rm_dm")
        self.setWindowIcon(qtg.QIcon("Reel.ico"))
        self.setFixedSize(1000, 700)

        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)

        my_label1 = qtw.QLabel("Give me the number of tasks you want to be ordered?")
        my_label1.setFont(QtGui.QFont('Red Hat Display', 40))
        main_layout.addWidget(my_label1, alignment=QtCore.Qt.AlignCenter)

        number_entry = qtw.QLineEdit()
        number_entry.setObjectName("tasks_number")
        number_entry.setFixedSize(200, 50)
        number_entry.setText("")
        main_layout.addSpacing(20)
        main_layout.addWidget(number_entry)
        main_layout.addWidget(number_entry, alignment=QtCore.Qt.AlignCenter)
        main_layout.addSpacing(300)
        # Create a frame for the labels
        labels_groupbox = qtw.QGroupBox()
        labels_groupbox.setFixedSize(750, 110)
        labels_groupbox.setObjectName("labels_groupbox")
        labels_groupbox.setStyleSheet("QGroupBox { border: 2px solid black; border-radius: 10px; padding: 10px; }")
        labels_layout = qtw.QVBoxLayout(labels_groupbox)

        my_label2 = qtw.QLabel("note")
        my_label2.setFont(QtGui.QFont('Red Hat Display', 18))
        labels_layout.addWidget(my_label2, alignment=QtCore.Qt.AlignCenter)

        my_label3 = qtw.QLabel("Please select a number of tasks greater than two, and kindly note that if you choose a number exceeding three tasks,\n\t\t you will only be able to view the time ranges and not the diagram.")
        my_label3.setFont(QtGui.QFont('Red Hat Display', 10))
        labels_layout.addWidget(my_label3, alignment=QtCore.Qt.AlignCenter)
        #my_label4 = qtw.QLabel(" the time ranges and not the diagram.")
        #my_label4.setFont(QtGui.QFont('Red Hat Display', 10))
        #labels_layout.addWidget(my_label4, alignment=QtCore.Qt.AlignCenter)

        main_layout.addWidget(labels_groupbox, alignment=QtCore.Qt.AlignCenter)

        button_layout = qtw.QHBoxLayout()
        main_layout.addLayout(button_layout) 

        spacer_item = qtw.QSpacerItem(0, 0, qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        button_layout.addItem(spacer_item)

        next_page = qtw.QPushButton("Next")
        next_page.setFixedSize(200, 50)
        next_page.clicked.connect(self.press_1)
        button_layout.addWidget(next_page, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

        self.show()
    # taskالصفحة ملئ الخانات الخاصة بكل  
    def press_1(self):
        number_entry = self.findChild(qtw.QLineEdit, "tasks_number")  # Find the entry box by its object name
        text = number_entry.text()
        number_entry.setText("")

        if text == "":
            qtw.QMessageBox.critical(self, "Error", "Please fill in the empty field.")
        elif int(text) < 2:
            qtw.QMessageBox.critical(self, "Error", "Please enter a number greater than or equal to 2.")
        else:
            self.new_window1 = qtw.QWidget()
            self.new_window1.setWindowTitle("TP_rm_dm")
            self.new_window1.setWindowIcon(qtg.QIcon("Reel.ico"))
            self.new_window1.setFixedSize(1000, 700)  # Set the fixed size of the new window
            self.new_window1.setLayout(qtw.QVBoxLayout())

            my_label1 = qtw.QLabel("Fill in the data ")
            my_label1.setFont(qtg.QFont('Red Hat display', 40))
            self.new_window1.layout().addWidget(my_label1, alignment=QtCore.Qt.AlignCenter)
             
            spacer_item = qtw.QSpacerItem(0, 40, qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Fixed)
            self.new_window1.layout().addItem(spacer_item)  # Add spacer item for spacing

            self.table_widget = qtw.QTableWidget()
            self.table_widget.setColumnCount(5)
            self.table_widget.setRowCount(int(text))
            self.table_widget.setHorizontalHeaderLabels(["Task", "Arrival time", "Duration", "Period", "Deadline"])

            for i in range(int(text)):
                for j, header in enumerate(["Task", "Arrival time", "Duration", "Period", "Deadline"]):
                    if j == 0:
                        item = qtw.QTableWidgetItem(f"{header} {i+1}")
                        self.table_widget.setItem(i, j, item)
                    else:
                        line_edit = qtw.QLineEdit()
                        self.table_widget.setCellWidget(i, j, line_edit)

            self.new_window1.layout().addWidget(self.table_widget)

            button_layout = qtw.QHBoxLayout()
            self.new_window1.layout().addLayout(button_layout)

            back_button = qtw.QPushButton("Back")
            back_button.setFixedSize(200, 50)
            back_button.clicked.connect(self.return_to_initial_window)
            button_layout.addWidget(back_button, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)

            spacer_item = qtw.QSpacerItem(0, 0, qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
            button_layout.addItem(spacer_item)

            next_button = qtw.QPushButton("Next")
            next_button.setFixedSize(200, 50)
            next_button.clicked.connect(self.press_2)
            button_layout.addWidget(next_button, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

            self.new_window1.setLayout(self.new_window1.layout())  # Set the layout

            self.new_window1.show()
    def return_to_initial_window(self):
        self.new_window1.close()  # Close the current secondary window
    #methodeالصفحة الخاصة باختيار ال
    def press_2(self):
        if not hasattr(self, 'table_widget'):
            qtw.QMessageBox.critical(self, "Error", "Please fill in the table first.")
            return
        
        tasks = []
        for row in range(self.table_widget.rowCount()):
            task = {}
            for col, header in enumerate(["Task", "Arrival time", "Duration", "Period", "Deadline"]):
                cell_widget = self.table_widget.cellWidget(row, col)
                if isinstance(cell_widget, qtw.QLineEdit):
                    text = cell_widget.text()
                    if text:
                        if not text.isnumeric():
                            qtw.QMessageBox.critical(self, "Error", f"Invalid input: {text} is not a number.")
                            return  # Abort further processing
                        task[header] = text
                    else:
                        qtw.QMessageBox.critical(self, "Error", "Please fill in all the fields.")
                        return  # Abort further processing
            tasks.append(task)

        self.new_window2 = qtw.QWidget()
        self.new_window2.setWindowTitle("TP_rm_dm")
        self.new_window2.setWindowIcon(qtg.QIcon("Reel.ico"))
        self.new_window2.setFixedSize(1000, 700)  # Set the fixed size of the new window
        self.new_window2.setLayout(qtw.QVBoxLayout())
        
        label_layout = qtw.QHBoxLayout()
        self.new_window2.layout().addLayout(label_layout)

        my_label2 = qtw.QLabel("Choose the sorting method?")
        my_label2.setFont(qtg.QFont('Red Hat display', 40))
        self.new_window2.layout().addWidget(my_label2) 
        label_layout.addWidget(my_label2, alignment=QtCore.Qt.AlignCenter )
        
        button_layout = qtw.QHBoxLayout()
        self.new_window2.layout().addLayout(button_layout)

        rm_button = qtw.QPushButton("RM")
        rm_button.setFixedSize(200, 50)
        rm_button.clicked.connect(self.press_rm)  
        self.new_window2.layout().addWidget(rm_button)
        button_layout.addWidget(rm_button, alignment=QtCore.Qt.AlignCenter )

        button_layout.addSpacing(20)

        dm_button = qtw.QPushButton("DM")
        dm_button.clicked.connect(self.press_dm) 
        dm_button.setFixedSize(200, 50) 
        self.new_window2.layout().addWidget(dm_button)
        button_layout.addWidget(dm_button, alignment=QtCore.Qt.AlignCenter)

        button_layout1 = qtw.QHBoxLayout()
        self.new_window2.layout().addLayout(button_layout1)

        back_button = qtw.QPushButton("Back")
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(self.return_to_initial_window1)
        button_layout1.addWidget(back_button, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)

        self.new_window2.show()
    def return_to_initial_window1(self):
        self.new_window2.close()  # Close the current window

    def press_rm(self):
        Tache = []  # List to store the tasks
        task_count = self.table_widget.rowCount()  # Get the number of tasks from the table
        
        if task_count <= 3:
            colors = ['#FF0000', '#00FF00', '#0000FF']
            random.shuffle(colors)
        
        for row in range(task_count):
            task = {}
            task['A'] = int(self.table_widget.cellWidget(row, 1).text())  # Get the arrival time
            task['C'] = int(self.table_widget.cellWidget(row, 2).text())  # Get the execution time
            task['Period'] = int(self.table_widget.cellWidget(row, 3).text())  # Get the period
            task['Dead line'] = int(self.table_widget.cellWidget(row, 4).text())  # Get the deadline
            task['name'] = f'T{row+1}'  # Assign a name to the task
            task['count'] = 0  # Initialize count to 0
            task['time'] = []  # Initialize time list
            
            if task_count <= 3:
                task['color'] = colors[row]  # Assign a unique color to each task
            
            task['y'] = row + 1  # Assign a y-coordinate for drawing
            Tache.append(task)

        time_used = []
        Period, c = [], []

        for T in Tache:
            Period.append(T['Period'])
            c.append(T['C'])

        Period_etude = lcm(*Period)
        GCD = gcd(*c)
        Tache = Priority_rm(Tache)

        for T in Tache:
            for i in range(T['A'], Period_etude, T['Period']):
                start = i
                temp_start = start
                end = i + 1
                temp_C = T['C']
                T['count'] += 1

                while temp_C != 0:
                    if end <= T['Period'] * T['count'] and end <= T['Dead line'] + (T['count'] - 1) * T['Period']:
                        if [temp_start, end] in time_used:
                            if start != end - 1:
                                T['time'].append([start, end - 1])
                            start = end
                            temp_start += 1
                            end += 1
                        else:
                            time_used.append([temp_start, end])
                            temp_C -= 1
                            temp_start += 1
                            end += 1
                    else:
                        # Create a new window to display the error message
                        self.new_window3 = qtw.QWidget()
                        self.new_window3.setWindowTitle("Error")
                        self.new_window3.setLayout(qtw.QVBoxLayout())

                        # Create a label to display the error message
                        error_label = qtw.QLabel(f"The task {T['name']} exceeds its period or deadline.")
                        error_label.setStyleSheet("color: red; font-size: 18px; font-weight: bold;")
                        self.new_window3.layout().addWidget(error_label)

                        self.new_window3.show()
                        return  # Exit the method if there is an error

                if start != end - 1:
                    T['time'].append([start, end - 1])

        if task_count <= 3:
            X = []
            for T in Tache:
                print(f"{T['name']}  :  {T['time']}")
                X.append(T['time'])

            draw_result = Draw(Tache, X, Period_etude, GCD, len(Tache), "RM")

            # Create a new window to display the drawing
            self.new_window3 = qtw.QWidget()
            self.new_window3.setWindowTitle("Drawing Window")
            self.new_window3.setWindowIcon(qtg.QIcon("Reel.ico"))
            self.new_window3.setFixedSize(1000, 700)  # Set the fixed size of the new window
            self.new_window3.setLayout(qtw.QVBoxLayout())

            # Create a label to display the drawing
            label = qtw.QLabel()
            pixmap = qtg.QPixmap.fromImage(draw_result)
            label.setPixmap(pixmap.scaled(1000, 700))  # Scale the pixmap to fit the window size
            self.new_window3.layout().addWidget(label)

            self.new_window3.show()
        else:
            # Create a new window to display the time ranges
            self.new_window3 = qtw.QWidget()
            self.new_window3.setWindowTitle("Time Ranges")
            self.new_window3.setLayout(qtw.QVBoxLayout())
            self.new_window3.setFixedSize(1000,700)

            # Create labels to display the time ranges for each task
            for T in Tache:
                time_label = qtw.QLabel(f"Time ranges for task {T['name']}: {T['time']}")
                time_label.setStyleSheet("font-size: 18px; font-weight: bold;")
                self.new_window3.layout().addWidget(time_label)

            self.new_window3.show()

    def press_dm(self):
        Tache = []  # List to store the tasks
        task_count = self.table_widget.rowCount()  # Get the number of tasks from the table
        if task_count <= 3:
            colors = ['#FF0000', '#00FF00', '#0000FF']
            random.shuffle(colors)
        
        for row in range(task_count):
            task = {}
            task['A'] = int(self.table_widget.cellWidget(row, 1).text())  # Get the arrival time
            task['C'] = int(self.table_widget.cellWidget(row, 2).text())  # Get the execution time
            task['Period'] = int(self.table_widget.cellWidget(row, 3).text())  # Get the period
            task['Dead line'] = int(self.table_widget.cellWidget(row, 4).text())  # Get the deadline
            task['name'] = f'T{row+1}'  # Assign a name to the task
            task['count'] = 0  # Initialize count to 0
            task['time'] = []  # Initialize time list
            
            if task_count <= 3:
                task['color'] = colors[row]  # Assign a unique color to each task
            
            task['y'] = row + 1  # Assign a y-coordinate for drawing
            Tache.append(task)

        time_used = []
        Period, c = [], []

        for T in Tache:
            Period.append(T['Period'])
            c.append(T['C'])
        
        Period_etude = lcm(*Period)
        GCD = gcd(*c)
        Tache = Priority_dm(Tache)
        
        for T in Tache:
            for i in range(T['A'], Period_etude, T['Period']):
                start = i
                temp_start = start
                end = i + 1
                temp_C = T['C']
                T['count'] += 1

                while temp_C != 0:
                    if end <= T['Period'] * T['count'] and end <= T['Dead line'] + (T['count'] - 1) * T['Period']:
                        if [temp_start, end] in time_used:
                            if start != end - 1:
                                T['time'].append([start, end - 1])
                            start = end
                            temp_start += 1
                            end += 1
                        else:
                            time_used.append([temp_start, end])
                            temp_C -= 1
                            temp_start += 1
                            end += 1
                    else:
                        # Create a new window to display the error message
                        self.new_window4 = qtw.QWidget()
                        self.new_window4.setWindowTitle("Error")
                        
                        self.new_window4.setLayout(qtw.QVBoxLayout())

                        # Create a label to display the error message
                        error_label = qtw.QLabel(f"The task {T['name']} exceeds its period or deadline.")
                        error_label.setStyleSheet("color: red; font-size: 18px; font-weight: bold;")
                        self.new_window4.layout().addWidget(error_label)

                        self.new_window4.show()
                        return  # Exit the method if there is an error

                if start != end - 1:
                    T['time'].append([start, end - 1])

        if task_count <= 3:
            X = []
            for T in Tache:
                print(f"{T['name']}  :  {T['time']}")
                X.append(T['time'])

            draw_result = Draw(Tache, X, Period_etude, GCD, len(Tache), "DM")

            # Create a new window to display the drawing
            self.new_window4 = qtw.QWidget()
            self.new_window4.setWindowTitle("Drawing Window")
            self.new_window4.setWindowIcon(qtg.QIcon("Reel.ico"))
            self.new_window4.setFixedSize(1000, 700)  # Set the fixed size of the new window
            self.new_window4.setLayout(qtw.QVBoxLayout())

            # Create a label to display the drawing
            label = qtw.QLabel()
            pixmap = qtg.QPixmap.fromImage(draw_result)
            label.setPixmap(pixmap.scaled(1000, 700))  # Scale the pixmap to fit the window size
            self.new_window4.layout().addWidget(label)

            self.new_window4.show()
        else:
            # Create a new window to display the time ranges
            self.new_window4 = qtw.QWidget()
            self.new_window4.setWindowTitle("Time Ranges")
            self.new_window4.setLayout(qtw.QVBoxLayout())
            self.new_window4.setFixedSize(1000,700)

            # Create labels to display the time ranges for each task
            for T in Tache:
                time_label = qtw.QLabel(f"Time ranges for task {T['name']}: {T['time']}")
                time_label.setStyleSheet("font-size: 18px; font-weight: bold;")
                self.new_window4.layout().addWidget(time_label)

            self.new_window4.show()
app = qtw.QApplication([])
set_dark_theme(app)
mw = MainWindow()
app.exec_()