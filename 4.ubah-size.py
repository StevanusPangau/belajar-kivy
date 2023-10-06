import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 200

        # Mengatur ukuran grid, jadi tidak perlu mengatur ukuran label dan text input
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=200,
        )
        self.top_grid.cols = 2

        # >>> Contoh mengatur ukuran label dan text input
        # self.top_grid.add_widget(Label(
        #     text="First Name: ",
        #     size_hint_y=None,
        #     height=50,
        #     size_hint_x=None,
        #     width=200,
        # ))
        # self.firstName = TextInput(
        #     multiline=False,
        #     size_hint_y=None,
        #     height=50,
        #     size_hint_x=None,
        #     width=400,
        # )
        self.top_grid.add_widget(Label(
            text="First Name: ",
        ))
        self.firstName = TextInput(
            multiline=False,
        )
        self.top_grid.add_widget(self.firstName)

        self.top_grid.add_widget(Label(text="Middle Name: "))
        self.middleName = TextInput(multiline=False)
        self.top_grid.add_widget(self.middleName)

        self.top_grid.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.top_grid.add_widget(self.lastName)
        self.add_widget(self.top_grid)

        self.submit = Button(
            text="Submit",
            font_size=32,
            size_hint_y=None,  # tambahkan code berikut untuk mengubah ukuran tombol y
            height=50,
            size_hint_x=None,  # tambahkan code berikut untuk mengubah ukuran tombol x
            width=200,
        )

        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        firstName = self.firstName.text
        middleName = self.middleName.text
        lastName = self.lastName.text
        print(f"Hello my name is {firstName} {middleName} {lastName}")
        self.add_widget(
            Label(text=f"Hello my name is {firstName} {middleName} {lastName}"))
        self.firstName.text = ""
        self.middleName.text = ""
        self.lastName.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
