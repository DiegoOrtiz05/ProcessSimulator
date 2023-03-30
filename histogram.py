from tkinter import ttk

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas import DataFrame

list_length_process = [3, 5, 10]
window = tk.Tk()

def _init():
    window.geometry("800x500")
    _create_histogram()
    window.mainloop()

def _set_list_numbers(list_ready,list_blocked,list_finished):
    list_length_process = [list_ready.__len__(), list_blocked.__len__(),list_finished.__len__()]


def _create_histogram():
    #data_labels = ["Busy","Ready","Finished"]
    data1 = {'Status': ['Busy', 'Ready', 'Finished'],
             'NoProcess': list_length_process
             }
    df1 = DataFrame(data1, columns=['Status', 'NoProcess'])
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, window)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['Status', 'NoProcess']].groupby('Status').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Current Process Status')
_init()