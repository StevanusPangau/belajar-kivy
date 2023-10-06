import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Cara satu
Builder.load_file('kivy/whatever.kv')

# Cara dua
'''
Builder.load_string("""
<MyGridLayout>

    firstName: FirstName
    middleName: MiddleName
    lastName: LastName

    GridLayout:
        cols: 1
        size: root.width, root.height

        GridLayout:
            cols: 2

            # Label akan masuk di kolom1
            # TextInput akan masuk di kolom2
            Label:
                text: "FirstName"
            TextInput:
                id: FirstName
                multiline: False
                
            Label:
                id: MiddleName
                text: "MiddleName"
            TextInput:
                multiline: False
                
            Label:
                id: LastName
                text: "LastName"
            TextInput:
                multiline: False
    
        Button:
            text: "Submit"
            font_size: 32
            on_press: root.press()
    """)
'''


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


class TestingApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    TestingApp().run()
