from sympy import *
import numpy as np
import matplotlib.pyplot as plt

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

GraphStyles = [u'seaborn-darkgrid',
			   u'seaborn-notebook', 
			   u'classic', 
			   u'seaborn-ticks', 
			   u'grayscale',
			   u'bmh',
			   u'seaborn-talk', 
			   u'dark_background', 
			   u'ggplot', 
			   u'fivethirtyeight', 
			   u'_classic_test', 
			   u'seaborn-colorblind', 
			   u'seaborn-deep',
			   u'seaborn-whitegrid', 
			   u'seaborn-bright', 
			   u'seaborn-poster', 
			   u'seaborn-muted', 
			   u'seaborn-paper', 
			   u'seaborn-white', 
			   u'seaborn-pastel', 
			   u'seaborn-dark', 
			   u'seaborn', 
			   u'seaborn-dark-palette'
			   ]

class LinhaDeOperacao:
	def __init__(self, CaixaLinha, Indice, NomeLinha, Input, Input2, Input3, Input4, Operacoes, Output):
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
				self.Input2.resize("21", "fill")

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

	def CalculaLinha(self, MF):
		MEMFILENAMES = open("Recursos\MemoriaNomes.txt", "r")
		MEMFILEADRESS = open("Recursos\MemoriaEnderecos.txt", "r")
		MEMFILEINPUTS = open("Recursos\MemoriaInputs.txt", "r")
		MemoriaTemporaria = [MEMFILENAMES.read().split("\n"), MEMFILEADRESS.read().split("\n"),
							 MEMFILEINPUTS.read().split("\n")]
		MEMFILENAMES.close()
		MEMFILEADRESS.close()
		MEMFILEINPUTS.close()

		def ParseInput(STRING):
			import LISTA
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
						A = ParseInput(self.Input.value)
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
						self.Input.value = "(Símbolo da variável)"
					else:
						try:
							self.Funcao = eval(A)
							self.Endereco = "MF[" + self.Indice + "]"
							self.Output.value = str(self.Funcao)
							self.Latex = latex(self.Funcao)
						except:
							self.Output.value = "ERRO"

				if self.Operacoes.value == "Expressão":
					if self.Input.value == "ajuda":
						self.Input.value = "(Símbolo da variável)"
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


class PainelGrafico:
	def __init__(self, INDEX):
		self.Indice = str(INDEX)
		self.NomeGrafico = "Graph" + str(INDEX) + ".png"
		self.LimEsquerdo = 0
		self.LimDireito = 0

		def PrintGraph(self):pass
	