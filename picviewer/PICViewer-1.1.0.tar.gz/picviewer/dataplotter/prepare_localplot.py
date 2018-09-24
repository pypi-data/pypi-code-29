



class PrepareLocalplot():

    def __init__(self,Mainwindow):

        self.main = Mainwindow


    def linecheckbox(self):
        """
        Local line selection checkbox
        """

        if self.main.lineCheckBox.isChecked():
            self.main.line_panel[self.main.panelselect-1]=True
            self.main.rectangleCheckBox.setChecked(False)
            self.main.rectangle_panel[self.main.panelselect-1]=False
            if self.main.panelselect-1 in self.main.rectangle1.keys():
                self.main.rectangle1[(self.main.panelselect-1)].remove()
                self.main.rectangle2[(self.main.panelselect-1)].remove()
                self.main.rectangle3[(self.main.panelselect-1)].remove()
                self.main.rectangle4[(self.main.panelselect-1)].remove()
                self.main.canvas.draw()
        else:
            self.main.line_panel[self.main.panelselect-1]=False
            if self.main.panelselect-1 in self.main.line.keys():
                self.main.line[(self.main.panelselect-1)].remove()
                self.main.canvas.draw()         

    def rectanglecheckbox(self):
        """
        Local rectangle selection checkbox
        """
        if self.main.rectangleCheckBox.isChecked():
            self.main.rectangle_panel[self.main.panelselect-1]=True
            self.main.lineCheckBox.setChecked(False)
            self.main.line_panel[self.main.panelselect-1]=False
            if self.main.panelselect-1 in self.main.line.keys():
                self.main.line[(self.main.panelselect-1)].remove()
                self.main.canvas.draw()         
        else:
            self.main.rectangle_panel[self.main.panelselect-1]=False

            if self.main.panelselect-1 in self.main.rectangle1.keys():
                self.main.rectangle1[(self.main.panelselect-1)].remove()
                self.main.rectangle2[(self.main.panelselect-1)].remove()
                self.main.rectangle3[(self.main.panelselect-1)].remove()
                self.main.rectangle4[(self.main.panelselect-1)].remove()
                self.main.canvas.draw()
