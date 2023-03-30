import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, NO, END, RIGHT, Y
import constants as cs
from Processimulator import Process

#window = tk.Tk()

table_process = ttk.Treeview()
table_events = ttk.Treeview()

def _init():

    table_process_test = _set_properties_table_process()
    table_events_test = _set_properties_table_events()
    _test_table_process(table_process_test) #Este es pa probar
    _test_table_events(table_events_test) #Este es pa probar



def _set_properties_table_process(master):
    table_frame = tk.Frame(master)
    table_frame.pack(pady=20)
    table_scroll = tk.Scrollbar(table_frame)
    table_scroll.pack(side=RIGHT, fill=Y)
    table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
    table['columns'] = cs.COLUMNS_NAME
    table_scroll.config(command=table.yview)
    _create_table_process(table, cs.COLUMNS_PROCESSES_STATUS)
    return table

def _set_properties_table_events(master):
    table_frame = tk.Frame(master,width="600",height="100")
    table_frame.pack(pady=20)
    table_scroll = tk.Scrollbar(table_frame)
    table_scroll.pack(side=RIGHT, fill=Y)
    table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
    table_scroll.config(command=table.yview)
    _create_table_events(table)
    return table



def getTableProcess():
    return table_process

def _create_table_process(table, columnsInput):
    table.column("#0", width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[0], width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[1], width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[2], width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[3], width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[4], width=80, anchor=CENTER)
    table.heading("#0", text='Process', anchor=CENTER)
    table.heading(cs.COLUMNS_NAME[0], text=columnsInput[1], anchor=CENTER)
    table.heading(cs.COLUMNS_NAME[1], text=columnsInput[2], anchor=CENTER)
    table.heading(cs.COLUMNS_NAME[2], text=columnsInput[3], anchor=CENTER)
    table.heading(cs.COLUMNS_NAME[3], text=columnsInput[4], anchor=CENTER)
    table.heading(cs.COLUMNS_NAME[4], text=columnsInput[5], anchor=CENTER)
    table.pack()

def _create_table_events(table):
    table.column("#0", width=80, anchor=CENTER)
    table.heading("#0", text=cs.COLUMN_NAME_EVENTS, anchor=CENTER)
    table.pack()



# Add elements to table
def _addProcess(table, process):
    table.insert("", END, text=process.id, values=(
        process.life_Time,
        process.NextIO,
        process.IO,
        process.status,
        process.quantum
    ))

# Add events to table
def _addEvents(table, text):
    table.insert("", END, text=text)


def _clearTableProcess():
    table_process.get_children()


# (self,id,life_Time,NextIO,IO,status):
def _test_table_process(table):
    for i in range(40):
        _addProcess(table, Process(i, "0/0", "2/2", 2, "Busy"))

# (self,id,life_Time,NextIO,IO,status):
def _test_table_events(table):
    for i in range(10):
        _addEvents(table,"Este es un nuevo evento $i")


