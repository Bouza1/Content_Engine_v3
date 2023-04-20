from kivy.core.window import Window
from kivy.properties import ObjectProperty
from socialEngine import fullScriptLI
from socialEngine import fullScriptTW
from socialEngine import openArticleBrowser
from scraper import news2Array
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import threading


# # if this is first time using please fill in username and password below otherwise leave blank
# username = ""
# password = ""
Window.size = (900, 400)

def merge_dictionaries(dict1, dict2):
    scrappedData = dict1 | dict2
    return scrappedData

# print(merge_dictionaries(news2Array("technews", "week", 1000), news2Array('hardware', 'week', 100)))
# scrappedData = news2Array("technews", "week", 1000)
# scrappedData = news2Array('hardware', 'week', 100)

scrappedData = merge_dictionaries(news2Array("technews", "week", 1000), news2Array('hardware', 'week', 100))
global i
i = 0

class Viewer(Screen):
    txtArea = ObjectProperty(None)
    def nextBtn(self):
        global i
        if i < len(scrappedData) - 1 and i >= 0:
            i = i + 1
            print(i)
            title = scrappedData[i][0]
            if len(scrappedData[i][0]) > 80:
                title = title[:100]
            self.ids.titleLbl.text = title
            self.ids.txtArea.text = title
            self.ids.backBtn.disabled = False
            self.ids.nextBtn.disabled = False
        elif i >= len(scrappedData) - 1:
            self.ids.nextBtn.disabled = True
            self.ids.backBtn.disabled = False

    def backBtn(self):
        global i
        if i <= len(scrappedData) and i > 0:
            i = i - 1
            print(i)
            self.ids.backBtn.disabled = False
            self.ids.nextBtn.disabled = False
            title = scrappedData[i][0]
            if len(scrappedData[i][0]) > 80:
                title = title[:100]
            self.ids.titleLbl.text = title
            self.ids.txtArea.text = title
        elif i <= 0:
            i = 0
            self.ids.backBtn.disabled = True
            self.ids.nextBtn.disabled = False
            self.ids.text = scrappedData[i][0]

    def openArticle(self):
        global i
        print("Open")
        openArticleBrowser(scrappedData[i][1])
    
    def rewrite(self):
        global i
        self.ids.txtArea.text = "Add Rewrite Function Here"

    def postArticle(self):
        global i
        new_thread = threading.Thread(target=fullScriptLI, args=(username, password, self.txtArea.text, scrappedData[i][1]))
        new_thread.start()
        # fullScriptLI(username, password, self.txtArea.text, scrappedData[i][1])
    
    def postTwitter(self):
        new_thread = threading.Thread(target=fullScriptTW, args=(self.txtArea.text, scrappedData[i][1]))
        new_thread.start()
        # fullScriptTW(self.txtArea.text, scrappedData[i][1])


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

sm = WindowManager()
sm.add_widget(Viewer(name='Viewer'))


class MyMainApp(App):
    def build(self):
        return sm
    
if __name__ == "__main__":
    MyMainApp().run()

