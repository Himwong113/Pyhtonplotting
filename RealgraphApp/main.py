from tkinter import *
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.figure
from mpl_toolkits import mplot3d
import pandas as pd
from numpy.distutils.fcompiler import none
import plotly.express as px
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statistics as stat
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from pandas import DataFrame
from matplotlib.figure import Figure

df_X = 0
df_Y = 0
df = []


### hardcode detail (function)
def checkdfdetail():
    FilepathName = TxtEntry.get()
    df = pd.read_csv(FilepathName, header=None)
    print(df.head)
    Labelsize1['text'] = "Data Frame :"
    Labelsize2['text'] = str(df.shape[0]) + " X " + str(df.shape[1])
    return df


def TextToInt(selection):
    lenofselection = len(selection)

    colnumnumber = 0
    for i in range(lenofselection):

        if (selection[lenofselection - i - 1] >= 'A') and (selection[lenofselection - i - 1] <= 'z'):
            selection = selection.lower()
            colnumnumber += (ord(selection[lenofselection - i - 1]) - ord('a') + 1) * (pow(26, i))
        else:
            print("input again")
            break
    return int(colnumnumber) - 1


def TextToIntXY():
    df_X = TxtEntryx.get()
    df_X = TextToInt(df_X)
    df_Y = TxtEntryy.get()
    df_Y = TextToInt(df_Y)

    Labelsize2['text'] = "df_X COL :" + str(df_X) + "     df_Y COL :" + str(df_Y)


def update_figure():
    fig = Figure(figsize=(5, 6),
                 dpi=100)

    # list of squares

    # adding the subplot
    fig.add_subplot(111).plot([], [])
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def plot():
    # the figure that will contain the plot
    df = checkdfdetail()
    print(df.head)

    df_X = TxtEntryx.get()
    df_X = TextToInt(df_X)
    df_Y = TxtEntryy.get()
    df_Y = TextToInt(df_Y)

    Labelsize2['text'] = "df_X COL :" + str(df_X) + "     df_Y COL :" + str(df_Y)
    x = df[df_X]
    y = df[df_Y]

    fig = Figure(figsize=(5, 6),
                 dpi=100)

    # list of squares

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.scatter(x, y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=3, column=0,rowspan=9,columnspan=9)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack(row=3, column=0,rowspan=9,columnspan=9)


#### UI Config


window = Tk()
window.title("ABC Graph App")  # top left name
window.geometry("1080x680")  # size is wodth 500height

labelF = Label(window, text="File path :", font='Arial 14')
labelF.grid(row=0, column=0, columnspan=2)
TxtEntry = Entry(window, width=80)
TxtEntry.grid(row=0, column=2)

ButtonSubmit = Button(window, text='Submit', font='Arial 10')
ButtonSubmit.grid(row=0, column=3, sticky='ne', padx=5)
ButtonSubmit['command'] = checkdfdetail

Labelsize1 = Label(window, font='Arial 10')
Labelsize1.grid(row=1, column=0, sticky='ew')
Labelsize2 = Label(window, font='Arial 10')
Labelsize2.grid(row=1, column=1, sticky='ew')

Labelsizex = Label(window, text='X Data', font='Arial 10')
Labelsizex.grid(row=3, column=10, sticky='ew')
TxtEntryx = Entry(window, width=20)
TxtEntryx.grid(row=4, column=10)

Labelsizey = Label(window, text='Y Data', font='Arial 10')
Labelsizey.grid(row=5, column=10, sticky='ew')
TxtEntryy = Entry(window, width=20)

TxtEntryy.grid(row=6, column=10)

ButtonSubmitData = Button(window, text='Submit', font='Arial 10')
ButtonSubmitData.grid(row=7, column=10, sticky='ns', padx=5)
####hardcode detail

# C:\Jupyter\Datatest.csv

ButtonSubmitData['command'] = TextToIntXY
ButtonSubmitData['command'] = update_figure
ButtonSubmitData['command'] = plot

# plot function is created for
# plotting the graph in
# tkinter window


window.mainloop()
