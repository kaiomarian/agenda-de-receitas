    def show_recipe(self, instance):
        recipe_name = instance.text
        recipe_info = self.recipes.get(recipe_name)
        if recipe_info:
            ingredients = recipe_info['Ingredientes']
            instructions = recipe_info['Instruções']
            recipe_text = f'Ingredientes:\n{ingredients}\n\nInstruções:\n{instructions}'
            self.lista_text.text = recipe_text
        else:
            self.lista_text.text = "Receita não encontrada."
