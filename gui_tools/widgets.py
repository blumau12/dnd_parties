from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton


class CompanyWorld(QWidget):
    DATETIME_TEXT_TEMPLATE = '{d} day of {m}, {y}\n({nd} day of a journey)'

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)

        self.company_name = QLabel('no company set')
        self.change_session = QPushButton('Change')
        self.stop_session = QPushButton('Stop session')
        self.datetime_text = QLabel(' \n ')
        self.datetime = QLabel('  :  ')
        self.add_1_min = QPushButton('1 min')
        self.add_10_min = QPushButton('10 min')
        self.add_1_hour = QPushButton('1 hour')
        self.add_8_hours = QPushButton('8 hours')
        self.add_1_day = QPushButton('1 day')
        self.add_custom = QPushButton('custom')

        self.init_gui()

    def init_gui(self):
        v_box = QVBoxLayout()

        h_box_company = QHBoxLayout()
        h_box_company.addWidget(self.company_name, stretch=4)
        h_box_company.addWidget(self.change_session, stretch=1)
        h_box_company.addWidget(self.stop_session, stretch=1)
        v_box.addLayout(h_box_company, stretch=0)

        h_box_clock = QHBoxLayout()
        self.datetime_text.setAlignment(Qt.AlignCenter)
        h_box_clock.addWidget(self.datetime_text, stretch=2)
        self.datetime.setAlignment(Qt.AlignCenter)
        h_box_clock.addWidget(self.datetime, stretch=1)
        v_box.addLayout(h_box_clock, stretch=1)

        h_box_add_time = QHBoxLayout()
        add = QLabel('add')
        add.setAlignment(Qt.AlignCenter)
        h_box_add_time.addWidget(add)
        h_box_add_time.addWidget(self.add_1_min)
        h_box_add_time.addWidget(self.add_10_min)
        h_box_add_time.addWidget(self.add_1_hour)
        h_box_add_time.addWidget(self.add_8_hours)
        h_box_add_time.addWidget(self.add_1_day)
        h_box_add_time.addWidget(self.add_custom)
        v_box.addLayout(h_box_add_time, stretch=0)

        self.setLayout(v_box)


class Characters(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.characters = []
        self.init_gui()

    def init_gui(self):
        h_box = QHBoxLayout()

        for character in self.parent().data.characters:
            char_w = Character(self, character)
            self.characters.append(char_w)
            h_box.addWidget(char_w)

        self.setLayout(h_box)


class Character(QWidget):
    def __init__(self, parent, character):
        QWidget.__init__(self, parent=parent)
        self.character = character

        self.head = CharacterHead(self)
        self.info_buttons = CharacterInfoButtons(self)
        self.var_stats = CharacterVarStats(self)
        self.active_states = CharacterActiveStates(self)
        self.inventory = CharacterInventory(self)

        self.init_ui()

    def init_ui(self):
        v_box = QVBoxLayout()

        v_box.addWidget(self.head)
        v_box.addWidget(self.info_buttons)
        v_box.addWidget(self.var_stats)
        v_box.addWidget(self.active_states)
        v_box.addWidget(self.inventory)

        self.setLayout(v_box)


class CharacterHead(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def init_ui(self):
        h_box = QHBoxLayout()

        v_box = QVBoxLayout()
        char_name_lvl = QLabel('Char Name, LVL')
        v_box.addWidget(char_name_lvl)
        char_race_classes = QLabel('race, classes')
        v_box.addWidget(char_race_classes)
        h_box.addLayout(v_box)

        v_box = QVBoxLayout()
        eye_pic = QLabel('eye pic')
        v_box.addWidget(eye_pic)
        vis_type = QLabel('NIGHTVIS')
        v_box.addWidget(vis_type)
        pass_perception = QLabel('PP')
        v_box.addWidget(pass_perception)
        h_box.addLayout(v_box)

        self.setLayout(h_box)


class CharacterInfoButtons(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def init_ui(self):
        h_box = QHBoxLayout()

        pers_info = QPushButton('Personal info')
        h_box.addWidget(pers_info)
        char_stats = QPushButton('Character stats')
        h_box.addWidget(char_stats)
        situational_stats = QPushButton('Situational stats')
        h_box.addWidget(situational_stats)

        self.setLayout(h_box)


class CharacterVarStats(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        hp = QLabel('HP:')
        grid.addWidget(hp, 0, 0)
        temp_hp = QLabel('Temp. HP:')
        grid.addWidget(temp_hp, 0, 1)
        hit_dices = QLabel('Hit dices:')
        grid.addWidget(hit_dices, 0, 2)
        inspiration = QLabel('Inspiration:')
        grid.addWidget(inspiration, 0, 3)

        hp_w = CharacterVarStatHP(self)
        grid.addWidget(hp_w, 1, 0)
        temp_hp = CharacterVarStatTempHP(self)
        grid.addWidget(temp_hp, 1, 1)
        hit_dices = CharacterVarStatHitDices(self)
        grid.addWidget(hit_dices, 1, 2)
        inspiration = CharacterVarStatInspiration(self)
        grid.addWidget(inspiration, 1, 3)

        self.setLayout(grid)


class CharacterVarStatHP(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def init_ui(self):
        pass


class CharacterVarStatTempHP(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def init_ui(self):
        pass


class CharacterVarStatHitDices(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def init_ui(self):
        pass


class CharacterVarStatInspiration(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def init_ui(self):
        pass


class CharacterActiveStates(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def init_ui(self):
        h_box = QHBoxLayout()
        self.setLayout(h_box)


class CharacterInventory(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.init_ui()

    def init_ui(self):
        h_box = QHBoxLayout()
        self.setLayout(h_box)
