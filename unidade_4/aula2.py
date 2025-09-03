from kivy.lang import Builder 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton 
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp

kv_string = """    
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    MDTextField:
        id: input_field
        hint_text: "Digite a expressão"
        font_size: 32
        halign: "right"
        size_hint_y: None
        height: 80
        multiline: False

    GridLayout:
        cols: 4
        spacing: 10
        size_hint_y: None
        height: 400

        MDRaisedButton:
            text: "7"
            on_release: app.on_number_press("7")
        MDRaisedButton:
            text: "8"
            on_release: app.on_number_press("8")
        MDRaisedButton:
            text: "9"
            on_release: app.on_number_press("9")
        MDRaisedButton:
            text: "/"
            on_release: app.on_number_press("/")

        MDRaisedButton:
            text: "4"
            on_release: app.on_number_press("4")
        MDRaisedButton:
            text: "5"
            on_release: app.on_number_press("5")
        MDRaisedButton:
            text: "6"
            on_release: app.on_number_press("6")
        MDRaisedButton:
            text: "*"
            on_release: app.on_number_press("*")

        MDRaisedButton:
            text: "1"
            on_release: app.on_number_press("1")
        MDRaisedButton:
            text: "2"
            on_release: app.on_number_press("2")
        MDRaisedButton:
            text: "3"
            on_release: app.on_number_press("3")
        MDRaisedButton:
            text: "-"
            on_release: app.on_number_press("-")

        MDRaisedButton:
            text: "0"
            on_release: app.on_number_press("0")
        MDRaisedButton:
            text: "."
            on_release: app.on_number_press(".")
        MDRaisedButton:
            text: "="
            on_release: app.calculate()
        MDRaisedButton:
            text: "+"
            on_release: app.on_number_press("+")
    
    MDRaisedButton:
        text: "C"
        on_release: app.clear()
        size_hint_y: None
        height: 60

"""
class CalculadoresApp(BoxLayout):

    def on_number_press(self,number):
        curret_text = self.ids.input_field.text
        new_text = f"{curret_text}{number}"
        self.ids.input_field.text = new_text

    def on_operator_press(self,operator):

        curret_text = self.ids.input_field.text
        new_text = f"{curret_text}{operator}"
        self.ids.input_field.text = new_text

    def clear_input(self):
        self.ids.input_field.text = ""

    def calculat_result(self):
        try:
            result = eval(self.ids.input_field.text)
            self.ids.input_field = str(result)
        except Exception as e:
            self.ids.input_field.text = "Erro"
class CalculatorMDApp (MDApp):
    def build(self):
        return CalculatorMDApp()
    
    def on_number_press(self,number):
        self.root.on_number_press(number)
    def on_operator_press(self, operator):
        self.root.on_operator_press(operator)
    def clear_input(self):
        self.root.clear_input()
    def calculate_result(self):
        self.root.calculate_result()

if __name__ == "__main__":
    Builder.load_string(kv_string)
    CalculatorMDApp().run()