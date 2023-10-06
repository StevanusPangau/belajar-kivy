import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    firstName = ObjectProperty(None)
    middleName = ObjectProperty(None)
    lastName = ObjectProperty(None)

    def press(self):
        firstName = self.firstName.text
        middleName = self.middleName.text
        lastName = self.lastName.text

        print(f"Hello my name is {firstName} {middleName} {lastName}")

        # self.add_widget(
        #     Label(text=f"Hello my name is {firstName} {middleName} {lastName}"))
        self.firstName.text = ""
        self.middleName.text = ""
        self.lastName.text = ""

# untuk memangil file .kv kita harus samakan nama file .kv dengan nama class kecuali jika ada kata App maka kita tuliskan hanya my.kv
# atau jika mengguakan nama Elder, berarti file .kv nya harus elder.kv


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
