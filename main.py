from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


PINK = (1, 0.25, 0.55, 1)
WHITE = (1, 1, 1, 1)
DARK = (0.15, 0.15, 0.15, 1)


class PinkBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*PINK)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(25)]
            )

        self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class PasswordBox(BoxLayout):
    def __init__(self, hint, **kwargs):
        super().__init__(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(50),
            spacing=dp(5),
            **kwargs
        )

        self.password = True

        self.field = TextInput(
            hint_text=hint,
            password=True,
            multiline=False,
            background_normal="",
            background_color=(1, 1, 1, 1),
            foreground_color=DARK,
            padding=[dp(15), dp(12)]
        )

        self.eye = Button(
            text="👁",
            size_hint_x=None,
            width=dp(55),
            background_normal="",
            background_color=(1, 1, 1, 1),
            color=DARK
        )

        self.eye.bind(on_press=self.show_password)

        self.add_widget(self.field)
        self.add_widget(self.eye)

    def show_password(self, instance):
        self.password = not self.password
        self.field.password = self.password


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main = BoxLayout(
            orientation="vertical",
            padding=[dp(25), dp(40)],
            spacing=dp(15)
        )

        main.add_widget(Widget())

        title = Label(
            text="WELCOME",
            font_size=dp(30),
            bold=True,
            color=WHITE,
            size_hint_y=None,
            height=dp(50)
        )

        main.add_widget(title)

        card = PinkBox(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12),
            size_hint_y=None,
            height=dp(330)
        )

        card.add_widget(Label(
            text="LOGIN",
            font_size=dp(25),
            bold=True,
            color=WHITE,
            size_hint_y=None,
            height=dp(40)
        ))

        self.user = TextInput(
            hint_text="Gmail অথবা ফোন নাম্বার",
            multiline=False,
            size_hint_y=None,
            height=dp(50),
            background_normal="",
            background_color=WHITE,
            padding=[dp(15), dp(12)]
        )

        card.add_widget(self.user)

        self.password = PasswordBox("Password")
        card.add_widget(self.password)

        forgot = Button(
            text="Forgot Password?",
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=WHITE,
            size_hint_y=None,
            height=dp(35)
        )

        forgot.bind(on_press=self.forgot_password)
        card.add_widget(forgot)

        login = Button(
            text="LOGIN",
            background_normal="",
            background_color=WHITE,
            color=PINK,
            bold=True,
            size_hint_y=None,
            height=dp(50)
        )

        login.bind(on_press=self.login)
        card.add_widget(login)

        register = Button(
            text="নতুন Account? Registration করুন",
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=WHITE,
            size_hint_y=None,
            height=dp(40)
        )

        register.bind(
            on_press=lambda x:
            setattr(self.manager, "current", "register")
        )

        card.add_widget(register)

        main.add_widget(card)
        main.add_widget(Widget())

        self.add_widget(main)

    def login(self, instance):
        print("Login button pressed")
        print("User:", self.user.text)
        print("Password:", self.password.field.text)

    def forgot_password(self, instance):
        print("Forgot Password clicked")


class RegisterScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main = BoxLayout(
            orientation="vertical",
            padding=[dp(25), dp(30)],
            spacing=dp(12)
        )

        main.add_widget(Widget())

        card = PinkBox(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12),
            size_hint_y=None,
            height=dp(390)
        )

        card.add_widget(Label(
            text="REGISTRATION",
            font_size=dp(24),
            bold=True,
            color=WHITE,
            size_hint_y=None,
            height=dp(45)
        ))

        self.user = TextInput(
            hint_text="Gmail অথবা ফোন নাম্বার",
            multiline=False,
            size_hint_y=None,
            height=dp(50),
            background_normal="",
            background_color=WHITE,
            padding=[dp(15), dp(12)]
        )

        card.add_widget(self.user)

        self.password = PasswordBox("Password")
        card.add_widget(self.password)

        self.confirm = PasswordBox("Confirm Password")
        card.add_widget(self.confirm)

        submit = Button(
            text="SUBMIT",
            background_normal="",
            background_color=WHITE,
            color=PINK,
            bold=True,
            size_hint_y=None,
            height=dp(50)
        )

        submit.bind(on_press=self.register)
        card.add_widget(submit)

        back = Button(
            text="আগে Account আছে? Login",
            background_normal="",
            background_color=(0, 0, 0, 0),
            color=WHITE,
            size_hint_y=None,
            height=dp(40)
        )

        back.bind(
            on_press=lambda x:
            setattr(self.manager, "current", "login")
        )

        card.add_widget(back)

        main.add_widget(card)
        main.add_widget(Widget())

        self.add_widget(main)

    def register(self, instance):

        user = self.user.text.strip()
        password = self.password.field.text
        confirm = self.confirm.field.text

        if not user:
            print("Gmail অথবা ফোন নাম্বার দিন")
            return

        if not password:
            print("Password দিন")
            return

        if password != confirm:
            print("Password এবং Confirm Password একই নয়")
            return

        if len(password) < 6:
            print("Password কমপক্ষে 6 অক্ষরের হতে হবে")
            return

        print("Registration information:")
        print("User:", user)
        print("Password:", password)

        # Firebase এখানে যুক্ত করা হবে

        self.manager.current = "login"


class MyApp(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(
            LoginScreen(name="login")
        )

        manager.add_widget(
            RegisterScreen(name="register")
        )

        return manager


if __name__ == "__main__":
    MyApp().run()