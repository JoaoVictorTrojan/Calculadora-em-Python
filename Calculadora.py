import customtkinter as ctk
import random
import math

TotalSoma = 0
TotalSubtraçao = 0
TotalMultiplicaçao = 0
TotalDivisao = 0
TotalAleatoriedade = 0
TotalPotenciacao = 0
TotalRaizQuadrada = 0
TotalPorcentagem = 0
TotalFatorial = 0
TotalHipotenusa = 0
TotalIMC = 0
Delta = 0
x1 = 0
x2= 0


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("340x520")
app.title("Calculadora")
app.resizable(False, False)


Titulo = ctk.CTkLabel(app, text="Calculadora", fg_color="transparent", font=("arial", 30, "bold"))
Titulo.pack()
MenuContas = ctk.CTkFrame(app, width=600, height=535, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
MenuContas.pack(padx=5 ,pady=15)

def Adiçao():
     MenuContas.forget()
     MenuAdiçao = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
     MenuAdiçao.pack(padx=5 ,pady=15)
     EntradaSoma = ctk.CTkEntry(MenuAdiçao, width=200,height=50, placeholder_text="Digite um valor para somar...", bg_color="#222222")
     EntradaSoma.place(x=65, y=25)
     ValorTotalSoma = ctk.CTkLabel(MenuAdiçao, text=f"O Resultado é igual à: \n{TotalSoma}", font=("arial", 20, "bold"), bg_color="#222222",fg_color="transparent")
     ValorTotalSoma.place(x=50, y=200)
     def Somar():
        global TotalSoma
        try:
            ValorEntradaSoma = int(EntradaSoma.get())
            TotalSoma += ValorEntradaSoma
            EntradaSoma.delete(0,"end")
            ValorTotalSoma.configure(text=f"O Resultado é igual à: \n{TotalSoma}")
        except ValueError:
            pass 
     BotaoAdicionar = ctk.CTkButton(MenuAdiçao, width=100, height=75, text="Adicionar valor", bg_color="#222222", fg_color="#0058CC", command=Somar, border_color="black", border_width=4)
     BotaoAdicionar.place(x=110, y=100)


def Subtração():
    MenuContas.forget()
    MenuSubtraçao = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent",border_color="black", border_width=4)
    MenuSubtraçao.pack(padx=5 ,pady=15)
    EntradaSubtraçao = ctk.CTkEntry(MenuSubtraçao, width=200,height=50, placeholder_text="Digite o outro valor...", bg_color="#222222")
    EntradaSubtraçao.place(x=75, y=75)
    ValorTotalSubtraçao = ctk.CTkLabel(MenuSubtraçao, text=f"O Resultado é igual à: \n{TotalSubtraçao}", font=("arial", 20, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalSubtraçao.place(x=75, y=250)
    ValorSubtraçao = ctk.CTkEntry(MenuSubtraçao, width=200,height=50, placeholder_text="Digite um valor para Subtrair...", bg_color="#222222")
    ValorSubtraçao.place(x=75, y=10)
    def Subtrair():
         global TotalSubtraçao
         try:
             ValorEntradaSubtraçao = int(EntradaSubtraçao.get())
             ValorInicialSubtraçao = int(ValorSubtraçao.get())
             TotalSubtraçao = ValorInicialSubtraçao - ValorEntradaSubtraçao
             EntradaSubtraçao.delete(0,"end")
             ValorSubtraçao.delete(0,"end")
             ValorTotalSubtraçao.configure(text=f"O Resultado é igual à: \n{TotalSubtraçao}")
         except ValueError:
             pass
    BotaoSubtrair = ctk.CTkButton(MenuSubtraçao, width=100, height=75, text="Subtrair valor", bg_color="#222222", fg_color="#0058CC", command=Subtrair, border_color="black", border_width=4)
    BotaoSubtrair.place(x=115, y=150)


def Multiplicaçao():
    MenuContas.forget()
    MenuMultiplicaçao = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuMultiplicaçao.pack(padx=5 ,pady=15)
    EntradaMultiplicaçao = ctk.CTkEntry(MenuMultiplicaçao, width=200,height=50, placeholder_text="Digite o outro valor...", bg_color="#222222")
    EntradaMultiplicaçao.place(x=65, y=75)
    ValorTotalMultiplicaçao = ctk.CTkLabel(MenuMultiplicaçao, text=f"O Resultado é igual à: \n{TotalMultiplicaçao}", font=("arial", 20, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalMultiplicaçao.place(x=50, y=250)
    ValorMultiplicaçao = ctk.CTkEntry(MenuMultiplicaçao, width=200,height=50, placeholder_text="Digite um valor para Multiplicar...", bg_color="#222222")
    ValorMultiplicaçao.place(x=65, y=10)
    def Multiplicar():
         global TotalMultiplicaçao
         try:
             ValorEntradaMultiplicaçao = int(EntradaMultiplicaçao.get())
             ValorInicialMultiplicaçao = int(ValorMultiplicaçao.get())
             TotalMultiplicaçao = ValorInicialMultiplicaçao * ValorEntradaMultiplicaçao
             EntradaMultiplicaçao.delete(0,"end")
             ValorMultiplicaçao.delete(0,"end")
             ValorTotalMultiplicaçao.configure(text=f"O Resultado é igual à: \n{TotalMultiplicaçao}")
         except ValueError:
             pass
    BotaoMultiplicar = ctk.CTkButton(MenuMultiplicaçao, width=100, height=75, text="Multiplicar valor", bg_color="#222222", fg_color="#0058CC", command=Multiplicar, border_color="black", border_width=4)
    BotaoMultiplicar.place(x=105, y=150)

def Divisao():
    MenuContas.forget()
    MenuDivisao = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuDivisao.pack(padx=5 ,pady=15)
    EntradaDivisao = ctk.CTkEntry(MenuDivisao, width=200,height=50, placeholder_text="Digite o outro valor...", bg_color="#222222")
    EntradaDivisao.place(x=65, y=75)
    ValorTotalDivisao = ctk.CTkLabel(MenuDivisao, text=f"O Resultado é igual à: \n{TotalDivisao}", font=("arial", 20, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalDivisao.place(x=50, y=250)
    ValorDivisao = ctk.CTkEntry(MenuDivisao, width=200,height=50, placeholder_text="Digite um valor para Dividir...", bg_color="#222222")
    ValorDivisao.place(x=65, y=10)
    def Dividir():
         global TotalDivisao
         try:
             ValorEntradaDivisao = int(EntradaDivisao.get())
             ValorInicialDivisao = int(ValorDivisao.get())
             TotalDivisao = ValorInicialDivisao / ValorEntradaDivisao
             EntradaDivisao.delete(0,"end")
             ValorDivisao.delete(0,"end")
             ValorTotalDivisao.configure(text=f"O Resultado é igual à: \n{TotalDivisao}")
         except ValueError:
             pass
    BotaoDividir = ctk.CTkButton(MenuDivisao, width=100, height=75, text="Dividir Valor", bg_color="#222222", fg_color="#0058CC", command=Dividir, border_color="black", border_width=4)
    BotaoDividir.place(x=105, y=150)


def Aleatoriedade():
    MenuContas.forget()
    MenuAleatoriedade = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuAleatoriedade.pack(padx=5 ,pady=15)
    EntradaAleatoriedade = ctk.CTkEntry(MenuAleatoriedade, width=200,height=50, placeholder_text="Digite o outro valor...", bg_color="#222222")
    EntradaAleatoriedade.place(x=65, y=75)
    ValorTotalAleatoriedade = ctk.CTkLabel(MenuAleatoriedade, text=f"O seu valor aleatorio é igual à: \n{TotalAleatoriedade}", font=("arial", 17, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalAleatoriedade.place(x=10, y=250)
    ValorAleatoriedade = ctk.CTkEntry(MenuAleatoriedade, width=200,height=50, placeholder_text="Digite um valor para calcular...", bg_color="#222222")
    ValorAleatoriedade.place(x=65, y=10)
    def CalcularAleatorio():
         global TotalAleatoriedade
         try:
             ValorEntradaAleatoriedade = int(EntradaAleatoriedade.get())
             ValorInicialAleatoriedade = int(ValorAleatoriedade.get())
             TotalAleatoriedade = random.randint(ValorInicialAleatoriedade, ValorEntradaAleatoriedade)
             EntradaAleatoriedade.delete(0,"end")
             ValorAleatoriedade.delete(0,"end")
             ValorTotalAleatoriedade.configure(text=f"O seu valor aleatorio é igual à: \n{TotalAleatoriedade}")
         except ValueError:
             pass
    BotaoAleatorio = ctk.CTkButton(MenuAleatoriedade, width=100, height=75, text="Valor Aleatorio", bg_color="#222222", fg_color="#0058CC", command=CalcularAleatorio, border_color="black", border_width=4)
    BotaoAleatorio.place(x=105, y=150)


def Bhaskara():
    MenuContas.forget()
    MenuBhaskara = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuBhaskara.pack(padx=5 ,pady=15)
    ValorEntradaA = ctk.CTkEntry(MenuBhaskara, width=200,height=50, placeholder_text="Digite o valor de A...", bg_color="#222222")
    ValorEntradaA.place(x=65, y=10)
    ValorEntradaB = ctk.CTkEntry(MenuBhaskara, width=200,height=50, placeholder_text="Digite o valor de B...", bg_color="#222222")
    ValorEntradaB.place(x=65, y=75)
    ValorEntradaC = ctk.CTkEntry(MenuBhaskara, width=200,height=50, placeholder_text="Digite o valor de C...", bg_color="#222222")
    ValorEntradaC.place(x=65, y=140)
    ValorBhaskara = ctk.CTkLabel(MenuBhaskara, text=f"O Resultado é igual à:", font=("arial", 17, "bold"), bg_color="#222222",fg_color="transparent")
    ValorBhaskara.place(x=10, y=300)
    def ResolverBhaskara():
         global Delta, x1, x2
         try:
             ValorA = float(ValorEntradaA.get())
             ValorB = float(ValorEntradaB.get())
             ValorC =  float(ValorEntradaC.get())
             Delta = (ValorB**2) - (4*ValorA*ValorC)
             x1 = ((((-1)*ValorB) + (Delta**0.5))/(2*ValorA))
             x2 = ((((-1)*ValorB) - (Delta**0.5))/(2*ValorA))
             ValorEntradaA.delete(0,"end")
             ValorEntradaB.delete(0,"end")
             ValorEntradaC.delete(0,"end")
             if Delta == 0:
              ValorBhaskara.configure(text=f"Como delta é igual a zero,\n temos apenas uma raiz: {x1:.2f}")
             elif Delta > 0:
                 ValorBhaskara.configure(text=f"Como delta é maior que zero,\n temos duas raizes: {x1:.2f} e {x2:.2f}")
             else:
                  ValorBhaskara.configure(text=f"Como delta é menor a zero,\n não temos raizes!")
         except ValueError:
             pass
    BotaoResolverBhaskara = ctk.CTkButton(MenuBhaskara, width=100, height=75, text="Calcular", bg_color="#222222", fg_color="#0058CC", command=ResolverBhaskara, border_color="black", border_width=4)
    BotaoResolverBhaskara.place(x=105, y=200)



def Potenciacao():
    MenuContas.forget()
    MenuPotenciacao = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuPotenciacao.pack(padx=5 ,pady=15)
    EntradaPotenciacao = ctk.CTkEntry(MenuPotenciacao, width=200,height=50, placeholder_text="Digite o exponte...", bg_color="#222222")
    EntradaPotenciacao.place(x=65, y=75)
    ValorTotalPotenciacao = ctk.CTkLabel(MenuPotenciacao, text=f"O Resultado é igual à: \n{TotalPotenciacao}", font=("arial", 20, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalPotenciacao.place(x=50, y=250)
    ValorPotenciacao = ctk.CTkEntry(MenuPotenciacao, width=200,height=50, placeholder_text="Digite o valor da base...", bg_color="#222222")
    ValorPotenciacao.place(x=65, y=10)
    def Potencializar():
         global TotalPotenciacao
         try:
             ValorEntradaPotenciacao = int(EntradaPotenciacao.get())
             ValorInicialPotenciacao = int(ValorPotenciacao.get())
             TotalPotenciacao = ValorInicialPotenciacao ** ValorEntradaPotenciacao
             EntradaPotenciacao.delete(0,"end")
             ValorPotenciacao.delete(0,"end")
             ValorTotalPotenciacao.configure(text=f"O Resultado é igual à: \n{TotalPotenciacao}")
         except ValueError:
             pass
    BotaoPotencializar = ctk.CTkButton(MenuPotenciacao, width=100, height=75, text="Potencializar Valor", bg_color="#222222", fg_color="#0058CC", command=Potencializar, border_color="black", border_width=4)
    BotaoPotencializar.place(x=105, y=150)



def RaizQuadrada():
    MenuContas.forget()
    MenuRaizQuadrada = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuRaizQuadrada.pack(padx=5 ,pady=15)
    ValorTotalRaizQuadrada = ctk.CTkLabel(MenuRaizQuadrada, text=f"O Resultado é igual à: \n{TotalPotenciacao}", font=("arial", 20, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalRaizQuadrada.place(x=10, y=250)
    ValorInicialRaizQuadrada = ctk.CTkEntry(MenuRaizQuadrada, width=220,height=50, placeholder_text="Digite o valor para calcular...", bg_color="#222222")
    ValorInicialRaizQuadrada.place(x=65, y=10)
    def CalcularRaizQuadrada():
         global TotalRaizQuadrada
         try:
             ValorEntradaRaizQuadrada = int(ValorInicialRaizQuadrada.get())
             TotalRaizQuadrada = ValorEntradaRaizQuadrada ** 0.5
             ValorInicialRaizQuadrada.delete(0,"end")
             ValorTotalRaizQuadrada.configure(text=f"O Resultado é igual à: \n{TotalRaizQuadrada:.2f}")
         except ValueError:
             pass
    BotaoCalcularRaizQuadrada = ctk.CTkButton(MenuRaizQuadrada, width=100, height=75, text="Calcular raiz quadrada", bg_color="#222222", fg_color="#0058CC", command=CalcularRaizQuadrada, border_color="black", border_width=4)
    BotaoCalcularRaizQuadrada.place(x=100, y=150)


def Porcentagem():
    MenuContas.forget()
    MenuPorcentagem = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuPorcentagem.pack(padx=5 ,pady=15)
    EntradaPorcentagem = ctk.CTkEntry(MenuPorcentagem, width=200,height=50, placeholder_text="Digite o valor a se calcular...", bg_color="#222222")
    EntradaPorcentagem.place(x=65, y=75)
    ValorTotalPorcentagem = ctk.CTkLabel(MenuPorcentagem, text=f"O Resultado é igual à: {TotalPorcentagem}", font=("arial", 20, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalPorcentagem.place(x=10, y=250)
    ValorPorcentagem = ctk.CTkEntry(MenuPorcentagem, width=200,height=50, placeholder_text="Digite o valor da porcentagem...", bg_color="#222222")
    ValorPorcentagem.place(x=65, y=10)
    def CalcularPorcentagem():
         global TotalPorcentagem
         try:
             ValorEntradaPorcentagem = float(EntradaPorcentagem.get())
             ValorInicialPorcentagem = float(ValorPorcentagem.get())
             TotalPorcentagem = ValorEntradaPorcentagem * ValorInicialPorcentagem / 100
             EntradaPorcentagem.delete(0,"end")
             ValorPorcentagem.delete(0,"end")
             ValorTotalPorcentagem.configure(text=f"{ValorInicialPorcentagem}% de {ValorEntradaPorcentagem} é igual a\n{TotalPorcentagem:.1f}")
         except ValueError:
             pass
    BotaoCalcularPorcentagem = ctk.CTkButton(MenuPorcentagem, width=100, height=75, text="Potencializar Valor", bg_color="#222222", fg_color="#0058CC", command=CalcularPorcentagem, border_color="black", border_width=4)
    BotaoCalcularPorcentagem.place(x=105, y=150)


def Fatorial():
    MenuContas.forget()
    MenuFatorial = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuFatorial.pack(padx=5 ,pady=15)
    ValorTotalFatorial = ctk.CTkLabel(MenuFatorial, text=f"<digite um valor>! é igual à: \n{TotalFatorial}", font=("arial", 20, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalFatorial.place(x=5, y=250)
    ValorInicialFatorial = ctk.CTkEntry(MenuFatorial, width=220,height=50, placeholder_text="Digite o valor para calcular...", bg_color="#222222")
    ValorInicialFatorial.place(x=65, y=10)
    def CalcularFatorial():
         global TotalFatorial
         try:
             ValorEntradaFatorial = int(ValorInicialFatorial.get())
             TotalFatorial = math.factorial(ValorEntradaFatorial)
             ValorInicialFatorial.delete(0,"end")
             ValorTotalFatorial.configure(text=f"{ValorEntradaFatorial}! é igual à: \n{TotalFatorial}")
         except ValueError:
              ValorTotalFatorial.configure(text=f"Digite um valor valido!")
    BotaoCalcularFatorial = ctk.CTkButton(MenuFatorial, width=100, height=75, text="Calcular fatorial", bg_color="#222222", fg_color="#0058CC", command=CalcularFatorial, border_color="black", border_width=4)
    BotaoCalcularFatorial.place(x=100, y=150)

def Hipotenusa():
    MenuContas.forget()
    MenuHipotenusa = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuHipotenusa.pack(padx=5 ,pady=15)
    EntradaHipotenusa = ctk.CTkEntry(MenuHipotenusa, width=200,height=50, placeholder_text="Digite o outro valor...", bg_color="#222222")
    EntradaHipotenusa.place(x=65, y=75)
    ValorTotalHipotenusa = ctk.CTkLabel(MenuHipotenusa, text=f"O valor da hipotenusa é igual à: \n{TotalHipotenusa:.2f}", font=("arial", 17, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalHipotenusa.place(x=10, y=250)
    ValorHipotenusa = ctk.CTkEntry(MenuHipotenusa, width=200,height=50, placeholder_text="Digite um valor para calcular...", bg_color="#222222")
    ValorHipotenusa.place(x=65, y=10)
    def CalcularHipotenusa():
         global TotalHipotenusa
         try:
             ValorEntradaHipotenusa = int(EntradaHipotenusa.get())
             ValorInicialHipotenusa = int(ValorHipotenusa.get())
             TotalHipotenusa = math.hypot(ValorEntradaHipotenusa, ValorInicialHipotenusa)
             EntradaHipotenusa.delete(0,"end")
             ValorHipotenusa.delete(0,"end")
             ValorTotalHipotenusa.configure(text=f"O valor da hipotenusa é igual à: \n{TotalHipotenusa:.2f}")
         except ValueError:
             pass
    BotaoCalcularHipotenusa = ctk.CTkButton(MenuHipotenusa, width=100, height=75, text="Calcular Hipotenusa", bg_color="#222222", fg_color="#0058CC", command=CalcularHipotenusa, border_color="black", border_width=4)
    BotaoCalcularHipotenusa.place(x=105, y=150)

def IMC():
    MenuContas.forget()
    MenuIMC = ctk.CTkFrame(app, width=600, height=425, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
    MenuIMC.pack(padx=5 ,pady=15)
    EntradaIMC = ctk.CTkEntry(MenuIMC, width=250,height=50, placeholder_text="Digite o seu peso para calcular (KG)...", bg_color="#222222")
    EntradaIMC.place(x=50, y=75)
    ValorTotalIMC = ctk.CTkLabel(MenuIMC, text=f"O seu I.M.C é igual à: {TotalIMC:.2f}", font=("arial", 17, "bold"), bg_color="#222222",fg_color="transparent")
    ValorTotalIMC.place(x=10, y=250)
    ValorIMC = ctk.CTkEntry(MenuIMC, width=250,height=50, placeholder_text="Digite sua altura para calcular(M)...", bg_color="#222222")
    ValorIMC.place(x=50, y=10)
    def CalcularIMC():
         global TotalIMC
         try:
             ValorPesoIMC = float(EntradaIMC.get())
             ValorAlturaIMC = float(ValorIMC.get())
             TotalIMC = ValorPesoIMC / (ValorAlturaIMC ** 2)
             EntradaIMC.delete(0,"end")
             ValorIMC.delete(0,"end")
             ValorTotalIMC.configure(text=f"O seu I.M.C é igual à: {TotalIMC:.2f}")
         except ValueError:
             pass
    BotaoCalcularIMC = ctk.CTkButton(MenuIMC, width=100, height=75, text="Calcular Indice de Massa Corporal", bg_color="#222222", fg_color="#0058CC", command=CalcularIMC, border_color="black", border_width=4)
    BotaoCalcularIMC.place(x=60, y=150)

def MenuOperaçao():
     MenuContas.pack(padx=5 ,pady=15)
     BotaoAdiçao = ctk.CTkButton(MenuContas, width=100, height=100, text="Adição", bg_color="#222222", fg_color="#0058CC", command=Adiçao, border_color="black", border_width=4)
     BotaoAdiçao.place(x=5, y=10)
     BotaoSubtração = ctk.CTkButton(MenuContas, width=100, height=100, text="Subtração", bg_color="#222222", fg_color="#0058CC", command=Subtração, border_color="black", border_width=4)
     BotaoSubtração.place(x=115, y=10)
     BotaoMultiplicaçao = ctk.CTkButton(MenuContas, width=100, height=100, text="Multiplicaçao", bg_color="#222222", fg_color="#0058CC", command=Multiplicaçao, border_color="black", border_width=4)
     BotaoMultiplicaçao.place(x=225, y=10)
     BotaoDivisao = ctk.CTkButton(MenuContas, width=100, height=100, text="Divisão", bg_color="#222222", fg_color="#0058CC", command=Divisao, border_color="black", border_width=4)
     BotaoDivisao.place(x=5, y=120)
     BotaoAleatoriedade = ctk.CTkButton(MenuContas, width=100, height=100, text="Aleatoriedade", bg_color="#222222", fg_color="#0058CC", command=Aleatoriedade, border_color="black", border_width=4)
     BotaoAleatoriedade.place(x=115, y=120)
     BotaoBhaskara = ctk.CTkButton(MenuContas, width=100, height=100, text="Bhaskara", bg_color="#222222", fg_color="#0058CC", command=Bhaskara, border_color="black", border_width=4)
     BotaoBhaskara.place(x=225, y=120)
     BotaoPotenciacao = ctk.CTkButton(MenuContas, width=100, height=100, text="Potenciação", bg_color="#222222", fg_color="#0058CC", command=Potenciacao, border_color="black", border_width=4)
     BotaoPotenciacao.place(x=5, y=230)
     BotaoRaizQuadrada = ctk.CTkButton(MenuContas, width=100, height=100, text="Raiz Quadrada", bg_color="#222222", fg_color="#0058CC", command=RaizQuadrada, border_color="black", border_width=4)
     BotaoRaizQuadrada.place(x=115, y=230)
     BotaoPorcentagem = ctk.CTkButton(MenuContas, width=100, height=100, text="Porcentagem", bg_color="#222222", fg_color="#0058CC", command=Porcentagem, border_color="black", border_width=4)
     BotaoPorcentagem.place(x=225, y=230)
     BotaoFatorial = ctk.CTkButton(MenuContas, width=100, height=100, text="Fatorial", bg_color="#222222", fg_color="#0058CC", command=Fatorial, border_color="black", border_width=4)
     BotaoFatorial.place(x=5, y=340)
     BotaoHipotenusa = ctk.CTkButton(MenuContas, width=100, height=100, text="Hipotenusa", bg_color="#222222", fg_color="#0058CC", command=Hipotenusa, border_color="black", border_width=4)
     BotaoHipotenusa.place(x=115, y=340)
     BotaoIMC = ctk.CTkButton(MenuContas, width=100, height=100, text="I.M.C", bg_color="#222222", fg_color="#0058CC", command=IMC, border_color="black", border_width=4)
     BotaoIMC.place(x=225, y=340)

MenuOperaçao()
app.mainloop()
