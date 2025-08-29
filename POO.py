class Preguntas():
    def __init__(self,title,prompt,hints,tags):
        self.title = title
        self.prompt = prompt
        self.hints = hints
        self.tags = tags
    
    def mostrar(self):
        print(self.title,self.prompt,self.hints,self.tags)
    