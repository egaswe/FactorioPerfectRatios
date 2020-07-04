filepath = r"C:\Program Files (x86)\Steam\steamapps\common\Factorio\data\base\prototypes\recipe\demo-recipe.lua"
file = open(filepath)
lines = ""

class Recipeclass:
    def __init__(self):
        self.Name = "Init"
        self.Input = []
        self.Output = []
        self.Time = 0,5
        self.Expensive = False
    def __str__(self):
        return self.Name + "\n" + str(self.Input) + "\n" + str(self.Output) + "\n" + str(self.Time)
    def ExpensiveMethod(self):
        self.Expensive = True
    def ChangeName(self,NewName):
        if self.Expensive == False:
            self.Name = NewName
    def ChangeTime(self, NewTime):
        if self.Expensive == False:
            self.Time = NewTime
    def AddInput(self, NewItem, NewQuantity):
        self.Input.append([NewItem,NewQuantity])
    def AddOutput(self, NewItem, NewQuantity):
        self.Output.append([NewItem,NewQuantity])


    

Recipes = []
CurrentRecipe = None
for line in file:
    line = line.strip(" ")
    if line == "type = \"recipe\",\n":
        if CurrentRecipe != None:
            Recipes.append(CurrentRecipe)
        CurrentRecipe = Recipeclass()
    if line == "expensive =\n":
        CurrentRecipe.ExpensiveMethod()
    if line.startswith("name = "):
        CurrentRecipe.ChangeName(line.split("\"")[1])
    if line.startswith("ingredients ="):
        CurrentRecipe.ChangeName(line.split("\"")[1])

Recipes.append(CurrentRecipe)

for a in Recipes:
    print(a)