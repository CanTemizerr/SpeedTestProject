import numpy as py
import pandas as pd
import os
class Analysis1():
    def __init__(self,file_cvs="speed_result.cvs"):
        self.file_cvs=file_cvs
        
    def analizyap(self):
        if not os.path.exists(self.file_cvs) or os.path.getsize(self.file_cvs) == 0:
                    self.df = pd.DataFrame(columns=["Download", "Upload", "Ping", "Time"])
       
        self.df = pd.read_csv(self.file_cvs, header=None, names=["Download", "Upload", "Ping", "Time"])
        print(self.df.describe().round(2))
    def allresult(self):
        if not os.path.exists(self.file_cvs) or os.path.getsize(self.file_cvs) == 0:
                            self.df = pd.DataFrame(columns=["Download", "Upload", "Ping", "Time"])
        self.df = pd.read_csv(self.file_cvs, header=None, names=["Download", "Upload", "Ping", "Time"])    
        print(self.df)

        
        