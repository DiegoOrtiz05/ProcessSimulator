import time
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import threading
from Processimulator import Cpu, Process, ProcessCreator, Simulator, dicProcess, listEvents, getBussy
from tkinter.constants import CENTER, NO, END, RIGHT, Y
import constants as cs
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Variable de simulacion
simulation = Simulator('time', 1, 5, 20, 4, 4, 3)


# PRoceso al iniciar simulacion
def startSimulation():
    try:
        time = int(variableEntryTSimulacion.get())

        # start()
        startTread(time)
    except ValueError:
        messagebox.showerror('Dato incorrecto', 'Ingresa un numero entero positivo')


def startTread(time):
    simulation = Simulator(time, 1, 5, 20, 4, 4, 3)

    hiloSimulation = threading.Thread(target=simulation.start)
    hiloSimulation.start()


titleWindow = 'Process Manager Project'
colorFondo = '#173055'
colorFuentePrincipal = '#FFFFFF'
colorEntry = '#F5F5F5'
mensajeHora = 'Reloj Sistema:'
mensajeTSimulacion = 'Tiempo de simulacion'
mensajeEstadoCpu = 'Estado CPU: '
mensajeColaProcesos = 'Cola de Procesos en:'
fuenteTitulo = ('Mixed', 30)
fuentePrincipal = ('Mixed,20')
mensajeTablaProcesos = 'Cola de procesos: '
list_length_process = [3, 5, 10]

# Ventana Principal
ventana = tk.Tk()
ventana.geometry('1200x720')
ventana.title(titleWindow)
ventana.resizable(0, 0)
ventana.config(bg=colorFondo)
# ventana.configure(background='black')

# Configurar el grid
ventana.rowconfigure(0, weight=0)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1)
ventana.rowconfigure(7, weight=1)
ventana.rowconfigure(8, weight=1)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)
ventana.columnconfigure(4, weight=1)
ventana.columnconfigure(5, weight=1)
ventana.columnconfigure(6, weight=1)
ventana.columnconfigure(7, weight=1)
ventana.columnconfigure(8, weight=1)
ventana.columnconfigure(9, weight=1)
ventana.columnconfigure(10, weight=1)
ventana.columnconfigure(11, weight=1)
ventana.columnconfigure(12, weight=1)
ventana.columnconfigure(13, weight=1)


def updateTableProcess():
    table_process.delete(*table_process.get_children())
    list_length_process[0] = 0
    list_length_process[1] = 0
    list_length_process[2] = 0
    for clave in dicProcess:
        statusComboBox = comboBoxEstadosProcesos.current()
        procesos = dicProcess[clave]
        if procesos[7] == 'Blocked':
            list_length_process[2] += 1
        elif procesos[7]=='Ready':
            list_length_process[1] += 1
        elif procesos[7] =='Running':
            list_length_process[0] += 1
        if statusComboBox == 0:
            _addProcess(table_process, Process(procesos[0], str(procesos[1]) + "/" + str(procesos[2]),
                                               str(procesos[3]) + "/" + str(procesos[4]),
                                               str(procesos[5]) + "/" + str(procesos[6]), procesos[7]),
                        str(procesos[8]))
        elif statusComboBox == 1:
            if procesos[7] == 'Blocked':
                _addProcess(table_process, Process(procesos[0], str(procesos[1]) + "/" + str(procesos[2]),
                                                   str(procesos[3]) + "/" + str(procesos[4]),
                                                   str(procesos[5]) + "/" + str(procesos[6]), procesos[7]),
                            str(procesos[8]))
        elif statusComboBox == 2:
            if procesos[7] == 'Ready':
                _addProcess(table_process, Process(procesos[0], str(procesos[1]) + "/" + str(procesos[2]),
                                                   str(procesos[3]) + "/" + str(procesos[4]),
                                                   str(procesos[5]) + "/" + str(procesos[6]), procesos[7]),
                            str(procesos[8]))
        elif statusComboBox == 3:
            if procesos[7] == 'Running':
                _addProcess(table_process, Process(procesos[0], str(procesos[1]) + "/" + str(procesos[2]),
                                                   str(procesos[3]) + "/" + str(procesos[4]),
                                                   str(procesos[5]) + "/" + str(procesos[6]), procesos[7]),
                            str(procesos[8]))

    updateTableEvents()
    #updateHistrograma()


    ventana.after(1000, updateTableProcess)


def updateTableEvents():
    table_events.delete(*table_events.get_children())
    for event in listEvents:
        _addEvents(table_events, event)
    if getBussy['status']:
        labelEstadoCPU.config(text=mensajeEstadoCpu + ' Bussy')
    else:
        labelEstadoCPU.config(text=mensajeEstadoCpu + ' Idle')
    if len(table_events.get_children())>4:
        table_events.yview((table_events.index(table_events.get_children()[-1])))


"""def updateHistrograma():
    figure.set_ydata(list_length_process)
    figure.canvas.draw()
    figure.canvas.flush_events()
"""

# Componente Titulo Principal
labelTitulo1 = tk.Label(ventana, text=titleWindow, bg=colorFondo, fg=colorFuentePrincipal, font=fuenteTitulo)
labelTitulo1.grid(row=1, column=1, columnspan=5)

# Componente Hora del sistema
labelHoraSistema = tk.Label(ventana, text=mensajeHora + datetime.now().time().strftime('%H:%M:%S'),
                            bg=colorFondo, fg=colorFuentePrincipal, font=fuentePrincipal)
labelHoraSistema.grid(row=1, column=10)


# Funcionamiento Hora del sistema
def updateHour():
    while True:
        labelHoraSistema.config(text=mensajeHora + datetime.now().time().strftime('%H:%M:%S'))
        # updateTableProcess()
        # print('Hora Actual:'+ mensajeHora+datetime.now().time().strftime('%H:%M:%S'))
        time.sleep(1)


hiloTime = threading.Thread(target=updateHour)
hiloTime.start()

# Separador
separador = ttk.Separator(ventana, orient='horizontal')
separador.grid(row=1, column=1, sticky='SWE', columnspan=12)

# Input Tiempo de Simulacion
# Texto Tiempo de simulacion
labelTSimulacion = tk.Label(ventana, text=mensajeTSimulacion, bg=colorFondo, fg=colorFuentePrincipal,
                            font=fuentePrincipal)
labelTSimulacion.grid(row=2, column=1, sticky='SWE', columnspan=2)

# Entrada Tiempo de Simulacion

imageSimulacion = tk.PhotoImage(file='sources/images/entry1.png')

labelEntrySimulacion = tk.Label(ventana, image=imageSimulacion, border=0, bg=colorFondo)
labelEntrySimulacion.grid(row=2, column=3, sticky='SWE', columnspan=2)
variableEntryTSimulacion = tk.StringVar(value='')
entryTSimulacion = tk.Entry(ventana, bg=colorEntry, border=0, font=fuentePrincipal, width=15,
                            textvariable=variableEntryTSimulacion)
entryTSimulacion.grid(row=2, column=3, columnspan=2, sticky='S', pady=10)

# BotonStarSimulacion
imageButtonSimulacion = tk.PhotoImage(file='sources/images/buttom.png')
bottomStarSimulacion = tk.Button(ventana, image=imageButtonSimulacion, bd=0, bg=colorFondo, command=startSimulation)
bottomStarSimulacion.grid(row=2, column=5, sticky='S')

# Estado CPU
labelEstadoCPU = tk.Label(ventana, text=mensajeEstadoCpu, bg=colorFondo, fg=colorFuentePrincipal, font=fuentePrincipal)
labelEstadoCPU.grid(row=2, column=9, sticky='WE', columnspan=2)

# Tabla de procesos
imageTablaProcesos = tk.PhotoImage(file='sources/images/frameEstadoProcesos.png')
labelTablaProceso = tk.Label(ventana, image=imageTablaProcesos, bg=colorFondo)
labelTablaProceso.grid(row=3, column=6, columnspan=7, rowspan=2)
panelTablaProcesos = tk.PanedWindow(ventana, bg='white', width=450, height=140)
panelTablaProcesos.grid(row=3, column=6, columnspan=7, rowspan=2)
labelTextProcesos = tk.Label(panelTablaProcesos, text=mensajeTablaProcesos, font=fuentePrincipal, bd=0)
labelTextProcesos.grid(row=0, column=0, sticky='WE')

# ComboBox Cola de procesos
# Label
labelColaProcesos = tk.Label(ventana, text=mensajeColaProcesos, bg=colorFondo, fg=colorFuentePrincipal,
                             font=fuentePrincipal)
labelColaProcesos.grid(row=4, column=1, columnspan=2, sticky='N')
# ComboBoxEstados
comboBoxEstadosProcesos = ttk.Combobox(ventana, state='readonly', values=['Todos', 'Blocked', 'Ready', 'Execute'],
                                       font=fuentePrincipal)
comboBoxEstadosProcesos.set('Todos')
comboBoxEstadosProcesos.grid(row=4, column=3, sticky='N')

# GraficaEstadoProcesos
imageEstadosProcesos = tk.PhotoImage(file='sources/images/grapframe.png')
labelGrapfEstadosProceso = tk.Label(ventana, image=imageEstadosProcesos, bg=colorFondo, bd=0)
labelGrapfEstadosProceso.grid(row=5, column=1, sticky='NSWE', columnspan=5, rowspan=3)
panelEstadoProcesos = tk.PanedWindow(ventana, bg='white', width=280, height=160)
panelEstadoProcesos.grid(row=5, column=1, columnspan=5, rowspan=3)

# TextArea Eventos

imageEventos = tk.PhotoImage(file='sources/images/frameEventos.png')
labelEventos = tk.Label(ventana, image=imageEventos, bg=colorFondo)
labelEventos.grid(row=6, column=6, sticky='NSWE', columnspan=5, rowspan=2)
panelEventos = tk.PanedWindow(ventana, bg='white', width=300, height=100)
panelEventos.grid(row=6, column=6, columnspan=5, rowspan=2, sticky='WE', padx=60)
labelTextEventos = tk.Label(panelEventos, text='Eventos', font=fuentePrincipal, bg='white', bd=0)
panelEventos.columnconfigure(0, weight=1)
panelEventos.rowconfigure(0, weight=1)
panelEventos.rowconfigure(1, weight=10)

labelTextEventos.grid(row=0, column=0, sticky='EW')


# Prueba Tablas


def _init():
    # _test_table_process(table_process) #Este es pa probar
    _test_table_events(table_events)  # Este es pa probar


def _set_properties_table_process(master):
    table_frame = tk.Frame(master, bg='white')
    table_frame.grid(row=1, column=0)
    table_scroll = tk.Scrollbar(table_frame)
    table_scroll.pack(side=RIGHT, fill=Y)
    table = ttk.Treeview(table_frame, height=8)
    table['columns'] = cs.COLUMNS_NAME
    table_scroll.config(command=table.yview)
    _create_table_process(table, cs.COLUMNS_PROCESSES_STATUS)
    return table


def _set_properties_table_events(master):
    # table_scroll.pack(side=RIGHT, fill=Y)
    table = ttk.Treeview(master=master, height=4)
    table.column("#0", anchor=tk.CENTER, stretch=1, width=50)
    table.grid(row=1, column=0, sticky='SNWE')
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


# Add elements to table
def _addProcess(table, process, quantum):
    table.insert("", END, text=process.id, values=(
        process.life_Time,
        process.NextIO,
        process.IO,
        process.status,
        quantum
    ))


# Add events to table
def _addEvents(table, text):
    table.insert("", tk.END, text=text)


def _clearTableProcess():
    table_process.get_children()


# (self,id,life_Time,NextIO,IO,status):
def _test_table_process(table):
    for i in range(40):
        _addProcess(table, Process(i, "0/0", "2/2", 2, "Busy"))


# (self,id,life_Time,NextIO,IO,status):
def _test_table_events(table):
    for i in range(5):
        _addEvents(table, f"Este es un nuevo evento  assssssssssssssssssadsddddddddddddddddddddddddddddsssssssd ${i}")


def _set_list_numbers(list_ready, list_blocked, list_finished):
    list_length_process = [list_ready.__len__(), list_blocked.__len__(), list_finished.__len__()]


def _create_histogram2():
    x=['Blocked','Ready','Running']
    figure1 = plt.figure(figsize=(8, 6), dpi=35)
    plt.ion()
    plt.bar(x, list_length_process)
    plt.title('Current Process Status', fontsize=20)
    plt.xlabel('Status')
    plt.ylabel('No Procesos')
    plt.ylim(0,10)
    plt.rcParams.update({'font.size':22})
    bar1 = FigureCanvasTkAgg(figure1, panelEstadoProcesos)
    bar1.get_tk_widget().grid(row=0, column=0, sticky='SNWE')
    while True:
        plt.cla()
        plt.title('Current Process Status', fontsize=20)
        plt.xlabel('Status', fontsize=20)
        plt.ylabel('No Procesos',fontsize=20)
        plt.ylim(0, 10)
        plt.rcParams.update({'font.size': 22})
        plt.bar(x,list_length_process)
        plt.draw()
        time.sleep(1)




table_process = _set_properties_table_process(panelTablaProcesos)
table_events = _set_properties_table_events(panelEventos)
hiloHistograma = threading.Thread(target=_create_histogram2)
hiloHistograma.start()
updateTableProcess()

# _init()
ventana.mainloop()
