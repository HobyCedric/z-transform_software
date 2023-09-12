# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:23:49 2021

@author: Foza
"""

import tkinter
from tkinter import messagebox
from Fonction import *


        
#definition des labels changeant à chaque evenement
class function_label_choice:
    def __init__(self,c_Text):
        self.fonction_label = tkinter.Label(app,bg ="white",text= c_Text ,width = 23, height = 3,font=("Century Gothic",10))
    def mouse_on(self,event):
        self.fonction_label.configure(bg = "light grey")
    def mouse_off(self,event):
        self.fonction_label.configure(bg = "white")
    def extract_value(self,event):
        global choice_value
        self.choice = self.fonction_label.cget("text")
        if self.choice == TABLE_FONCTION[0]:
            choice_value = 1
        if self.choice == TABLE_FONCTION[1]:
            choice_value = 2
        if self.choice == TABLE_FONCTION[2]:
            choice_value = 3
        if self.choice == TABLE_FONCTION[3]:
            choice_value = 4
        if self.choice == TABLE_FONCTION[4]:
            choice_value = 5
        if self.choice == TABLE_FONCTION[5]:
            choice_value = 6
        show_all()

#pour les intitulés
class function_label_screen:
    def __init__(self,c_Text):
        self.screen_label = tkinter.Label(cadre, bg = "white", text = c_Text,font=("Century Gothic",10))

#pour les zones de textes
class function_entry:
    def __init__(self):
        self.fonction_entry = tkinter.Entry(cadre, relief = "flat",font=("Century Gothic",10), bg = "white", width = 15)

class entry_canvas:
    def __init__(self):
        self.canva_bordure = tkinter.Label(cadre, image = image1, bg = "white")
    def mouse_on(self,event):
        self.canva_bordure.configure(image = image2) 
    def mouse_off(self,event):
        self.canva_bordure.configure(image = image1)
class button:
    def __init__(self):
        self.button_label = tkinter.Label(cadre, image = image3, bg = "white")
    def mouse_on(self,event):
        self.button_label.configure(image = image4)
    def mouse_off(self,event):
        self.button_label.configure(image = image3)
   


def destroy_widget_frame():
    for widget in cadre.winfo_children():
        widget.destroy()


def show_all():
    global TABLE_VARIABLE_VARIABLE
    global Var1,Var2,Var3,Var4
    
    X_PLACE_SCREEN_VARIABLE = 20
    Y_PLACE_SCREEN_VARIABLE = 0

    X_PLACE_ENTRY = 20
    Y_PLACE_ENTRY = 34

    X_PLACE_LABEL = 5
    Y_PLACE_LABEL = 20
    if choice_value == 1:
        TABLE_VARIATION_FONCTION = VARIABLE_FONCTION_1
    if choice_value == 2:
        TABLE_VARIATION_FONCTION = VARIABLE_FONCTION_2
    if choice_value == 3:
        TABLE_VARIATION_FONCTION = VARIABLE_FONCTION_3
    if choice_value == 4:
        TABLE_VARIATION_FONCTION = VARIABLE_FONCTION_4
    if choice_value == 5:
        TABLE_VARIATION_FONCTION = VARIABLE_FONCTION_5
    if choice_value == 6:
        TABLE_VARIATION_FONCTION = VARIABLE_FONCTION_6  
    #suppression des éléments présents sur l'écran
    destroy_widget_frame()
    #apparition des éléments sur l'ecran
    for variable in TABLE_VARIATION_FONCTION:
        COUNT_VARIABLE = 0
        #id_Label
        variable = function_label_screen(variable)
        variable.screen_label.place( x= X_PLACE_SCREEN_VARIABLE, y=Y_PLACE_SCREEN_VARIABLE)
        Y_PLACE_SCREEN_VARIABLE += 70
        COUNT_VARIABLE += 1
    if choice_value == 1 or choice_value == 3 or choice_value == 6:
        #bordure
        var1 = entry_canvas()
        var2 = entry_canvas()
        var3 = entry_canvas()
         #saisie
        Var1 = function_entry()
        Var2 = function_entry()
        Var3 = function_entry()

        TABLE_VARIABLE_VARIABLE = [Var1,Var2,Var3]
        TABLE_VARIABLE_CANVA  = [var1,var2,var3]
        
    if choice_value == 2 or choice_value == 4 or choice_value == 5:
       #bordure
        var1 = entry_canvas()
        var2 = entry_canvas()
        var3 = entry_canvas()
        var4 = entry_canvas()
        #saisie
        Var1 = function_entry()
        Var2 = function_entry()
        Var3 = function_entry()
        Var4 = function_entry()
        TABLE_VARIABLE_VARIABLE = [Var1,Var2,Var3,Var4]
        TABLE_VARIABLE_CANVA  = [var1,var2,var3, var4]
        
    if choice_value == 1 or choice_value == 3 or choice_value == 6:
        Var1.fonction_entry.bind('<Enter>',var1.mouse_on)
        var1.canva_bordure.bind('<Enter>',var1.mouse_on)
        var1.canva_bordure.bind('<Leave>',var1.mouse_off)
        
        Var2.fonction_entry.bind('<Enter>',var2.mouse_on)
        var2.canva_bordure.bind('<Enter>',var2.mouse_on)
        var2.canva_bordure.bind('<Leave>',var2.mouse_off)
        
        Var3.fonction_entry.bind('<Enter>',var3.mouse_on)
        var3.canva_bordure.bind('<Enter>',var3.mouse_on)
        var3.canva_bordure.bind('<Leave>',var3.mouse_off)
        
    if choice_value == 2 or choice_value == 4 or choice_value == 5:
         
         Var1.fonction_entry.bind('<Enter>',var1.mouse_on)
         var1.canva_bordure.bind('<Enter>',var1.mouse_on)
         var1.canva_bordure.bind('<Leave>',var1.mouse_off)
         
         Var2.fonction_entry.bind('<Enter>',var2.mouse_on)
         var2.canva_bordure.bind('<Enter>',var2.mouse_on)
         var2.canva_bordure.bind('<Leave>',var2.mouse_off)
         
         Var3.fonction_entry.bind('<Enter>',var3.mouse_on)
         var3.canva_bordure.bind('<Enter>',var3.mouse_on)
         var3.canva_bordure.bind('<Leave>',var3.mouse_off)
         
         Var4.fonction_entry.bind('<Enter>',var4.mouse_on)
         var4.canva_bordure.bind('<Enter>',var4.mouse_on)
         var4.canva_bordure.bind('<Leave>',var4.mouse_off)
         
    for var1 in TABLE_VARIABLE_CANVA:
        var1.canva_bordure.place(x = X_PLACE_LABEL, y = Y_PLACE_LABEL)
        Y_PLACE_LABEL += 70
    
  
    for var in TABLE_VARIABLE_VARIABLE:
        var.fonction_entry.place(x = X_PLACE_ENTRY, y =Y_PLACE_ENTRY)
        Y_PLACE_ENTRY += 70

        
    #apparition du bouton:
    button_label = button()
    button_label.button_label.place( x = X_PLACE_SCREEN_VARIABLE - 15, y = Y_PLACE_SCREEN_VARIABLE*COUNT_VARIABLE + 10)
    button_label.button_label.bind('<Enter>',button_label.mouse_on)
    button_label.button_label.bind('<Leave>',button_label.mouse_off)
    button_label.button_label.bind('<Button-1>',clic_button)

def clic_button(event):
    try:
        if choice_value == 1 or choice_value == 3 or choice_value == 6:
            V1 = float(Var1.fonction_entry.get())
            V2 = float(Var2.fonction_entry.get())
            V3 = float(Var3.fonction_entry.get())
        if choice_value == 2 or choice_value == 4 or choice_value == 5:
            V1 = float(Var1.fonction_entry.get())
            V2 = float(Var2.fonction_entry.get())
            V3 = float(Var3.fonction_entry.get())
            V4 = float(Var4.fonction_entry.get())
    
    #creation de la fenetre pur l'affichage de la réponse
        result = tkinter.Toplevel()
        result.configure(bg = "white")
        result.title("G(z)")
        result.iconbitmap('logo.ico')
        result.resizable(width = False, height = False )
        
        intitule = tkinter.Label(result, bg = "white", text = "La transformée en Z:", font =("Century Gothic", 10))
        intitule.place( x = 5, y = 5)
        varResult = tkinter.StringVar()
        result_label = tkinter.Label(result, bg = "white",width = 45, height = 8,textvariable = varResult, font=("Century Gothic", 10))
        result_label.place(x = 10, y =30)
    
        #dimension de la fenetre toplevel
        ecranX = int(app.winfo_screenwidth()) 
        ecranY = int(app.winfo_screenheight())
        fenetreX = 400
        fenetreY = 200
        
        posX = (ecranX // 2) - (fenetreX // 2)
        posY = (ecranY // 2) - (fenetreY // 2)

        geo = "{}x{}+{}+{}".format(fenetreX,fenetreY,posX,posY) 
        result.geometry(geo)
        
        if choice_value == 1:
            varResult.set(Fonction1(V1,V2,V3))
        if choice_value == 2:
            varResult.set(Fonction2(V1,V2,V3,V4))
        if choice_value == 3:
            varResult.set(Fonction3(V1,V2,V3))
        if choice_value == 4:
            varResult.set(Fonction4(V1,V2,V3,V4))
        if choice_value == 5:
            varResult.set(Fonction5(V1,V2,V3,V4))
        if choice_value == 6:
            varResult.set(Fonction6(V1,V2,V3))
    except ValueError:
        
        messagebox.showwarning("Transformée en Z","Verifiez les valeurs saisies")
    except UnboundLocalError:
        messagebox.showwarning("Transformée en Z","Verifiez les valeurs saisies")
    except ZeroDivisionError:
        result.destroy()
        messagebox.showwarning("Transformée en Z","Division par zéro")
 
#element pour la table des fonctions
TABLE_FONCTION  = ["         G0\nG(p) = ----\n          (1+ τ.p)","                       G0.e^(-nTep)\nG(p) = ---------------\n          (1+ τ.p)","         1\nG(p) = ---------------\n             τ'.p(1+ τ.p)","         G0\nG(p) = ---------------\n             (1+τ1.p)(1+ τ2.p)","         G0\nG(p) = -------------------------------\n  1 + 2m (p/w0) + (p/w0)^2","         G0\nG(p) = ----\n          (1+ τ.p)^2"]
VARIABLE_FONCTION_1 = ["La valeur de G0:","La valeur de τ:","La valeur de Te:"]
VARIABLE_FONCTION_2 = ["La valeur de G0:","La valeur de τ:","La valeur de Te:","La valeur de n:"]
VARIABLE_FONCTION_3 = ["La valeur de τ:","La valeur de τ':","La valeur de Te:"]
VARIABLE_FONCTION_4 = ["La valeur de G0:","La valeur de τ1:","La valeur de τ2:","La valeur de Te:"]
VARIABLE_FONCTION_5 = ["La valeur de G0:","La valeur de m:","La valeur de w0:","La valeur de Te:"]
VARIABLE_FONCTION_6 = ["La valeur de G0:","La valeur de τ:","La valeur de Te:"]
TABLE_VARIABLE_FONCTION = []
TABLE_VARIABLE_VARIABLE = []
X_PLACE_INIT = 0
Y_PLACE_INIT = 0

#Creation de la fenetre
        
app = tkinter.Tk()
app.title("Transformée en Z")
app.iconbitmap('logo.ico')
app.resizable(width = False, height = False )
app.configure(bg = "white")


#image pour le champs de saisie
image1 = tkinter.PhotoImage(file = "OffFocuss1.gif")
image2 = tkinter.PhotoImage(file = "onFocuss.gif")
#image pour le boutton
image3 = tkinter.PhotoImage(file = "button1.gif")
image4 = tkinter.PhotoImage(file = "button2.gif")

#affichage table des fonctions
for fonction in TABLE_FONCTION:
    fonction =function_label_choice(fonction)
    fonction.fonction_label.place(x = X_PLACE_INIT , y = Y_PLACE_INIT)
    Y_PLACE_INIT += 57
    #evenement entrer et sortie de la souris
    fonction.fonction_label.bind('<Enter>',fonction.mouse_on)
    fonction.fonction_label.bind('<Leave>',fonction.mouse_off)
    fonction.fonction_label.bind('<Button-1>',fonction.extract_value)

#creation d'un cadre
cadre = tkinter.Frame(app, width = 300, height = 342, bg = "white")
cadre.place(x = 195,y = 0)
#Texte d'accueil
Texte_accueil = tkinter.Label(cadre, text = "Bienvenue sur \nTransformée en Z.", font =("Century Gothic", 20), bg = "white")
Texte_accueil.place(x = 30, y = 100)
#dessin de la ligne
ligne = tkinter.Canvas(app, width = 0.5, height = 800, bg = "light grey")
ligne.place(x = 190, y = 0)
#dimensionnement de la fenetre

ecranX = int(app.winfo_screenwidth()) 
ecranY = int(app.winfo_screenheight())
fenetreX = 500
fenetreY = 342

posX = (ecranX // 2) - (fenetreX // 2)
posY = (ecranY // 2) - (fenetreY // 2)

geo = "{}x{}+{}+{}".format(fenetreX,fenetreY,posX,posY) 
app.geometry(geo)
#app.overrideredirect(1)
app.mainloop()