from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar


class UserProfileApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        # Главный layout
        main_layout = MDBoxLayout(orientation="vertical", spacing="10dp", padding="20dp")

        # Карточка профиля
        profile_card = MDCard(
            orientation="vertical",
            padding="20dp",
            size_hint=(1, None),
            height="500dp",
            elevation=3,
            radius=[15, 15, 15, 15]
        )

        # Заголовок с аватаром
        header = MDBoxLayout(orientation="vertical", size_hint_y=None, height="120dp")
        header.md_bg_color = self.theme_cls.primary_color

        avatar_label = MDLabel(
            text="GC",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H4",
            bold=True
        )
        header.add_widget(avatar_label)
        profile_card.add_widget(header)

        # Имя пользователя
        name_label = MDLabel(
            text="Georgii Chetverikov",
            halign="center",
            font_style="H5",
            bold=True,
            size_hint_y=None,
            height="40dp"
        )
        profile_card.add_widget(name_label)

        # Секции
        self.add_section(profile_card, "Biography", "I'm a Student in MAI")
        self.add_section(profile_card, "Skills", "Python | PHP | SQL | JavaScript")

        # Опыт работы
        exp_label = MDLabel(
            text="Experience",
            font_style="H6",
            bold=True,
            size_hint_y=None,
            height="30dp"
        )
        profile_card.add_widget(exp_label)

        self.add_experience_item(profile_card, "Python Developer", "Mar 2021 - Present")
        self.add_experience_item(profile_card, "Teacher in 5-9 classes", "Aug 2025 - ...")
        self.add_experience_item(profile_card, "Builder", "10.12.2024 - 15.12.2024")

        main_layout.add_widget(profile_card)
        return main_layout

    def add_section(self, parent, title, content):
        title_label = MDLabel(
            text=title,
            font_style="H6",
            bold=True,
            size_hint_y=None,
            height="30dp"
        )
        parent.add_widget(title_label)

        content_label = MDLabel(
            text=content,
            theme_text_color="Secondary",
            size_hint_y=None,
            height="30dp"
        )
        parent.add_widget(content_label)

    def add_experience_item(self, parent, position, dates):
        item_layout = MDBoxLayout(orientation="vertical", size_hint_y=None, height="50dp")

        position_label = MDLabel(
            text=position,
            bold=True,
            size_hint_y=None,
            height="25dp"
        )

        dates_label = MDLabel(
            text=dates,
            theme_text_color="Secondary",
            font_style="Caption",
            size_hint_y=None,
            height="20dp"
        )

        item_layout.add_widget(position_label)
        item_layout.add_widget(dates_label)
        parent.add_widget(item_layout)


if __name__ == '__main__':
    UserProfileApp().run()