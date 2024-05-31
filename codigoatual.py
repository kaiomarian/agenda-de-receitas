import kivy
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class RecipeApp(App):
    def build(self):
        self.receitas = {}  # Dicionário para armazenar as receitas
        self.layout_principal = BoxLayout(orientation='vertical')

        self.entrada_nome = TextInput(hint_text='Nome da Receita', hint_text_color = get_color_from_hex('2E522C'), background_color = get_color_from_hex('BAFFC0'))
        self.entrada_ing = TextInput(hint_text='Ingredientes', hint_text_color = get_color_from_hex('2E522C'), background_color = get_color_from_hex('BAFFC0'))
        self.entrada_ins = TextInput(hint_text='Instruções', hint_text_color = get_color_from_hex('2E522C'), background_color = get_color_from_hex('BAFFC0'))
        self.espaco1 = Label(text ='', size_hint =(None, None), size = (50, 6))
        self.botao_adc = Button(text='Adicionar Receita', size_hint = (None, None), size = (150, 10), color = get_color_from_hex('BAFFC0'), background_normal ='none',  background_color = get_color_from_hex('2E522C'))
        self.botao_adc.bind(on_press=self.adicionar_receita)
        self.espaco2 = Label(text = '', size_hint = (None, None), size = (150, 50))
        self.botao_mostrar_esconder = Button(text='Mostrar/Esconder Receitas', size_hint=(None, None), size=(150, 10), color=get_color_from_hex('BAFFC0'), background_normal="None",  background_color=get_color_from_hex('2E522C'))
        self.botao_mostrar_esconder.bind(on_press=self.mostrar_esconder_receitas)
        self.espaco3 = Label(text = '', size_hint = (None, None), size = (150, 50))
        self.botao_del = Button(text='Apagar Receita', size_hint = (None, None), size = (150, 10), color = get_color_from_hex('BAFFC0'), background_normal = "None",  background_color = get_color_from_hex('2E522C'))
        self.botao_del.bind(on_press=self.apagar_receita)

        self.texto_lista = Label(text='Receitas Disponíveis:', color = get_color_from_hex('2E522C'),  size_hint =(None, None), size = (600, 90))
        self.lista_receitas = BoxLayout(orientation='vertical', size_hint_y=None)
        self.lista_receitas.bind(minimum_height=self.lista_receitas.setter('height'))
        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.lista_receitas)

        self.layout_principal.add_widget(self.entrada_nome)
        self.layout_principal.add_widget(self.entrada_ing)
        self.layout_principal.add_widget(self.entrada_ins)
        self.layout_principal.add_widget(self.espaco1)
        self.layout_principal.add_widget(self.botao_adc)
        self.layout_principal.add_widget(self.espaco2)
        self.layout_principal.add_widget(self.botao_del)
        self.layout_principal.add_widget(self.espaco3)
        self.layout_principal.add_widget(self.botao_mostrar_esconder)
        self.layout_principal.add_widget(self.texto_lista)
        self.layout_principal.add_widget(self.scroll_view)
        Window.clearcolor = get_color_from_hex('#DEFFDA')
        Window.size = (500, 700)
        return self.layout_principal

    def adicionar_receita(self, instance):
        nome = self.entrada_nome.text
        ingredientes = self.entrada_ing.text
        instrucoes = self.entrada_ins.text

        if nome and ingredientes and instrucoes:
            if nome not in self.receitas:  # Check if recipe with same name already exists
                self.receitas[nome] = {'Ingredientes': ingredientes, 'Instruções': instrucoes}

                botao_receita = Button(text=nome, color=get_color_from_hex('BAFFC0'), background_normal="None",  background_color=get_color_from_hex('2E522C'), size_hint=(None, None), size=(500, 50))
                botao_receita.bind(on_press=self.mostrar_receita)
                self.lista_receitas.add_widget(botao_receita)

                self.entrada_nome.text = ''
                self.entrada_ing.text = ''
                self.entrada_ins.text = ''
        else:
            self.texto_lista.text = 'já tem receita com esse nome'

    def apagar_receita(self, instance):
        nome = self.entrada_nome.text
        if nome in self.receitas:
            del self.receitas[nome]

            for child in self.lista_receitas.children:
                if child.text == nome:
                    self.lista_receitas.remove_widget(child)
            self.entrada_nome.text = ''
            self.entrada_ing.text = ''
            self.entrada_ins.text = ''

    def mostrar_receita(self, instance):
        nome_receita = instance.text
        informacao_receita = self.receitas.get(nome_receita)
        if informacao_receita:
            ingredientes = informacao_receita['Ingredientes']
            instrucoes = informacao_receita['Instruções']
            texto_receita = f'Ingredientes:\n{ingredientes}\n\nInstruções:\n{instrucoes}'
            self.texto_lista.text = texto_receita
            self.texto_lista.color = get_color_from_hex('2E522C') 
        else:
            self.texto_lista.text = "Receita não encontrada."
        
    def mostrar_esconder_receitas(self, instance):
        if self.lista_receitas.height > 0:
            self.lista_receitas.height = 0
            self.botao_mostrar_esconder.text = 'Mostrar Receitas'
        else:
            self.lista_receitas.height = self.lista_receitas.minimum_height
            self.botao_mostrar_esconder.text = 'Esconder Receitas'

if __name__ == '__main__':
    RecipeApp().run()
