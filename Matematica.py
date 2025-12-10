import customtkinter as ctk
import random

TotalSoma = 0
TotalSubtraçao = 0
TotalMultiplicaçao = 0
TotalDivisao = 0
TotalAleatoriedade = 0

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("340x450")
app.title("Calculadora")
app.resizable(False, False)


Titulo = ctk.CTkLabel(app, text="Calculadora", fg_color="transparent", font=("arial", 30, "bold"))
Titulo.pack()
MenuContas = ctk.CTkFrame(app, width=600, height=425, bg_color="gray", fg_color="transparent", border_color="black", border_width=4)
MenuContas.pack(padx=5 ,pady=15)

def Adiçao():
     MenuContas.forget()
     MenuAdiçao = ctk.CTkFrame(app, width=600, height=425, bg_color="gray", fg_color="transparent", border_color="black", border_width=4)
     MenuAdiçao.pack(padx=5 ,pady=15)
     EntradaSoma = ctk.CTkEntry(MenuAdiçao, width=200,height=50, placeholder_text="Digite um valor para somar...", bg_color="gray")
     EntradaSoma.place(x=65, y=25)
     ValorTotalSoma = ctk.CTkLabel(MenuAdiçao, text=f"O Resultado é igual à: {TotalSoma}", font=("arial", 20, "bold"), bg_color="gray",fg_color="transparent")
     ValorTotalSoma.place(x=50, y=200)
     def Somar():
        global TotalSoma
        try:
            ValorEntradaSoma = int(EntradaSoma.get())
            TotalSoma += ValorEntradaSoma
            EntradaSoma.delete(0,"end")
            ValorTotalSoma.configure(text=f"O Resultado é igual à: {TotalSoma}")
        except ValueError:
            pass 
     BotaoAdicionar = ctk.CTkButton(MenuAdiçao, width=100, height=75, text="Adicionar valor", bg_color="gray", fg_color="#0058CC", command=Somar, border_color="black", border_width=4)
     BotaoAdicionar.place(x=110, y=100)


def Subtração():
    MenuContas.forget()
    MenuSubtraçao = ctk.CTkFrame(app, width=600, height=425, bg_color="gray", fg_color="transparent",border_color="black", border_width=4)
    MenuSubtraçao.pack(padx=5 ,pady=15)
    EntradaSubtraçao = ctk.CTkEntry(MenuSubtraçao, width=200,height=50, placeholder_text="Digite o outro valor...", bg_color="gray")
    EntradaSubtraçao.place(x=75, y=75)
    ValorTotalSubtraçao = ctk.CTkLabel(MenuSubtraçao, text=f"O Resultado é igual à: {TotalSubtraçao}", font=("arial", 20, "bold"), bg_color="gray",fg_color="transparent")
    ValorTotalSubtraçao.place(x=75, y=250)
    ValorSubtraçao = ctk.CTkEntry(MenuSubtraçao, width=200,height=50, placeholder_text="Digite um valor para Subtrair...", bg_color="gray")
    ValorSubtraçao.place(x=75, y=10)
    def Subtrair():
         global TotalSubtraçao
         try:
             ValorEntradaSubtraçao = int(EntradaSubtraçao.get())
             ValorInicialSubtraçao = int(ValorSubtraçao.get())
             TotalSubtraçao = ValorInicialSubtraçao - ValorEntradaSubtraçao
             EntradaSubtraçao.delete(0,"end")
             ValorSubtraçao.delete(0,"end")
             ValorTotalSubtraçao.configure(text=f"O Resultado é igual à: {TotalSubtraçao}")
         except ValueError:
             pass
    BotaoSubtrair = ctk.CTkButton(MenuSubtraçao, width=100, height=75, text="Subtrair valor", bg_color="gray", fg_color="#0058CC", command=Subtrair, border_color="black", border_width=4)
    BotaoSubtrair.place(x=115, y=150)


def Multiplicaçao():
    MenuContas.forget()
    MenuMultiplicaçao = ctk.CTkFrame(app, width=600, height=425, bg_color="gray", fg_color="transparent", border_color="black", border_width=4)
    MenuMultiplicaçao.pack(padx=5 ,pady=15)
    EntradaMultiplicaçao = ctk.CTkEntry(MenuMultiplicaçao, width=200,height=50, placeholder_text="Digite o outro valor...", bg_color="gray")
    EntradaMultiplicaçao.place(x=65, y=75)
    ValorTotalMultiplicaçao = ctk.CTkLabel(MenuMultiplicaçao, text=f"O Resultado é igual à: {TotalMultiplicaçao}", font=("arial", 20, "bold"), bg_color="gray",fg_color="transparent")
    ValorTotalMultiplicaçao.place(x=50, y=250)
    ValorMultiplicaçao = ctk.CTkEntry(MenuMultiplicaçao, width=200,height=50, placeholder_text="Digite um valor para Multiplicar...", bg_color="gray")
    ValorMultiplicaçao.place(x=65, y=10)
    def Multiplicar():
         global TotalMultiplicaçao
         try:
             ValorEntradaMultiplicaçao = int(EntradaMultiplicaçao.get())
             ValorInicialMultiplicaçao = int(ValorMultiplicaçao.get())
             TotalMultiplicaçao = ValorInicialMultiplicaçao * ValorEntradaMultiplicaçao
             EntradaMultiplicaçao.delete(0,"end")
             ValorMultiplicaçao.delete(0,"end")
             ValorTotalMultiplicaçao.configure(text=f"O Resultado é igual à: {TotalMultiplicaçao}")
         except ValueError:
             pass
    BotaoMultiplicar = ctk.CTkButton(MenuMultiplicaçao, width=100, height=75, text="Multiplicar valor", bg_color="gray", fg_color="#0058CC", command=Multiplicar, border_color="black", border_width=4)
    BotaoMultiplicar.place(x=105, y=150)

def Divisao():
    MenuContas.forget()
    MenuDivisao = ctk.CTkFrame(app, width=600, height=425, bg_color="gray", fg_color="transparent", border_color="black", border_width=4)
    MenuDivisao.pack(padx=5 ,pady=15)
    EntradaDivisao = ctk.CTkEntry(MenuDivisao, width=200,height=50, placeholder_text="Digite o outro valor...", bg_color="gray")
    EntradaDivisao.place(x=65, y=75)
    ValorTotalDivisao = ctk.CTkLabel(MenuDivisao, text=f"O Resultado é igual à: {TotalDivisao}", font=("arial", 20, "bold"), bg_color="gray",fg_color="transparent")
    ValorTotalDivisao.place(x=50, y=250)
    ValorDivisao = ctk.CTkEntry(MenuDivisao, width=200,height=50, placeholder_text="Digite um valor para Dividir...", bg_color="gray")
    ValorDivisao.place(x=65, y=10)
    def Dividir():
         global TotalDivisao
         try:
             ValorEntradaDivisao = int(EntradaDivisao.get())
             ValorInicialDivisao = int(ValorDivisao.get())
             TotalDivisao = ValorInicialDivisao / ValorEntradaDivisao
             EntradaDivisao.delete(0,"end")
             ValorDivisao.delete(0,"end")
             ValorTotalDivisao.configure(text=f"O Resultado é igual à: {TotalDivisao}")
         except ValueError:
             pass
    BotaoDividir = ctk.CTkButton(MenuDivisao, width=100, height=75, text="Dividir Valor", bg_color="gray", fg_color="#0058CC", command=Dividir, border_color="black", border_width=4)
    BotaoDividir.place(x=105, y=150)


def Aleatoriedade():
    MenuContas.forget()
    MenuAleatoriedade = ctk.CTkFrame(app, width=600, height=425, bg_color="gray", fg_color="transparent", border_color="black", border_width=4)
    MenuAleatoriedade.pack(padx=5 ,pady=15)
    EntradaAleatoriedade = ctk.CTkEntry(MenuAleatoriedade, width=200,height=50, placeholder_text="Digite o outro valor...", bg_color="gray")
    EntradaAleatoriedade.place(x=65, y=75)
    ValorTotalAleatoriedade = ctk.CTkLabel(MenuAleatoriedade, text=f"O seu valor aleatorio é igual à: {TotalAleatoriedade}", font=("arial", 17, "bold"), bg_color="gray",fg_color="transparent")
    ValorTotalAleatoriedade.place(x=10, y=250)
    ValorAleatoriedade = ctk.CTkEntry(MenuAleatoriedade, width=200,height=50, placeholder_text="Digite um valor para calcular...", bg_color="gray")
    ValorAleatoriedade.place(x=65, y=10)
    def CalcularAleatorio():
         global TotalAleatoriedade
         try:
             ValorEntradaAleatoriedade = int(EntradaAleatoriedade.get())
             ValorInicialAleatoriedade = int(ValorAleatoriedade.get())
             TotalAleatoriedade = random.randint(ValorInicialAleatoriedade, ValorEntradaAleatoriedade)
             EntradaAleatoriedade.delete(0,"end")
             ValorAleatoriedade.delete(0,"end")
             ValorTotalAleatoriedade.configure(text=f"O seu valor aleatorio é igual à: {TotalAleatoriedade}")
         except ValueError:
             pass
    BotaoAleatorio = ctk.CTkButton(MenuAleatoriedade, width=100, height=75, text="Valor Aleatorio", bg_color="gray", fg_color="#0058CC", command=CalcularAleatorio, border_color="black", border_width=4)
    BotaoAleatorio.place(x=105, y=150)

def MenuOperaçao():
     MenuContas.pack(padx=5 ,pady=15)
     BotaoAdiçao = ctk.CTkButton(MenuContas, width=100, height=100, text="Adição", bg_color="gray", fg_color="#0058CC", command=Adiçao, border_color="black", border_width=4)
     BotaoAdiçao.place(x=5, y=10)
     BotaoSubtração = ctk.CTkButton(MenuContas, width=100, height=100, text="Subtração", bg_color="gray", fg_color="#0058CC", command=Subtração, border_color="black", border_width=4)
     BotaoSubtração.place(x=115, y=10)
     BotaoMultiplicaçao = ctk.CTkButton(MenuContas, width=100, height=100, text="Multiplicaçao", bg_color="gray", fg_color="#0058CC", command=Multiplicaçao, border_color="black", border_width=4)
     BotaoMultiplicaçao.place(x=225, y=10)
     BotaoDivisao = ctk.CTkButton(MenuContas, width=100, height=100, text="Divisão", bg_color="gray", fg_color="#0058CC", command=Divisao, border_color="black", border_width=4)
     BotaoDivisao.place(x=5, y=120)
     BotaoAleatoriedade = ctk.CTkButton(MenuContas, width=100, height=100, text="Aleatoriedade", bg_color="gray", fg_color="#0058CC", command=Aleatoriedade, border_color="black", border_width=4)
     BotaoAleatoriedade.place(x=115, y=120)


     
MenuOperaçao()
app.mainloop()
