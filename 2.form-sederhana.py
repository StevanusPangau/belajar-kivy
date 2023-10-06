import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call Grid Layout Constructor
        super().__init__(**kwargs)

        # Set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="First Name: "))
        # Add text input, multiline is false because we want single line
        self.firstName = TextInput(multiline=False)
        self.add_widget(self.firstName)

        self.add_widget(Label(text="Middle Name: "))
        self.middleName = TextInput(multiline=False)
        self.add_widget(self.middleName)

        self.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.add_widget(self.lastName)

        # Create a submit button
        self.submit = Button(text="Submit", font_size=32)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        firstName = self.firstName.text
        middleName = self.middleName.text
        lastName = self.lastName.text

        print(f"Hello my name is {firstName} {middleName} {lastName}")

        # Print it to the screen
        self.add_widget(
            Label(text=f"Hello my name is {firstName} {middleName} {lastName}"))

        # Clear the input boxes
        self.firstName.text = ""
        self.middleName.text = ""
        self.lastName.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
