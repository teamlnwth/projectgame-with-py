import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.vector import Vector
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from math import atan2, degrees, cos, sin
import random
from kivy.uix.floatlayout import FloatLayout

# คลาสตัวละคร
class Character(Widget):
    def __init__(self, source, max_health, **kwargs):
        super().__init__(**kwargs)
        self.max_health = max_health
        self.current_health = max_health
        with self.canvas:
            # แถบเลือดสีแดง (เต็ม)
            self.health_bar_full = Rectangle(pos=(self.x, self.top + 5), size=(self.width, 5), source='blood\green.png')
            # แถบเลือดสีเขียว (ลดลงตามเลือดที่เหลือ)
            self.health_bar_current = Rectangle(pos=(self.x, self.top + 5), size=(self.width, 5), source='blood\green.png')
            self.rect = Rectangle(pos=self.pos, size=(100, 200), source=source)
        self.bind(pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = value
        self.update_health_bar()

    def update_health_bar(self):
        # คำนวณขนาดและตำแหน่งของแถบเลือด
        self.health_bar_full.pos = (self.x, self.y - 80)
        self.health_bar_full.size = (self.width, 120)
class Princess(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.princess_image = Rectangle(source='princess\princess.png', pos=self.center, size=(132, 115))
        self.bind(pos=self.update_rect)

    def update_rect(self, instance, value):
        self.princess_image.pos = value

# คลาสมอนสเตอร์
class Monster(Widget):
    def __init__(self, source, max_health, **kwargs):
        super().__init__(**kwargs)
        self.max_health = max_health
        self.current_health = max_health
        with self.canvas:
            self.health_bar_full = Rectangle(pos=(self.right - self.width, self.top + 5), size=(self.width, 5), source='blood/monster1.png')
            self.rect = Rectangle(pos=self.pos, size=(150, 150), source=source)
            self.health_label = Label(text="HP: {}/{}".format(self.max_health, self.current_health), pos=(self.right - self.width, self.top + 15), size=(self.width, 20))
        self.bind(pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = value
        self.health_label.pos = (self.right - self.width, self.y - 80)
        self.health_bar_full.pos = (self.right - self.width, self.y - 80)
        self.update_health_bar()

    def update_health_bar(self):
        health_ratio = self.current_health / self.max_health
        self.health_bar_full.size = (self.width * health_ratio, 5)
        self.health_label.text = "HP: {}/{}".format(self.current_health, self.max_health)

    def move_monster_towards_player(self, player_pos, speed=20):
        monster_pos = self.pos
        dx = player_pos[0] - monster_pos[0]
        dy = player_pos[1] - monster_pos[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance < 50:
            return
        angle = atan2(dy, dx)
        new_pos = (monster_pos[0] + speed * cos(angle),
                   monster_pos[1] + speed * sin(angle))
        self.pos = new_pos
        self.update_health_bar()

class Monster2(Widget):
    def __init__(self, source, max_health, **kwargs):
        super().__init__(**kwargs)
        self.max_health = max_health
        self.current_health = max_health
        with self.canvas:
            self.health_bar_full = Rectangle(pos=(self.right - self.width, self.top + 5), size=(self.width, 5), source='blood/monster1.png')
            self.rect = Rectangle(pos=self.pos, size=(150, 200), source=source)
            self.health_label = Label(text="HP: {}/{}".format(self.max_health, self.current_health), pos=(self.right - self.width, self.top + 15), size=(self.width, 20))
        self.bind(pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = value
        self.health_label.pos = (self.right - self.width, self.y - 80)
        self.health_bar_full.pos = (self.right - self.width, self.y - 80)
        self.update_health_bar()

    def update_health_bar(self):
        health_ratio = self.current_health / self.max_health
        self.health_bar_full.size = (self.width * health_ratio, 5)
        self.health_label.text = "HP: {}/{}".format(self.current_health, self.max_health)

    def move_monster_towards_player(self, player_pos, speed=20):
        monster_pos = self.pos
        dx = player_pos[0] - monster_pos[0]
        dy = player_pos[1] - monster_pos[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance < 50:
            return
        angle = atan2(dy, dx)
        new_pos = (monster_pos[0] + speed * cos(angle),
                   monster_pos[1] + speed * sin(angle))
        self.pos = new_pos
        self.update_health_bar()


class Monster3(Widget):
    def __init__(self, source, max_health, **kwargs):
        super().__init__(**kwargs)
        self.max_health = max_health
        self.current_health = max_health
        with self.canvas:
            self.health_bar_full = Rectangle(pos=(self.right - self.width, self.top + 5), size=(self.width, 5), source='blood/monster1.png')
            self.rect = Rectangle(pos=self.pos, size=(150, 200), source=source)
            self.health_label = Label(text="HP: {}/{}".format(self.max_health, self.current_health), pos=(self.right - self.width, self.top + 15), size=(self.width, 20))
        self.bind(pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = value
        self.health_label.pos = (self.right - self.width, self.y - 80)
        self.health_bar_full.pos = (self.right - self.width, self.y - 80)
        self.update_health_bar()

    def update_health_bar(self):
        health_ratio = self.current_health / self.max_health
        self.health_bar_full.size = (self.width * health_ratio, 5)
        self.health_label.text = "HP: {}/{}".format(self.current_health, self.max_health)

    def move_monster_towards_player(self, player_pos, speed=20):
        monster_pos = self.pos
        dx = player_pos[0] - monster_pos[0]
        dy = player_pos[1] - monster_pos[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance < 50:
            return
        angle = atan2(dy, dx)
        new_pos = (monster_pos[0] + speed * cos(angle),
                   monster_pos[1] + speed * sin(angle))
        self.pos = new_pos
        self.update_health_bar()

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.killed_monsters = 0
        self.monsters = []  # รายการมอนสเตอร์ทั้งหมด
        self.idle_images = ['Character/Player/Idle/__Idle-00{}.png'.format(str(i).zfill(2)) for i in range(10)]
        self.run_images = ['Character/Player/Run/__Run-00{}.png'.format(str(i).zfill(2)) for i in range(10)]
        self.attack_images = ['Character/Player/Attack/__Attack-00{}.png'.format(str(i).zfill(2)) for i in range(6)]
        self.player = Character(source=self.idle_images[0], max_health=100)  # แก้ไขตรงนี้เป็น player

        # โหลดรูปภาพพื้นหลัง
        self.background = Image(source="back\menu_background.jpg.jpg", allow_stretch=True, keep_ratio=False)
        self.background.size = self.size
        self.add_widget(self.background)

        self.player = Character(source=self.idle_images[0], max_health=100)  
# ให้ตัวละครเริ่มต้นที่ตรงกลางของหน้าจอ
        self.player.pos = (self.width / 2 - self.player.width / 2, self.height / 2 - self.player.height / 2)

        self.add_widget(self.player)  # แก้ไขตรงนี้เป็น player

        with self.canvas.before:
            self.background_rect = Rectangle(pos=self.pos, size=self.size, source="back\menu_background.jpg.jpg")

        self.bind(size=self.on_size)

        self.countdown_label = Label(text="", font_size=20, pos_hint={'center_x': 0.5, 'top': 0.95})
        self.add_widget(self.countdown_label)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        self.pressed_keys = set()
        self.image_index = 0
        self.is_running = False
        self.is_attacking = False
        self.idle_update_speed = 1/10
        self.run_update_speed = 1/20
        self.attack_update_speed = 1/15
        Clock.schedule_interval(self.update_image, self.idle_update_speed)
        Clock.schedule_interval(self.move_step, 1/60)
        
        self.background_music = SoundLoader.load('song/songingame.mp3')
        self.background_music.loop = True
        self.background_music.play()

        # เรียกใช้เมทอด spawn_monster() เพื่อให้มอนสเตอร์เกิดขึ้นทุก 10 วินาที
        Clock.schedule_interval(self.spawn_monster, 10)

        self.princess = None
        self.victory_label = None

    def spawn_monster(self, dt):
        if not self.monsters:  # ถ้ายังไม่มีมอนสเตอร์
            # สร้างมอนสเตอร์แบบที่หนึ่ง
            monster = Monster(source='monter\monter_1.png', max_health=500)
            monster_x = random.randint(0, self.width - monster.width)
            monster_y = random.randint(0, self.height - monster.height)
            monster.pos = (monster_x, monster_y)
            self.add_widget(monster)
            self.monsters.append(monster)  # เพิ่มมอนสเตอร์ลงในรายการ

        elif len(self.monsters) == 1 and self.monsters[0] not in self.children:  # ถ้ามอนสเตอร์ตัวแรกตายแล้ว
            Clock.schedule_once(self.spawn_second_monster, 5)  # เรียกฟังก์ชัน spawn_second_monster() ในอีก 5 วินาที

    def spawn_next_monster(self, dt):
        if self.killed_monsters == 1:
        # สร้างมอนสเตอร์แบบที่สอง
            monster2 = Monster2(source='monter\monter_2.png', max_health=1000)
            monster2_x = random.randint(0, self.width - monster2.width)
            monster2_y = random.randint(0, self.height - monster2.height)
            monster2.pos = (monster2_x, monster2_y)
            self.add_widget(monster2)
            self.monsters.append(monster2)  # เพิ่มมอนสเตอร์ลงในรายการ

        elif self.killed_monsters == 2:
        # สร้างมอนสเตอร์แบบที่สาม
            monster3 = Monster3(source='monter\monter_3.png', max_health=1500)
            monster3_x = random.randint(0, self.width - monster3.width)
            monster3_y = random.randint(0, self.height - monster3.height)
            monster3.pos = (monster3_x, monster3_y)
            self.add_widget(monster3)
            self.monsters.append(monster3)  # เพิ่มมอนสเตอร์ลงในรายการ

        elif self.killed_monsters == 3:  # เมื่อฆ่ามอนสเตอร์ตัวสุดท้ายแล้ว
            self.princess = Princess(center=self.center)
            self.add_widget(self.princess)
            self.victory_label = Label(text="<3", font_size=30, center=self.center)
            self.add_widget(self.victory_label)
            self.killed_monsters = 0  # รีเซ็ตจำนวนมอนสเตอร์ที่ถูกฆ่า

        self.countdown_time = 5
        Clock.schedule_interval(self.update_countdown, 1)


    def spawn_second_monster(self, dt):
        if len(self.monsters) == 1 and self.monsters[0] not in self.children:  # ตรวจสอบให้แน่ใจว่ามอนสเตอร์ตัวแรกยังไม่มีในรายการ children แล้ว
            # สร้างมอนสเตอร์แบบที่สอง
            monster2 = Monster(source='monter\monter_2.png', max_health=1000)
            monster2_x = random.randint(0, self.width - monster2.width)
            monster2_y = random.randint(0, self.height - monster2.height)
            monster2.pos = (monster2_x, monster2_y)
            self.add_widget(monster2)
            self.monsters.append(monster2)  # เพิ่มมอนสเตอร์ลงในรายการ

        elif len(self.monsters) == 2 and self.monsters[1] not in self.children:  # ถ้ามอนสเตอร์ตัวที่สองตายแล้ว
            Clock.schedule_once(self.spawn_third_monster, 5)  # เรียกฟังก์ชัน spawn_third_monster() ในอีก 5 วินาที

    def spawn_third_monster(self, dt):
        if len(self.monsters) == 2 and self.monsters[1] not in self.children:  # ตรวจสอบให้แน่ใจว่ามอนสเตอร์ตัวที่สองยังไม่มีในรายการ children แล้ว
            # สร้างมอนสเตอร์แบบที่สาม
            monster3 = Monster(source='monter\monter_3.png', max_health=1500)
            monster3_x = random.randint(0, self.width - monster3.width)
            monster3_y = random.randint(0, self.height - monster3.height)
            monster3.pos = (monster3_x, monster3_y)
            self.add_widget(monster3)
            self.monsters.append(monster3)  # เพิ่มมอนสเตอร์ลงในรายการ

    def update_countdown(self, dt):
        self.countdown_time -= 1
        self.countdown_label.text = f""
        if self.countdown_time <= 0:
            Clock.unschedule(self.update_countdown)
            self.countdown_label.text = ""
            if self.killed_monsters == 1:
                Clock.schedule_once(self.spawn_next_monster, 5)
            elif self.killed_monsters == 2:
                Clock.schedule_once(self.spawn_next_monster, 5)

    def on_size(self, *args):
        self.background.size = self.size
        self.background_rect.size = self.size
        self.player.pos = (self.width / 2 - self.player.width / 2, self.height / 2 - self.player.height / 2)
    

    def update_image(self, dt):
        if self.is_running:
            self.player.rect.source = self.run_images[self.image_index]
            update_speed = self.run_update_speed
        else:
            self.player.rect.source = self.idle_images[self.image_index]
            update_speed = self.idle_update_speed

        self.image_index += 1
        if self.image_index >= 10:
            self.image_index = 0

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(text)
        self.is_running = True

        if text == 'j' and not self.is_attacking:
            self.is_attacking = True
            self.image_index = 0
            Clock.unschedule(self.update_image)
            Clock.schedule_interval(self.update_attack_image, self.attack_update_speed)
            Clock.unschedule(self.move_step)
            self.is_running = False

        if 'a' in self.pressed_keys:
            self.idle_images = ['Character/Player/Idle/__Idle-left-00{}.png'.format(str(i).zfill(2)) for i in range(10)]
            self.run_images = ['Character/Player/Run/__Run-left-00{}.png'.format(str(i).zfill(2)) for i in range(10)]
            self.attack_images = ['Character/Player/Attack/__Attack-left-00{}.png'.format(str(i).zfill(2)) for i in range(6)]
        elif 'd' in self.pressed_keys:
            self.idle_images = ['Character/Player/Idle/__Idle-00{}.png'.format(str(i).zfill(2)) for i in range(10)]
            self.run_images = ['Character/Player/Run/__Run-00{}.png'.format(str(i).zfill(2)) for i in range(10)]
            self.attack_images = ['Character/Player/Attack/__Attack-00{}.png'.format(str(i).zfill(2)) for i in range(6)]

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]

        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

        if len(self.pressed_keys) == 0:
            self.is_running = False

    def update_attack_image(self, dt):
        if self.is_attacking:
            self.player.rect.source = self.attack_images[self.image_index]
            self.image_index += 1
            if self.image_index >= len(self.attack_images):
                self.is_attacking = False
                self.image_index = 0
                Clock.unschedule(self.update_attack_image)
                Clock.schedule_interval(self.update_image, self.idle_update_speed)
                Clock.schedule_interval(self.move_step, 1/60)

            # เมื่อการโจมตีเสร็จสิ้น และมีการชนกับมอนเตอร์ให้ลดเลือดของมอนเตอร์
            for monster in self.monsters:
                if self.player.collide_widget(monster):
                    self.on_attacked(monster)

    def move_step(self, dt):
        cur_x, cur_y = self.player.pos

        # ถ้ามีปุ่มถูกกดอยู่ให้เคลื่อนที่ตามปุ่ม
        if self.pressed_keys:
            moved = False
            step = 100 * dt

            if 'w' in self.pressed_keys:
                cur_y += step
                moved = True
            if 's' in self.pressed_keys:
                cur_y -= step
                moved = True
            if 'a' in self.pressed_keys:
                cur_x -= step
                moved = True
            if 'd' in self.pressed_keys:
                cur_x += step
                moved = True

            # ตรวจสอบว่าตำแหน่งใหม่หลังจากการเคลื่อนที่อยู่ในขอบเขตของหน้าจอหรือไม่
            if 0 <= cur_x <= self.width - self.player.width and 0 <= cur_y <= self.height - self.player.height:
                self.player.pos = (cur_x, cur_y)
                self.is_running = True
            else:
                self.is_running = False
        else:
            # ไม่มีปุ่มถูกกด ไม่ต้องเคลื่อนที่
            self.is_running = False

        # เคลื่อนที่มอนสเตอร์ไปหาตัวละคร
        player_pos = self.player.pos
        for monster in self.monsters:
            monster.move_monster_towards_player(player_pos, speed=2)

            # ตรวจสอบการชนของมอนสเตอร์
            if self.player.collide_widget(monster):
                self.on_attacked(monster)

    def on_attacked(self, monster):
        if self.is_attacking:
            monster.current_health -= 50
            if monster.current_health <= 0:
                self.remove_widget(monster)
                self.monsters.remove(monster)  # นำมอนสเตอร์ออกจากรายการ
                self.killed_monsters += 1
                if self.killed_monsters == 1:
                    Clock.schedule_once(self.spawn_next_monster, 5)
                elif self.killed_monsters == 2:
                    Clock.schedule_once(self.spawn_next_monster, 5)


class ClassSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(ClassSelectionScreen, self).__init__(**kwargs)
        self.name = 'class_selection_screen'

        layout = FloatLayout()

        bg_image = Image(source='howtoplay/howtoplay.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg_image)

        # Warrior Button
        warrior_button = Button(text="Warrior", font_size=20, size_hint=(None, None), size=(200, 45))
        warrior_button.background_color = (0.8, 0.4, 0.2, 1)
        warrior_button.color = (1, 1, 1, 1)
        warrior_button.border = (5, 5, 5, 5)
        warrior_button.border_radius = [10]
        warrior_button.bind(on_release=self.switch_to_game)
        layout.add_widget(warrior_button)

        # Position Warrior Button
        warrior_button.pos_hint = {'center_x': 0.5, 'y': 0.1}

        # Archer Button
        self.archer_button = Button(text="Archer", font_size=20, size_hint=(None, None), size=(200, 45))
        self.archer_button.background_color = (0.2, 0.6, 1, 1)
        self.archer_button.color = (1, 1, 1, 1)
        self.archer_button.border = (5, 5, 5, 5)
        self.archer_button.border_radius = [10]
        self.archer_button.bind(on_release=self.update_button)
        layout.add_widget(self.archer_button)

        # Position Archer Button
        self.archer_button.pos_hint = {'center_x': 0.5, 'y': 0.05}

        # Mage Button
        self.mage_button = Button(text="Mage", font_size=20, size_hint=(None, None), size=(200, 45))
        self.mage_button.background_color = (1, 0.4, 0.6, 1)
        self.mage_button.color = (1, 1, 1, 1)
        self.mage_button.border = (5, 5, 5, 5)
        self.mage_button.border_radius = [10]
        self.mage_button.bind(on_release=self.update_button)
        layout.add_widget(self.mage_button)

        # Position Mage Button
        self.mage_button.pos_hint = {'center_x': 0.5, 'y': 0}

        self.add_widget(layout)

    def switch_to_game(self, instance):
        # Switch to the Game Screen
        self.manager.current = 'game_screen'

    def update_button(self, instance):
        # Change Archer and Mage Buttons to "Updating..."
        if instance == self.archer_button:
            self.archer_button.text = "Updating..."
            self.archer_button.disabled = True
        elif instance == self.mage_button:
            self.mage_button.text = "Updating..."
            self.mage_button.disabled = True


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.name = 'game_screen'

        game_widget = GameWidget()
        self.add_widget(game_widget)
        self.monsters_killed_label = Label(text="Monsters Killed: 0", font_size=20, size_hint=(None, None), size=(200, 50), pos_hint={'right': 1})
        self.add_widget(self.monsters_killed_label)

        Clock.schedule_interval(self.update_monsters_killed_label, 1)
    def update_monsters_killed_label(self, dt):
        game_widget = None
        for child in self.children:
            if isinstance(child, GameWidget):
                game_widget = child
                break

        if game_widget:
            self.monsters_killed_label.text = f"Monsters Killed: {game_widget.killed_monsters}"


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.name = 'main_menu'

        layout = BoxLayout(orientation='vertical')
        window_width, window_height = Window.size
        self.background = Image(source='back/welcome.png', size=(window_width, window_height))

        # เพิ่มภาพพื้นหลังลงในเมนู
        self.add_widget(self.background)
        start_button = Button(text="Start Game", font_size=20, size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        start_button.background_normal = ''  # ลบพื้นหลังปกติของปุ่ม
        start_button.background_color = (0, 0, 1, 1)  # ตั้งค่าสีพื้นหลังของปุ่ม
        self.add_widget(start_button)

        start_button = Button(text="Start Game", font_size=20, size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        start_button.background_normal = ''
        start_button.background_color = (0, 0, 1, 1)
        start_button.bind(on_release=self.switch_to_class_selection)
        layout.add_widget(start_button)

        self.add_widget(layout)

    def switch_to_class_selection(self, instance):
        # Switch to the Class Selection Screen
        self.manager.current = 'class_selection_screen'


class GameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu())
        sm.add_widget(ClassSelectionScreen())
        sm.add_widget(GameScreen())
        return sm


if __name__ == '__main__':
    GameApp().run()
 