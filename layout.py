import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class RecipeApp(App):
    def build(self):
        self.recipes = {}  # Dicionário para armazenar as receitas

        self.main_layout = BoxLayout(orientation='vertical')
        
        self.inp_nome = TextInput(hint_text='Nome da Receita', hint_text_color = get_color_from_hex('2E522C'), background_color = get_color_from_hex('BAFFC0'))
        self.inp_ing = TextInput(hint_text='Ingredientes', hint_text_color = get_color_from_hex('2E522C'), background_color = get_color_from_hex('BAFFC0'))
        self.inp_ins = TextInput(hint_text='Instruções', hint_text_color = get_color_from_hex('2E522C'), background_color = get_color_from_hex('BAFFC0'))
        self.espaco1 = Label(text ='', size_hint =(None, None), size = (10, 5))
        self.adc_rec = Button(text='Adicionar Receita', size_hint = (None, None), size = (150, 10), color = get_color_from_hex('BAFFC0'))
        self.adc_rec.bind(on_press=self.add_recipe)
        self.espaco2 = Label(text = '', size_hint = (None, None), size = (150, 50))
        self.del_rec = Button(text='Apagar Receita', size_hint = (None, None), size = (150, 10), color = get_color_from_hex('BAFFC0'))
        self.del_rec.bind(on_press=self.delete_recipe)

        self.lista_text = Label(text='Receitas Disponíveis:')
        self.recipe_list = BoxLayout(orientation='vertical')

        self.main_layout.add_widget(self.inp_nome)
        self.main_layout.add_widget(self.inp_ing)
        self.main_layout.add_widget(self.inp_ins)
        self.main_layout.add_widget(self.espaco1)
        self.main_layout.add_widget(self.adc_rec)
        self.main_layout.add_widget(self.espaco2)
        self.main_layout.add_widget(self.del_rec)
        self.main_layout.add_widget(self.lista_text)
        self.main_layout.add_widget(self.recipe_list)
        Window.clearcolor = get_color_from_hex('000000')
        Window.size = (500, 700)
        return self.main_layout
    
if __name__ == '__main__':
    RecipeApp().run()    
