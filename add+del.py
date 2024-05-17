 def add_recipe(self, instance):
        name = self.inp_nome.text
        ingredients = self.inp_ing.text
        instructions = self.inp_ins.text

        if name and ingredients and instructions:
            self.recipes[name] = {'Ingredientes': ingredients, 'Instruções': instructions}

            
            recipe_button = Button(text=name)
            recipe_button.bind(on_press=self.show_recipe)
            self.recipe_list.add_widget(recipe_button)

            
            self.inp_nome.text = ''
            self.inp_ing.text = ''
            self.inp_ins.text = ''

    def delete_recipe(self, instance):
        name = self.inp_nome.text
        if name in self.recipes:
            del self.recipes[name]
        
            for child in self.recipe_list.children:
                if child.text == name:
                    self.recipe_list.remove_widget(child)
            self.inp_nome.text = ''
            self.inp_ing.text = ''
            self.inp_ins.text = ''
