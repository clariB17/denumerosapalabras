from __future__ import (division, unicode_literals, print_function)
import wx
from wx.core import StaticText
from numerosaletras import *

class LeeNumeros(wx.Panel):
    '''Main LeeNumeros dialog'''

    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        sizer = wx.BoxSizer(wx.VERTICAL)  # Main vertical sizer

        self.display = wx.TextCtrl(self)  # Current numeros
        sizer.Add(self.display, 0, wx.EXPAND | wx.BOTTOM,10)  # Add to main sizer
        self.display.SetMaxLength(15) #Limita la entrada a 15 caracteres solo si la entrada es por teclado

        gsizer = wx.GridSizer(4, 3, 8, 8)
        for row in (("1", "2", "3"), ("4", "5", "6"),
                    ("7", "8", "9"), ("","0", "C")):
            for label in row:
                b = wx.Button(self, label=label, size=(190, -1))
                gsizer.Add(b)
                b.Bind(wx.EVT_BUTTON, self.OnButton)
        sizer.Add(gsizer, 1, wx.EXPAND)

        # [    boton     ]
        b = wx.Button(self, label="Escribir numero")
        b.Bind(wx.EVT_BUTTON, self.OnButton)
        sizer.Add(b,0, wx.EXPAND | wx.ALL, 8)
        self.equal = b

        c = wx.StaticText(self, label="respuesta")
        sizer.Add(c, 1, wx.EXPAND | wx.ALL)
        self.equal = c
        

        # Set sizer and center
        self.SetSizerAndFit(sizer)


    def OnButton(self, evt):
        '''Handle button click event'''

        # Get title of clicked button
        label = evt.GetEventObject().GetLabel()

        if label == "Escribir numero":  # Evento
            self.Evento()
        elif label == "C":  # Clear
            self.display.SetValue("")

        else:  # Just add button text to current calculation
            self.display.SetValue(self.display.GetValue() + label)
            self.display.SetInsertionPointEnd()
            self.equal.SetFocus()  # Set the [escribir numero] button in focus

    def Evento(self):
        try:
            compute = self.display.GetValue()
            # Ignore empty calculation
            if not compute.strip():
                return
            v = int(self.display.GetValue())
            a = numero_a_letra(v)

            result = numero_a_letra(compute)
            r = self.equal.SetLabel(str(" El Numero: '")+str(v)+str(" se escribe: '")+result+str(" '")) 
            #si el resultado no entra en pantalla no se como hacer para que baje de linea. Se puede abrir la ventana y ahi si baja 
            # Show result
            return r
            

        except Exception as e:
            wx.LogError(str(e))
            return



class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('title', "Lee Numeros by Clara")
        wx.Frame.__init__(self, *args, **kwargs)

        self.calcPanel = LeeNumeros(self)

        # put the panel on -- in a sizer to give it some space
        S = wx.BoxSizer(wx.VERTICAL)
        S.Add(self.calcPanel, 1, wx.GROW | wx.ALL, 10)
        self.SetSizerAndFit(S)
        self.CenterOnScreen()


if __name__ == "__main__":
    # Run the application
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()
