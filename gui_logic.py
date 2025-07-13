from gui_ui import Ui_Form as View
import Game
from PySide6.QtCore import (Qt)

from PySide6.QtCore import QPropertyAnimation, QRect, QParallelAnimationGroup, QPoint, QTimer
from PySide6.QtWidgets import QApplication, QWidget

import bfs, dfs, Astar
from Astar import manhDist, eucliDist


import time

class GUI(QWidget, View):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.intial_state=self.lineEdit.text()
        self.setupUi(self)
        self.counter=0
        self.timer = QTimer(self)
        self.setStyleSheet("""
                           
             QWidget {
                background-color: linen;  
            }
                           
            QLabel {
                font-size: 24px;  
                border: 2px solid black;  
                background-color: pink;
            
            }
            QPushButton{
                     background-color: white;
                           
                           
                     }
                           
             
                           
             
         """
           
                        )
        

        self.label_9.setStyleSheet("""
            QLabel {
                font-size: 10px;   
                background-color:white; 
            }
        """)

        self.depth_label.setStyleSheet("""
            QLabel{
                font-size: 10px;   
                background-color:white;} 
                                    """)
        
        self.nodes_label.setStyleSheet("""
           QLabel{ font-size: 10px;   
                background-color:white; }
                                    """)
        

        self.cost_label.setStyleSheet("""
            QLabel{font-size: 10px;   
                background-color:white; }
                                    """)
        

        self.path_label.setStyleSheet("""
            QLabel{font-size: 10px;   
                background-color:white; }
                                    """)
        
        
        self.depth_disp_label.setStyleSheet("""
                    QLabel{
                             font-size: 10px;  
                            font-size= 10px;
                                            }
                                            """)
        self.cost_disp_label.setStyleSheet("""
                    QLabel{
                             font-size: 10px;  
                            font-size= 10px;
                                            }
                                            """)
        self.nodes_disp_label.setStyleSheet("""
                    QLabel{
                             font-size: 10px;  
                            font-size= 10px;
                                            }
                                            """)
        
        self.path_disp_label.setStyleSheet("""
                    QLabel{
                             font-size: 10px;  
                            font-size= 10px;
                                            }
                                            """)
                                            

       


        
        time_1 = time.time()
        self.bfs_button.clicked.connect(self.run_bfs)
        time_2 = time.time()
        
        time_1 = time.time()
        self.dfs_button.clicked.connect(self.run_dfs)
        time_2 = time.time()
        # # eucli

        time_1 = time.time()
        self.eucli_button.clicked.connect(self.run_Astar_Eucli) 
        time_2 = time.time()
        # # manh

        time_1 = time.time()
        self.manh_button.clicked.connect(self.run_Astar_Manh)
        time_2 =time.time()


    def validate_input(self, user_input):
       

        
        if len(user_input) != 9:
            return False

        
        if not all(char in '012345678' for char in user_input):
            return False

        
        if len(set(user_input)) != 9:
            return False

        return True

    def run_bfs(self):
        user_input = self.validate_input(self.lineEdit.text())

        if user_input:

            path, visited_len, counter=bfs.bfs(self.lineEdit.text())
            self.depth_disp_label.setText(str(counter))
            self.nodes_disp_label.setText(str(visited_len))
            self.path_disp_label.setText(str(path))
            self.cost_disp_label.setText(str(len(path)-1))
            self.grid_processing(path, visited_len)

        else:
            print("enter valid input")

    def run_dfs(self):

        user_input = self.validate_input(self.lineEdit.text())

        if user_input:
            path, visited_len, counter=dfs.DFS(self.lineEdit.text())
            self.depth_disp_label.setText(str(counter))
            self.nodes_disp_label.setText(str(visited_len))
            self.path_disp_label.setText(str(path))
            self.cost_disp_label.setText(str(len(path)-1))
            self.grid_processing(path, visited_len)
        
        else:
            print("enter valid input")



    def run_Astar_Eucli(self):
        user_input = self.validate_input(self.lineEdit.text())

        if user_input:
            path, visited_len, counter=Astar.aStarWithBothH(self.lineEdit.text(),eucliDist)
            self.depth_disp_label.setText(str(counter))
            self.nodes_disp_label.setText(str(visited_len))
            self.path_disp_label.setText(str(path))
            self.cost_disp_label.setText(str(len(path)-1))
            self.grid_processing(path, visited_len)
        else:
            print("enter valid input")
        
    def run_Astar_Manh(self):
        user_input = self.validate_input(self.lineEdit.text())

        if user_input:
            path, visited_len, counter=Astar.aStarWithBothH(self.lineEdit.text(),manhDist)
            self.depth_disp_label.setText(str(counter))
            self.nodes_disp_label.setText(str(visited_len))
            self.path_disp_label.setText(str(path))
            self.cost_disp_label.setText(str(len(path)-1))
            self.grid_processing(path, visited_len)
        else:
            print("enter valid input")
        


    


    def grid_processing(self,paths, no_expanded):
            self.current_state_index = 0
            self.paths = paths
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_grid)
            self.timer.start(2000)
                
        
        
    def update_grid(self):
        if self.current_state_index < len(self.paths):
            current_state = self.paths[self.current_state_index]
            for i in range(len(current_state)):
                label = getattr(self, f'label_{i}', None)
                if label:
                    if current_state[i] == '0':
                        label.setText(" ")
                    else:
                        label.setText(current_state[i])
            self.current_state_index += 1
        else:
            self.timer.stop()

                
        

if __name__ == "__main__":
    app = QApplication()
    window = GUI()
    window.show()
    app.exec()