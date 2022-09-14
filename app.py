"""
Code compiler
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW,BOTTOM,LEFT,RIGHT
import httpx
import json
import random
import string
import tempfile

class rextester(toga.App):
    async def getquote(self,widget):
                
                try:
                    async with httpx.AsyncClient() as client:
                        response = await client.get("https://api.quotable.io/random")

                        payload = response.json()
                        self.main_window.info_dialog(
                        payload['author'],
                        payload['content'],
                    )
                except:
                        self.main_window.info_dialog(
                        'Internet Error',
                        'Check internet connectivity',)
    def rexa(self,widget):
        self.main_box.remove(self.homebox)
        
        self.homebox=toga.Box(style=Pack(direction=COLUMN))
        source_label = toga.Label(
            'Source code: ',
            
        )

        button = toga.Button(
            'Compile',
            on_press=self.compile,
            style=Pack(background_color='green')
            
        )

        

        rex = toga.Command(
        self.rexa,
        'Rextester',
        tooltip='Perform action 0',
        #icon=brutus_icon,
        order=1
    )
        memes = toga.Command(
            self.memesa,
            'Memes',
            tooltip='Perform action 1',
            #icon=brutus_icon,
            order=2 
        )
        quotes = toga.Command(
            self.quotesa,
            'Quotes',
            tooltip='Perform action 2',
            #icon=toga.Icon.TOGA_ICON,
            order=3 
        )
        

        self.output = toga.MultilineTextInput(style=Pack(flex=1,padding_right=10,height=400),readonly=True )
        
        self.code = toga.MultilineTextInput(style=Pack(flex=1,padding_bottom=600,height=100),placeholder="Syntax:\nLanguage-number\ncode\nExample:\n38\necho 'Hello world'\nNB: type 'list' to get language numbers")

        
        codeBox = toga.Box()
        codeBox.add(source_label)
        codeBox.add(self.code)
        codeBox.add(button)

        self.homebox.add(self.output)
        self.homebox.add(codeBox)
        self.main_box.add(self.homebox)

        self.main_window.show()
            
    def quotesa(self,sender):
              
                button = toga.Button(
                    'generate quote!',
                    on_press=self.getquote,
                    style=Pack(flex=1,padding=100)
                )

                self.main_box.remove(self.homebox)
                self.homebox = toga.Box()
                
                self.homebox.add(button)
                self.main_box.add(self.homebox)
                
                self.main_window.show()
                

    async def getmeme(self,widget):
              
                self.main_box.remove(self.homebox)
                try:
                    async with httpx.AsyncClient() as cs:
                        r= await  cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot')
                

                    res =  r.json()
                
                    
                    while 1:
                        link = res['data']['children'] [random.randint(0, 15)]['data']['url']
                        if link[-3:] != 'gif':
                            break
                    async with httpx.AsyncClient() as cs:
                        r= await  cs.get(link)
                        im = r.content
                            
                            
                    with  tempfile.NamedTemporaryFile(delete=False) as temp:
                            
                                temp.write(im)
                                temp.close()
                    view = toga.ImageView(id='view',image=toga.Image(temp.name))
                    
                    button = toga.Button(
                            'Generate meme!',
                            on_press=self.getmeme,
                            style=Pack(flex=1,padding=50)
                            
                        )
                
                    self.homebox = toga.Box(style=Pack(direction=COLUMN))
                    
                    self.homebox.add(button)
                    self.homebox.add(view)
                    
                    self.main_box.add(self.homebox)
                    self.main_window.show()
                
                except httpx.ConnectError:
                    self.main_window.info_dialog(
                        'Error',
                        'Connectivity Error',)
                    self.memesa(widget)
    def memesa(self,widget):
        self.main_box.remove(self.homebox)
        
        button = toga.Button(
            'Generate meme!',
            on_press=self.getmeme,
            style=Pack(flex=1,padding=50)
            
        )
        self.homebox = toga.Box()
        self.homebox.add(button)
        self.main_box.add(self.homebox)
        self.main_window.show()
    
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

            
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.homebox=toga.Box(style=Pack(direction=COLUMN))
        source_label = toga.Label(
            'Source code: ',
            
        )

        button = toga.Button(
            'Compile',
            on_press=self.compile,
            style=Pack(background_color='green')
            
        )

        

        rex = toga.Command(
        self.rexa,
        'Rextester',
        tooltip='Perform action 0',
        #icon=brutus_icon,
        order=1
    )
        memes = toga.Command(
            self.memesa,
            'Memes',
            tooltip='Perform action 1',
            #icon=brutus_icon,
            order=2 
        )
        quotes = toga.Command(
            self.quotesa,
            'Quotes',
            tooltip='Perform action 2',
            #icon=toga.Icon.TOGA_ICON,
            order=3 
        )

        self.output = toga.MultilineTextInput(style=Pack(flex=1,padding_right=10,height=400),readonly=True )
        
        self.code = toga.MultilineTextInput(style=Pack(flex=1,padding_bottom=600,height=100),placeholder="Syntax:\nLanguage-number\ncode\nExample:\n38\necho 'Hello world'\nNB: type 'list' to get language numbers")

        
        codeBox = toga.Box()
        codeBox.add(source_label)
        codeBox.add(self.code)
        codeBox.add(button)

        self.homebox.add(self.output)
        self.homebox.add(codeBox)
        self.main_box.add(self.homebox)
        
        #self.commands.add(rex, memes, quotes)
        
        
        self.main_window = toga.MainWindow(title="DeepState")
        self.main_window.toolbar.add(rex, memes, quotes)
        self.main_window.content = self.main_box
        self.main_window.show()

    async def compile(self,widget):
        code = self.code.value
        ln = code.partition('\n')[0]

        if ln == 'list':
            lst ="""
        C# = 1
        VB.NET = 2
        F# = 3
        Java = 4
        Python = 5
        C (gcc) = 6
        C++ (gcc) = 7
        Php = 8
        Pascal = 9
        Objective-C = 10
        Haskell = 11
        Ruby = 12
        Perl = 13
        Lua = 14
        Nasm = 15
        Sql Server = 16
        Javascript = 17
        Lisp = 18
        Prolog = 19
        Go = 20
        Scala = 21
        Scheme = 22
        Node.js = 23
        Python 3 = 24
        Octave = 25
        C (clang) = 26
        C++ (clang) = 27    
        C++ (vc++) = 28
        C (vc) = 29
        D = 30
        R = 31
        Tcl = 32
        MySQL = 33
        PostgreSQL = 34
        Oracle = 35
        Swift = 37
        Bash = 38
        Ada = 39
        Erlang = 40
        Elixir = 41
        Ocaml = 42
        Kotlin = 43
        Brainf*** = 44
        Fortran = 45,
        Rust = 46,
        Clojure = 47 """
            self.output.value=lst
            return
        try:
            num = int(ln.strip())
        except:
            self.output.value ='Language number should be an integer between 1 and 47'
            return
        
        if 1>num or num>47  :
            self.output.value ="""Language number needs to be between 1 and 47
Type 'list' to get language numbers.
"""
            return

        
        code = code.split("\n",1)[1]        
        
        url = "https://rextester.com/rundotnet/Run"
        
        data={
            "LanguageChoiceWrapper": ln.strip(),
            "EditorChoiceWrapper": "1",
            "LayoutChoiceWrapper": "1",
            "Program": code,
            "Input": "",
            "Privacy": "",
            "PrivacyUsers": "",
            "Title": "",
            "SavedOutput": "",
            "WholeError": "",
            "WholeWarning": "",
            "StatsToSave": "",
            "CodeGuid": "",
            "IsInEditMode": "False",
            "IsLive": "False"
    }
        try:
            async with httpx.AsyncClient() as cs:

                timeout = httpx.Timeout(13.0, read=None)
                res = await cs.post(url,data=data,timeout=timeout) 
                
                res = json.loads(res.text)
                
                if res['Errors'] != None:
                    if len(res['Errors']) > 6000:
                        res['Errors']=res['Errors'][:1000]
                    
                    self.output.value=res['Errors']
                    return
                 
                result =res['Result']
                if len(result) > 1024:
                    
                    c=0
                    while 1:
                        
                       if  result[900+c]=='\n':
                               result=result[:900+c]+"\n.\n.\n.\n"
                               break
                       if c==100:
                          result= result[:1000]
                          break
                       c+=1

                elif result =='' or result.isspace():
                    result='‎‎ \n'
                
                self.output.value=res['Result']
        except TimeoutError:
                self.output.value='Timeout Error'
                
        except :
                self.output.value='Check internet connectivity'
                
    

        


def main():
    
    return rextester()
