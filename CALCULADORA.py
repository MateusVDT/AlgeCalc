from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from sympy.plotting import plot
from guizero import *
import LISTA
MF = []

ListaDeOperacoes = ["Variável Contínua",
					"Variável Discreta",
					"Var. Cont. ≥0",
					"Var. Disc. ≥0",
					"Var. Cont. >0",
					"Var. Disc. >0",
					"----------------",
					"Função Implícita",
					"Expressão",
					"Equação",
					"Numerizar",
					"Isolar ℝ",
					"Isolar ℂ",
					"EDO",
					"Substituir",
					"----------------",
					"Integral",
					"Derivada",
					"----------------",
					"Somatório",
					"Transf. Laplace",
					"Transf. Inv. Laplace",
					"----------------",
					"Latex"
					]

def ParseInput(STRING):
	MEMFILENAMES = open("Recursos\MemoriaNomes.txt", "r")
	MEMFILEADRESS = open("Recursos\MemoriaEnderecos.txt", "r")
	MEMFILEINPUTS = open("Recursos\MemoriaInputs.txt", "r")
	MemoriaTemporaria = [MEMFILENAMES.read().split("\n"),
					  MEMFILEADRESS.read().split("\n"),
					  MEMFILEINPUTS.read().split("\n")]
	MEMFILENAMES.close()
	MEMFILEADRESS.close()
	MEMFILEINPUTS.close()

	EXPRESSION = str(STRING)
	for i in range(0, len(LISTA.Value)):
		EXPRESSION = EXPRESSION.replace(LISTA.Value[i][0], LISTA.Value[i][1])
	for i in range(0, len(MemoriaTemporaria[0])):
		try:
			EXPRESSION = EXPRESSION.replace(MemoriaTemporaria[0][i], MemoriaTemporaria[1][i])
		except:
			pass
	for i in range(0, len(LISTA.Value)):
		EXPRESSION = EXPRESSION.replace(LISTA.Value[i][1], LISTA.Value[i][0])
	return EXPRESSION

class LinhaDeOperacao:
	def __init__( self, CaixaLinha, Indice, NomeLinha, Input, Input2, Input3, Input4, Operacoes, Output):
		self.CaixaLinha = CaixaLinha
		self.Indice = str(Indice)
		self.NomeLinha = NomeLinha
		self.Input = Input
		self.Input2 = Input2
		self.Input3 = Input3
		self.Input4 = Input4
		self.Operacoes = Operacoes
		self.Output = Output
		self.Funcao = 0
		self.Endereco = ""
		self.Latex = ""

	def AtualizaCaixa(self):
		def InputChange(N):
			if N == 1:
				self.Input.resize("fill", "fill")
				self.Input2.visible = 0
				self.Input3.visible = 0
				self.Input4.visible = 0

			elif N == 2:
				self.Input2.visible = 1
				self.Input3.visible = 0
				self.Input4.visible = 0
				self.Input2.resize(5, "fill")
				self.Input.resize("fill", "fill")
 
			elif N == 3:
				self.Input2.visible = 1
				self.Input3.visible = 1
				self.Input4.visible = 0
				self.Input2.resize(5, "fill")
				self.Input.resize("fill", "fill")

			elif N == 4:
				self.Input2.visible = 1
				self.Input3.visible = 1
				self.Input4.visible = 1
				self.Input2.resize(5, "fill")
				self.Input.resize("fill", "fill")


			elif N == "EQ":
				self.Input2.visible = 1
				self.Input3.visible = 0
				self.Input4.visible = 0
				self.Input.resize("fill", "fill")
				self.Input2.resize(20, "fill")

		if self.Operacoes.value == "Variável Contínua":
			InputChange(1)
		elif self.Operacoes.value == "Variável Discreta":
			InputChange(1)
		elif self.Operacoes.value == "Função Implícita":
 			InputChange(2)
		elif self.Operacoes.value == "Var. Cont. ≥0":
			InputChange(1)
		elif self.Operacoes.value == "Var. Disc. ≥0":
			InputChange(1)
		elif self.Operacoes.value == "Var. Cont. >0":
			InputChange(1)
		elif self.Operacoes.value == "Var. Disc. >0":
			InputChange(1)
		elif self.Operacoes.value == "Expressão":
			InputChange(1)
		elif self.Operacoes.value == "Equação":
			InputChange("EQ")
		elif self.Operacoes.value == "Numerizar":
			InputChange(1)
		elif self.Operacoes.value == "Integral":
			InputChange(4)
		elif self.Operacoes.value == "Derivada":
			InputChange(3)
		elif self.Operacoes.value == "Isolar ℝ":
			InputChange(2)
		elif self.Operacoes.value == "Isolar ℂ":
			InputChange(2)
		elif self.Operacoes.value == "Somatório":
			InputChange(4)
		elif self.Operacoes.value == "Transf. Laplace":
			InputChange(3)
		elif self.Operacoes.value == "Transf. Inv. Laplace":
 			InputChange(3)
		elif self.Operacoes.value == "EDO":
			InputChange(2)
		elif self.Operacoes.value == "Latex":
			InputChange(1)
		elif self.Operacoes.value == "Substituir":
			InputChange(3)

	def Eq2PNG(self):
		try:
			fig = plt.figure()
			if self.Latex != "":
				fig.text(0.5, 0.5, r'$' + self.Latex + r'$', ha='center', va='center', size=20)
			else:
				fig.text(0.5, 0.5,"", ha='center', va='center', size=20)
			plt.savefig("Recursos\\" + str(self.NomeLinha.value) + ".png", bbox_inches='tight')
			plt.close(fig)
		except:
			pass

	def CalculaLinha(self, MemoriaExterna):
		global MF
		MF = MemoriaExterna

		def SymbolException(STRING):
			import LISTA
			STRING = str(STRING)
			for i in range(0, len(LISTA.Value)):
				if LISTA.Value[i][0] == STRING:
					return '⟶ERRORCODE00'
			return ""

		def ArmazenaArquivo():
			MEMFILENAMES = open("Recursos\MemoriaNomes.txt", "a")
			MEMFILEADRESS = open("Recursos\MemoriaEnderecos.txt", "a")
			MEMFILEINPUTS = open("Recursos\MemoriaInputs.txt", "a")
			MEMFILENAMES.write(str(self.NomeLinha.value) + "\n")
			MEMFILEADRESS.write(str(self.Endereco) + "\n")
			MEMFILEINPUTS.write(
				str(self.Input.value) + ";" + str(self.Input2.value) + ";" + str(self.Input3.value) + ";" + str(
					self.Input4.value) + "\n")
			MEMFILENAMES.close()
			MEMFILEADRESS.close()
			MEMFILEINPUTS.close()

		if self.Input.value != "":
			if self.Operacoes.value == "Variável Contínua":
				if SymbolException(self.Input.value) == "":
					if self.Input.value == "ajuda":
						self.Input.value = "(Símbolo da variável)"
					else:
						self.Funcao = Symbol(self.Input.value)
						self.NomeLinha.value = str(self.Input.value)
						self.Endereco = "MF[" + self.Indice + "]"
						self.Output.value = "Variável contínua " + str(self.Input.value)
						self.Latex = r'\left\{' + self.Input.value + r'\in\mathbb{C}\right\}'
				else:
					self.Input.value = "VARIAVEL PROIBIDA"

			elif self.Operacoes.value == "Variável Discreta":
				if SymbolException(self.Input.value) == "":
					if self.Input.value == "ajuda":
						self.Input.value = "(Símbolo da variável)"
					else:
						self.Funcao = Symbol(self.Input.value, integer=True)
						self.NomeLinha.value = str(self.Input.value)
						self.Endereco = "MF[" + self.Indice + "]"
						self.Output.value = "Variável discreta " + str(self.Input.value)
				else:
					self.Input.value = "VARIAVEL PROIBIDA"

			elif self.Operacoes.value == "Função Implícita":
				if SymbolException(self.Input.value) == "":
					if self.Input.value == "ajuda":
						self.Input.value = "(Símbolo da função)"
						self.Input2.value = "(Var)"
					else:
						A = self.Input.value
						B = ParseInput(self.Input2.value)
						self.Funcao = eval('Function("' + A + '")(' + B + ")")
						self.NomeLinha.value = str(self.Input.value)
						self.Endereco = "MF[" + self.Indice + "]"
						self.Output.value = "Função Implícita " + self.Input.value + "(" + self.Input2.value + ")"
				else:
 					self.Input.value = "FUNÇÃO PROIBIDA"

			elif self.Operacoes.value == "Var. Cont. ≥0":
				if SymbolException(self.Input.value) == "":
					if self.Input.value == "ajuda":
						self.Input.value = "(Símbolo da variável)"
					else:
						self.Funcao = Symbol(self.Input.value, positive=True)
						self.NomeLinha.value = str(self.Input.value)
						self.Endereco = "MF[" + self.Indice + "]"
						self.Output.value = "Variável contínua " + str(self.Input.value)
				else:
					self.Input.value = "VARIAVEL PROIBIDA"

			elif self.Operacoes.value == "Var. Disc. ≥0":
				if SymbolException(self.Input.value) == "":
					if self.Input.value == "ajuda":
						self.Input.value = "(Símbolo da variável)"
					else:
						self.Funcao = Symbol(self.Input.value, integer=True, positive=True)
						self.NomeLinha.value = str(self.Input.value)
						self.Endereco = "MF[" + self.Indice + "]"
						self.Output.value = "Variável discreta " + str(self.Input.value)
				else:
					self.Input.value = "VARIAVEL PROIBIDA"

			elif self.Operacoes.value == "Var. Cont. >0":
				if SymbolException(self.Input.value) == "":
					if self.Input.value == "ajuda":
						self.Input.value = "(Símbolo da variável)"
					else:
						self.Funcao = Symbol(self.Input.value, positive=True, nonzero=True)
						self.NomeLinha.value = str(self.Input.value)
						self.Endereco = "MF[" + self.Indice + "]"
						self.Output.value = "Variável contínua " + str(self.Input.value)
				else:
					self.Input.value = "VARIAVEL PROIBIDA"

			elif self.Operacoes.value == "Var. Disc. >0":
				if SymbolException(self.Input.value) == "":
					if self.Input.value == "ajuda":
						self.Input.value = "(Símbolo da variável)"
					else:
						self.Funcao = Symbol(self.Input.value, integer=True, positive=True, nonzero=True)
						self.NomeLinha.value = str(self.Input.value)
						self.Endereco = "MF[" + self.Indice + "]"
						self.Output.value = "Variável discreta " + str(self.Input.value)
				else:
					self.Input.value = "VARIAVEL PROIBIDA"

			else:
				A = ParseInput(self.Input.value)
				B = ParseInput(self.Input2.value)
				C = ParseInput(self.Input3.value)
				D = ParseInput(self.Input4.value)

				if self.Operacoes.value == "Expressão":
					if self.Input.value == "ajuda":
						self.Input.value = "(Digite a expressão)"
					else:
						try:
							self.Funcao = eval(A)
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Equação":
					if self.Input.value == "ajuda":
						self.Input.value = "(Expressão1)"
						self.Input2.value = "(Expressão2)"
					else:
						try:
							self.Funcao = eval("Eq(" + A + "," + B + ")")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Numerizar":
					if self.Input.value == "ajuda":
						self.Input.value = "(Expressão)"
					else:
						try:
							self.Funcao = eval("N(" + A + ")")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Integral":
					if self.Input.value == "ajuda":
						self.Input.value = "(Expressão)"
						self.Input2.value = "(Var)"
						self.Input3.value = "Lim-"
						self.Input4.value = "Lim+"
					else:
						try:
							if C == "":
								self.Funcao = eval("integrate(" + A + "," + B + ")")
							else:
								self.Funcao = eval("integrate(" + A + ",(" + B + "," + C + "," + D + "))")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Derivada":
					if self.Input.value == "ajuda":
						self.Input.value = "(Expressão)"
						self.Input2.value = "(Var)"
						self.Input3.value = "Ordem"
					else:
						try:
							if C == "":
								self.Funcao = eval("diff(" + A + "," + B + ")")
							else:
								self.Funcao = eval("diff(" + A + "," + B + "," + C + ")")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Isolar ℝ":
					if self.Input.value == "ajuda":
						self.Input.value = "(Equação ou Expressão)"
						self.Input2.value = "(Var)"
					else:
						try:
							self.Funcao = eval("solveset(" + A + "," + B + ", domain=S.Reals)")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"
  
				if self.Operacoes.value == "Isolar ℂ":
					if self.Input.value == "ajuda":
						self.Input.value = "(Equação ou Expressão)"
						self.Input2.value = "(Var)"
					else:
						try:
							self.Funcao = eval("solveset(" + A + "," + B + ")")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Somatório":
					if self.Input.value == "ajuda":
						self.Input.value = "(Expressão)"
						self.Input2.value = "(Var)"
						self.Input3.value = "Lim-"
						self.Input4.value = "Lim+"
					else:
						try:
							if C == "":
								self.Funcao = eval("summation(" + A + "," + B + ")")
							else:
								self.Funcao = eval("summation(" + A + ",(" + B + "," + C + "," + D + "))")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Transf. Laplace":
					if self.Input.value == "ajuda":
						self.Input.value = "(Expressão)"
						self.Input.value2 = "(Var1)"
						self.Input.value3 = "(Var2)"

					else:
						try:
							self.Funcao = eval("laplace_transform(" + A + "," + B + "," + C + ")[0]")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Transf. Inv. Laplace":
					if self.Input.value == "ajuda":
						self.Input.value = "(Expressão)"
						self.Input.value2 = "(Var1)"
						self.Input.value3 = "(Var2)"
					else:
						try:
							self.Funcao = eval("inverse_laplace_transform(" + A + "," + B + "," + C + ")")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "EDO":
					if self.Input.value == "ajuda":
						self.Input.value = "(Equação)"
						self.Input2.value = "(Fun)"
					else:
						try:
							self.Funcao = eval("dsolve(" + A + "," + B + ")")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"
							
				if self.Operacoes.value == "Substituir":
					if self.Input.value == "ajuda":
						self.Input.value = "(Expressão ou Eq.)"
						self.Input2.value = "(ExpA)"
						self.Input3.value = "(ExpB)"
					else:
						try:
							self.Funcao = eval(A + ".subs(" + B + "," + C + ")")
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Latex":
					if self.Input.value == "ajuda":
						self.Input.value = "(Expressão)"
					else:
						self.Funcao = latex(eval(A))
						self.Endereco = "MF[" + self.Indice + "]"
						self.Output.value = str(self.Funcao)
						self.Latex = self.Funcao
		else:
			self.Output.value = "Input Vazio"
		ArmazenaArquivo()



class LinhaGrafica2D:
	def __init__(self, BoxLinha, ExpOpt, CorOpt, EspOpt, EstOpt):
		self.BoxLinha = BoxLinha
		self.ExpOpt = ExpOpt
		self.CorOpt = CorOpt
		self.EspOpt = EspOpt
		self.EstOpt = EstOpt
		self.CONTADOR = 1
		
	def Update(self, LISTADEEXPRESSOES):
		self.ExpOpt.clear()
		self.CONTADOR = 1
		self.ExpOpt.append("Nenhuma")
		for i in range(0, len(LISTADEEXPRESSOES)):
			self.ExpOpt.append(LISTADEEXPRESSOES[i])
			self.CONTADOR = self.CONTADOR+1 
	
class PainelGrafico2D:
	def __init__(self, Grafico, OpcoesDeVariaveis, LimiteEsquerdo, LimiteDireito, INDEX, AreaLinhas, AreaGrafico, DPI):
		
		self.Indice = str(INDEX)
		self.NomeGrafico = "Grafico" + str(INDEX) + ".png"
		self.CaixaGrafico = Grafico
		self.OpcoesDeVariaveis = OpcoesDeVariaveis
		self.LimiteEsquerdo = LimiteEsquerdo
		self.LimiteDireito = LimiteDireito
		self.INDEX = INDEX
		self.AreaLinhas = AreaLinhas
		self.ListaLinhas = []
		self.AreaGrafico = AreaGrafico
		self.GraficoEmSi = 0
		self.DPI = DPI
		
	def CriaLinha(self):
		self.AreaLinhas.resize("fill", self.AreaLinhas.height+25)
		NovaLinha = Box(self.AreaLinhas, align="top", height=25, width="fill")
		Text(NovaLinha, text="Expressão:", align="left")
		OpcoesDeExpressao = Combo(NovaLinha, options=["Nenhuma"], align="left", height="fill", width=7)
		Text(NovaLinha, text="Cor:0x", align="left")
		OpcoesDeCor = TextBox(NovaLinha, width=6, height="fill", align="left")
		OpcoesDeCor.value = "FF0000"
		Text(NovaLinha, text="Espessura:", align="left")
		OpcoesDeEspessura = Combo(NovaLinha, options=["1","2","3","4","5","6","7","8"], align="left", height="fill")
		Text(NovaLinha, text="Estilo:", align="left")
		OpcoesDeEstilo = Combo(NovaLinha, options=['-', '--', '-.', ':'], align="left", height="fill", width=2)
		self.ListaLinhas.append(LinhaGrafica2D(NovaLinha,OpcoesDeExpressao,OpcoesDeCor,OpcoesDeEspessura,OpcoesDeEstilo))
		
		
	def Update(self, EXPRESSOES, VARIAVEIS):
		self.OpcoesDeVariaveis.clear()
		self.OpcoesDeVariaveis.append("Nenhuma")
		for i in range(0, len(VARIAVEIS)):
			self.OpcoesDeVariaveis.append(VARIAVEIS[i])
		for i in range(0, len(self.ListaLinhas)):
			self.ListaLinhas[i].Update(EXPRESSOES)

	def RenderGraf(self):
		if self.OpcoesDeVariaveis.value != "Nenhuma":
			var = eval(ParseInput(self.OpcoesDeVariaveis.value))
			for i in range(0,len(self.ListaLinhas)):
				if self.ListaLinhas[i].ExpOpt.value != "Nenhuma":
					tempfun = eval(ParseInput(self.ListaLinhas[i].ExpOpt.value))
					Color = []
					Color.append(float.fromhex(self.ListaLinhas[i].CorOpt.value[2:3]))
					Color.append(float.fromhex(self.ListaLinhas[i].CorOpt.value[2:3]))
					Color.append(float.fromhex(self.ListaLinhas[i].CorOpt.value[4:5]))
					if i == 0:
						Grafico = plot(tempfun, (var, self.LimiteEsquerdo.value, self.LimiteDireito.value), show=False)
					else:
						Linha = plot(tempfun, (var, self.LimiteEsquerdo.value, self.LimiteDireito.value), show=False)
						Linha.color = var, (Color[0])
						Grafico.extend(Linha)
			backend = Grafico.backend(Grafico)
			backend.process_series()
			backend.fig.savefig("Recursos\\" + self.NomeGrafico, dpi=int(self.DPI.value))
			if self.GraficoEmSi !=0:
				self.GraficoEmSi.destroy()
				self.GraficoEmSi =0
			self.GraficoEmSi = Picture(self.AreaGrafico, "Recursos\\" + self.NomeGrafico)
		else:
			if self.GraficoEmSi !=0:
				self.GraficoEmSi.destroy()
				self.GraficoEmSi =0
			
