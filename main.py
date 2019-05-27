from guizero import *
from CALCULADORA import LinhaDeOperacao, ListaDeOperacoes, PainelGrafico2D

#Classe memória contém as variáveis da memória da calculadora
class Memoria:
	def __init__(self):
		self.Linha = []
		self.Grafico = []
		self.ContadorLinhas = 0
		self.ContadorGraficos = 0
		self.PaginasFuncionais = 0
		self.PaginasGraficas   = 0
		self.FuncoesAnteriores= []
		self.ListaVariaveis = []
		self.NomeFuncoes = []

	def LimpaMemoria(self):
		MEMFILEADRESS = open("Recursos\MemoriaEnderecos.txt", "w")
		MEMFILENAMES = open("Recursos\MemoriaNomes.txt", "w")
		MEMFILEOUTPUTS = open("Recursos\MemoriaInputs.txt", "w")
		MEMFILEADRESS.close()
		MEMFILENAMES.close()
		MEMFILEOUTPUTS.close()
		self.NomeFuncoes = []
		OpcoesDeEquacoes.clear()
		OpcoesDeEquacoes.append("Nenhuma")
		self.FuncoesAnteriores = []
		self.ListaVariaveis = []
		for i in range(0, self.ContadorLinhas):
			self.Linha[i].Output.value = ""
			self.Linha[i].NomeLinha.value = "M"+self.Linha[i].Indice
			self.Linha[i].Funcao = 0
			self.Linha[i].Endereco = ""
			self.Linha[i].Latex = ""

	def ReiniciaTudo(self):
		self.LimpaMemoria()
		for i in range(0, M.ContadorLinhas):
			self.Linha[i].CaixaLinha.destroy()
		self.Linha.clear()
		self.ContadorLinhas = 0
		PrimeiraPaginaFuncional()
		NovaLinha()

	def CalculaTudo(self):
		self.LimpaMemoria()
		for i in range(0, self.ContadorLinhas):
			self.Linha[i].CalculaLinha(self.FuncoesAnteriores)
			self.FuncoesAnteriores.append(self.Linha[i].Funcao)
			if self.Linha[i].Operacoes.value in ["Variável Contínua","Variável Discreta","Var. Cont. ≥0","Var. Disc. ≥0","Var. Cont. >0","Var. Disc. >0"]:
				self.ListaVariaveis.append(self.Linha[i].NomeLinha.value)
			self.NomeFuncoes.append(self.Linha[i].NomeLinha.value)
			OpcoesDeEquacoes.append(self.Linha[i].NomeLinha.value)
		self.UpdateConteudoGrafico()
			
	def AtualizaInputs(self):
		for i in range(0, self.ContadorLinhas):
			self.Linha[i].AtualizaCaixa()

	def MudaPaginaFuncional(self):
		for i in range(0, self.ContadorLinhas):
			self.Linha[i].CaixaLinha.visible = False
		for i in range(self.PaginasFuncionais*15, self.PaginasFuncionais*15+15):
			if i < self.ContadorLinhas:
				self.Linha[i].CaixaLinha.visible = True

	def MudaPaginaGrafica(self):
		for i in range(0, self.ContadorGraficos):
			self.Grafico[i].CaixaGrafico.visible = False
		if self.PaginasGraficas != self.ContadorGraficos:
			self.Grafico[self.PaginasGraficas].CaixaGrafico.visible = True
	
	def UpdateConteudoGrafico(self):
		if self.ContadorGraficos != 0:
			for j in range(0, self.ContadorGraficos):
				self.Grafico[j].Update(self.NomeFuncoes, self.ListaVariaveis)
		

M = Memoria()

##Inicia uma nova janela
MainWindow = App(layout="auto", title="AlgeCalc BETA 0.12", width=800, height=600)
MainWindow.tk.iconbitmap('favicon.ico')


##Interface do módulo funcional
ModuloFuncional = Box(MainWindow, align="top", layout="auto", height="fill", width="fill")

#interface do módulo gráfico, oculto por padrão
ModuloGrafico = Box(MainWindow, align="top", layout="auto", height="fill", width="fill")
ModuloGrafico.visible=False

#Barra de opções do módulo funcional
BarraFuncional = Box(ModuloFuncional, align="top", layout="auto", height=30, width="fill")
PushButton(BarraFuncional, text="Calcula", align="left", command=M.CalculaTudo)
def NovaLinha():
	Indice = M.ContadorLinhas
	CaixaLinha = Box(AreaDeLinhas, align="top", layout="auto", height=25, width="fill")
	NomeLinha = Text(CaixaLinha, text="M" + str(Indice), width="7", align="left")
	OpcoesDeOperacao = Combo(CaixaLinha, options=ListaDeOperacoes, align="left", height="fill", width=15,
							 command=M.AtualizaInputs)
	ContainerInput = Box(CaixaLinha, align="left", layout="auto", height=25, width=250)
	CaixaDeInput4 = TextBox(ContainerInput, width=5, height="fill", align="right")
	CaixaDeInput3 = TextBox(ContainerInput, width=5, height="fill", align="right")
	CaixaDeInput2 = TextBox(ContainerInput, width=5, height="fill", align="right")
	CaixaDeInput  = TextBox(ContainerInput, width="fill", height="fill", align="right")
	CaixaDeInput2.visible = False
	CaixaDeInput3.visible = False
	CaixaDeInput4.visible = False
	Text(CaixaLinha, text="⟶", width="2", align="left")
	CaixaDeOutput = TextBox(CaixaLinha, text="", align="left", width="fill", height="fill")
	M.Linha.append(
		LinhaDeOperacao(
				CaixaLinha, Indice, NomeLinha, CaixaDeInput, CaixaDeInput2,
				 CaixaDeInput3, CaixaDeInput4, OpcoesDeOperacao, CaixaDeOutput
		)
	)
	M.ContadorLinhas = M.ContadorLinhas + 1

PushButton(BarraFuncional, text="Nova Linha", align="left", command=NovaLinha)
PushButton(BarraFuncional, text="RESET", align="left", command=M.ReiniciaTudo)
def HabilitaGraficos():
	ModuloFuncional.visible = False
	ModuloGrafico.visible = True
	M.UpdateConteudoGrafico()
BotaoGrafico = PushButton(BarraFuncional, width=16, text="Módulo Gráfico", align="right", command=HabilitaGraficos)
def ProximaPaginaFuncional():
	if  M.ContadorLinhas > (M.PaginasFuncionais+1)*15-1:
		M.PaginasFuncionais = M.PaginasFuncionais + 1
	M.MudaPaginaFuncional()
	MostradorPaginaFuncional.value="Pág." + str(M.PaginasFuncionais)
PushButton(BarraFuncional, text="→", align="right", command=ProximaPaginaFuncional)
def AnteriorPaginaFuncional():
	if M.PaginasFuncionais > 0:
		M.PaginasFuncionais = M.PaginasFuncionais - 1
	M.MudaPaginaFuncional()
	MostradorPaginaFuncional.value="Pág." + str(M.PaginasFuncionais)
MostradorPaginaFuncional = Text(BarraFuncional, text="Pág.0", align="right")
PushButton(BarraFuncional, text="←", align="right", command=AnteriorPaginaFuncional)
def PrimeiraPaginaFuncional():
	M.PaginasFuncionais = 0
	M.MudaPaginaFuncional()
	MostradorPaginaFuncional.value="Pág." + str(M.PaginasFuncionais)
PushButton(BarraFuncional, text="←←", align="right", command=PrimeiraPaginaFuncional)

#Área onde as linhas de memória são exibidas
AreaDeLinhas = Box(ModuloFuncional, align="top", layout="auto", height=375, width="fill")

#Barra de opções de equações renderizadas
BarraEquacoes = Box(ModuloFuncional, align="top", layout="auto", height=25, width="fill")
Text(BarraEquacoes, text="Exibir:", align="left")

ImagemDaEquacao = 0
def AualizaImagemEQ(NOME):
	global ImagemDaEquacao
	if(ImagemDaEquacao!=0):
		try: ImagemDaEquacao.destroy()
		except:pass
	if NOME != "Nenhuma":
		global M
		OPTS = [[],[]]
		for i in range(0,M.ContadorLinhas):
			OPTS[0].append(M.Linha[i].NomeLinha.value)
			OPTS[1].append(M.Linha[i].Latex)
		M.Linha[OPTS[0].index(NOME)].Eq2PNG()
		try:
			ImagemDaEquacao=Picture(AreaDeEquacoes, "Recursos\\"+NOME+".png")
		except:
			pass

OpcoesDeEquacoes = Combo(BarraEquacoes, options=["Nenhuma"], align="left", height="fill", width=15, command=AualizaImagemEQ)

#Área onde as equações serão renderizadas
AreaDeEquacoes = Box(ModuloFuncional, align="top", layout="auto", border=1, height="fill", width="fill")
AreaDeEquacoes.bg = "white"	

#Código do Módulo  gráfico
BarraGrafica = Box(ModuloGrafico, align="top", layout="auto", height=30, width="fill")
def NovoGrafico2D():
	if M.PaginasGraficas == M.ContadorGraficos:
		INDEX = M.ContadorGraficos
		Grafico = Box(ModuloGrafico, align="top", layout="auto", height="fill", width="fill")
		BarraDeConfigs = Box(Grafico, align="top", layout="auto", height=25, width="fill")
		NovaLinhaBox = Box(BarraDeConfigs, align="left", layout="auto", height="fill", width=155)
		Text(BarraDeConfigs, text="Eixo Horizontal:", align="left")
		OpcoesDeEixo = Combo(BarraDeConfigs, options=["Nenhuma"], align="left", height="fill")
		Text(BarraDeConfigs, text="Lim Esquerdo:", align="left")
		LimiteEsquerdo = TextBox(BarraDeConfigs, text="-5", width=5, height="fill", align="left")
		Text(BarraDeConfigs, text="Lim Direito:", align="left")
		LimiteDireito = TextBox(BarraDeConfigs, text="5", width=5, height="fill", align="left")
		Text(BarraDeConfigs, text="DPI:", align="left")
		DPI = TextBox(BarraDeConfigs, text="90", width=5, height="fill", align="left")
		AreaLinhas = Box(Grafico, align="top", layout="auto", height=1, width="fill")
		AreaGrafico = Box(Grafico, align="top", layout="auto", border=1, height="fill", width="fill")
		AreaGrafico.bg = "white"
		M.Grafico.append(PainelGrafico2D(Grafico, OpcoesDeEixo, LimiteEsquerdo, LimiteDireito, INDEX, AreaLinhas, AreaGrafico, DPI))
		def NovaLinha(A):
			M.Grafico[A].CriaLinha()
			M.UpdateConteudoGrafico()
		PushButton(NovaLinhaBox, text="Nova Linha", align="left", command=NovaLinha, args=[INDEX])
		PushButton(NovaLinhaBox, text="Renderizar", align="left", command=M.Grafico[INDEX].RenderGraf)
		M.ContadorGraficos = M.ContadorGraficos+1
	
PushButton(BarraGrafica, text="Plot 2D", align="left", command=NovoGrafico2D)
PushButton(BarraGrafica, text="Plot 3D", align="left", enabled=False)
PushButton(BarraGrafica, text="Animação 2D", align="left", enabled=False)
PushButton(BarraGrafica, text="Animação 3D", align="left", enabled=False)

def HabilitaFuncional():
	ModuloFuncional.visible = True
	ModuloGrafico.visible = False
BotaoFuncional = PushButton(BarraGrafica, width=16 ,text="Módulo Funcional", align="right", command=HabilitaFuncional)
def ProximaPaginaGrafico():
	if  M.ContadorGraficos > (M.PaginasGraficas):
		M.PaginasGraficas = M.PaginasGraficas + 1
	MostradorPaginaGrafica.value="Gráfico " + str(M.PaginasGraficas)
	M.MudaPaginaGrafica()
	M.UpdateConteudoGrafico()
PushButton(BarraGrafica, text="→", align="right", command=ProximaPaginaGrafico)
MostradorPaginaGrafica = Text(BarraGrafica, text="Gráfico 0", align="right")
def AnteriorPaginaGrafico():
	if M.PaginasGraficas > 0:
		M.PaginasGraficas = M.PaginasGraficas - 1
	M.MudaPaginaGrafica()
	MostradorPaginaGrafica.value="Gráfico " + str(M.PaginasGraficas)
	M.UpdateConteudoGrafico()
PushButton(BarraGrafica, text="←", align="right", command=AnteriorPaginaGrafico)
def PrimeiraPaginaGrafica():
	M.PaginasGraficas = 0
	MostradorPaginaGrafica.value="Gráfico " + str(M.PaginasGraficas)
	M.MudaPaginaGrafica()
	M.UpdateConteudoGrafico()
PushButton(BarraGrafica, text="←←", align="right", command=PrimeiraPaginaGrafica)

#Cria uma linha de memória e abre a janela principal
NovaLinha()
MainWindow.display()
