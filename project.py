import webbrowser
import pyautogui
import time
class Nav:
    def Painel(self):
        self.navegar()
        time.sleep(3)
        self.EscreverNome()
        time.sleep(1)
        self.tirarPrint()
        self.MarcarMac()
        self.BaixarArquivo()
        time.sleep(2)
        self.alertFim()

    def navegar(self):
        webbrowser.open('https://cursoautomacao.netlify.app/')
        
    def EscreverNome(self):
        pyautogui.moveTo(322,163, duration=1.1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.scroll(-2000)
        pyautogui.moveTo(71,397, duration=1.1)
        pyautogui.click()
        pyautogui.typewrite('Guilherme')

    def tirarPrint(self):
        image = pyautogui.screenshot(imageFilename='Print_tela.png')

    def MarcarMac(self):
        pyautogui.scroll(2000)
        pyautogui.moveTo(52,297, duration=1.1)
        pyautogui.click()

    def BaixarArquivo(self):
        pyautogui.scroll(-3710)
        pyautogui.moveTo(142,176, duration=0.5)
        for i in range(4):
            pyautogui.click()
            time.sleep(0.4)
            pyautogui.move(xOffset=0, yOffset=115, duration=0.3)
        time.sleep(0.4)
        pyautogui.scroll(-120)
        pyautogui.click()

    def alertFim(self):
        pyautogui.alert(text="VOCÊ TERMINOU!", title="Desafio Concluido", button="ok :)")

root = Nav()
root.Painel()
