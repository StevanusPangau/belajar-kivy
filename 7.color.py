import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('kivy/color.kv')


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


class TestingApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    TestingApp().run()
