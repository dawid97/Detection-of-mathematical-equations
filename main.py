from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from  kivy.uix.label import Label
from  kivy.uix.gridlayout import GridLayout
from kivy.graphics import Line, Color, Rectangle
from kivy.core.window import Window
import CheckImage

class WindowArea(GridLayout):
    def __init__(self, **kwargs):
        super(WindowArea, self).__init__(**kwargs)
        self.cols = 1
        self.draw_area = DrawArea()      
        
        #Draw Area layout
        self.draw_layout = GridLayout()
        self.draw_layout.cols = 1
        self.draw_layout.rows = 1
        self.draw_layout.add_widget(self.draw_area)


        #Buttons layout
        self.buttons_layout = GridLayout()
        self.buttons_layout.cols = 2
        
        self.submit_button = Button(text="Calculate!", font_size=40)
        self.submit_button.bind(on_press = self.submit_button_pressed)

        self.clear_button = Button(text="Clear!", font_size=40)
        self.clear_button.bind(on_press = self.clear_button_pressed)
        
        self.buttons_layout.add_widget(self.submit_button)
        self.buttons_layout.add_widget(self.clear_button)

        self.add_widget(self.draw_layout)
        self.add_widget(self.buttons_layout)

    def submit_button_pressed(self, instance):
        try:
            self.submit_button.text = str(eval(self.draw_area.get_equation()))
        except:
            self.submit_button.text = 'Error!'
        finally:
            self.submit_button.text += '\nPress to calculate again!'

    def clear_button_pressed(self, instance):
        self.draw_area.clear_canvas()


class DrawArea(Widget):
    def __init__(self, **kwargs):
        super(DrawArea, self).__init__(**kwargs)
        self.equation = ''

        with self.canvas:
            Color(1, 1, 1, 1, mode='rgba')
            Rectangle(pos=self.pos, size=(1920,1080))
            Color(0,0,0)
    
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y),width = 2)
        
    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)
		
    def on_touch_up(self, touch):
        file_loc = 'drawing.png'
        file_loc.replace
        Widget.export_to_png(self,file_loc)
        self.equation = CheckImage.check_image(file_loc)

    def get_equation(self):
        return self.equation

    def clear_canvas(self):
        with self.canvas:
            Color(1, 1, 1, 1, mode='rgba')
            Rectangle(pos=self.pos, size=(1920,1080))
            Color(0,0,0)


class KivyApp(App):
    
    def build(self):
        return WindowArea()

if __name__ == "__main__":
    KivyApp().run()
		