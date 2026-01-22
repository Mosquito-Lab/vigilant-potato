from PySide6.QtWidgets import (QWidget, QGridLayout, QLabel, QRadioButton, QPushButton, QGroupBox, QHBoxLayout,
                               QVBoxLayout, QLineEdit)
from PySide6.QtGui import QPixmap

from Delta_Team.Images.image_finder import get_image


# Default options
class StartupWidget(QWidget):
    def __init__(self):
        super().__init__()

        animee_label = QLabel()
        animee_label.setPixmap(QPixmap(get_image('animee.png')))

        anime_button = QPushButton("Anime")
        animation_button = QPushButton("Animation")

        # Layout configs
        widget_layout = QGridLayout()
        widget_layout.addWidget(animee_label, 1, 1)
        widget_layout.addWidget(anime_button, 2, 0)
        widget_layout.addWidget(animation_button, 2, 2)

        self.setLayout(widget_layout)


# Handles more detailed options
class OptionsWidget(QWidget):
    def __init__(self):
        super().__init__()

        # FOLDER NAME
        folder_name = QGroupBox("Do you want the default folder name? (The name as shown on the site)")
        yes = QRadioButton("Yes")
        no = QRadioButton("No")

        folder_name_layout = QVBoxLayout()
        folder_name_layout.addWidget(yes)
        folder_name_layout.addWidget(no)
        folder_name.setLayout(folder_name_layout)

        # QUALITY OPTIONS
        quality = QGroupBox()
        q1 = QRadioButton("1080p")
        q2 = QRadioButton("720p")
        q2.setChecked(True)
        q3 = QRadioButton("480p")
        q4 = QRadioButton("360p")

        quality_layout = QVBoxLayout()
        quality_layout.addWidget(q1)
        quality_layout.addWidget(q2)
        quality_layout.addWidget(q3)
        quality_layout.addWidget(q4)
        quality.setLayout(quality_layout)

        # LANGUAGE OPTIONS
        language = QGroupBox()
        dubbed = QRadioButton("Dubbed")
        subbed = QRadioButton("Subbed")
        subbed.setChecked(True)
        chinese = QRadioButton("Chinese")

        language_layout = QVBoxLayout()
        language_layout.addWidget(dubbed)
        language_layout.addWidget(subbed)
        language_layout.addWidget(chinese)
        language.setLayout(language_layout)

        # EPISODES OPTIONS
        episodes = QGroupBox()
        download_all = QRadioButton("Download All")
        range_selector = QRadioButton("Download Range")

        episodes_layout = QVBoxLayout()
        episodes_layout.addWidget(download_all)
        episodes_layout.addWidget(range_selector)
        episodes.setLayout(episodes_layout)

        # MAIN LAYOUT
        widget_layout = QGridLayout()
        widget_layout.addWidget(language, 0,1)
        widget_layout.addWidget(episodes, 1,0)
        widget_layout.addWidget(quality,1,2)
        widget_layout.addWidget(folder_name, 2,1)
        self.setLayout(widget_layout)


# Widget for searching a name
class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()

        # SEARCH QUERY
        name_label = QLabel("Name: ")
        edit_name = QLineEdit()
        edit_name.setPlaceholderText("Enter name to search")
        search_query_layout = QHBoxLayout()
        search_query_layout.addWidget(name_label)
        search_query_layout.addWidget(edit_name)

        # EXACT NAME OPTIONS
        exact_name = QGroupBox("Is the name exact? Season and all? Word for word? Bar for bar?")
        yes = QRadioButton("Yes")
        no = QRadioButton("No")

        exact_name_layout = QHBoxLayout()
        exact_name_layout.addWidget(yes)
        exact_name_layout.addWidget(no)

        # HANDLER OPTIONS
        handler = QGroupBox()
        handler_s = QRadioButton("Simple")
        handler_s.setChecked(True)
        handler_x = QRadioButton("Complex")
        handler_c = QRadioButton("Choice")

        handler_layout = QHBoxLayout()
        handler_layout.addWidget(handler_s)
        handler_layout.addWidget(handler_x)
        handler_layout.addWidget(handler_c)
        handler.setLayout(handler_layout)

        # OPTIONS LAYOUT
        options_layout = QHBoxLayout()
        options_layout.addWidget(exact_name)
        options_layout.addWidget(handler)

        search_button = QPushButton("Search")

        # MAIN LAYOUT
        widget_layout = QVBoxLayout()
        widget_layout.addWidget(name_label)
        widget_layout.addWidget(edit_name)
        widget_layout.addLayout(options_layout)
        widget_layout.addWidget(search_button)
        self.setLayout(widget_layout)

