#DECLARANDO A CLASS PAI - PESSOA
class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


#DECLARANDO A CLASS FILHA DE PESSOA - Aluno
class Aluno(Pessoa):
    def __init__(self, nome = None, idade = None, matricula = None, curso = None):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    #lista de cursos
cursos = ['nada','Engenharia', 'Medicina', 'Direito', 'Arquitetura']


#DECLARANDO A CLASS FILHA DE PESSOA - Funcionario
class Funcionario(Pessoa):
    def __init__(self, nome = None, idade = None, setor = None, salario = None):
        super().__init__(nome, idade)
        self.setor = setor
        self.salario = salario

    #lista de setores
setores = ['nada','Secretaria Escolar', 'Setor Pedagógico', 'Setor Administrativo/Financeiro', 'Outros Setores: Limpeza, portaria, biblioteca, cozinha e coordenação']


#INÍCIO DO PROGRAMA PRINCIPAL
contador = 0

while contador == 0:

    AouF = input("Você é aluno ou funcionário? Digite (A ou F): ").upper()
    if AouF == 'A':
        print("\n Bem-vindo aluno! \n")
        matricula = input("Digite sua matrícula: ")
        curso = int(input("Escolha seu curso entre as opções a seguir:\n" +
                  "1. Engenharia\n" +
                  "2. Medicina\n" +
                  "3. Direito\n" +
                  "4. Arquitetura\n"))
        
        if curso <= 0 or curso > 4:
            print("Opção inválida de curso.")
            
        else:
            print("\n Matrícula e curso registrados com sucesso! \n")

            print("Você escolheu o curso: " + cursos[curso])
            print(f"Sua matrícula é: {matricula}")
            contador += 1

            A = Aluno(nome, idade, matricula, curso)
    
    
    elif AouF == 'F':
        print("\n Bem-vindo funcionário! \n")

        salario = float(input("Digite seu salário: R$ "))
        setor = int(input("Digite seu setor de atuação entre as opções a seguir:\n" +
                  "1. Secretaria Escolar\n" +
                  "2. Setor Pedagógico\n" +
                  "3. Setor Administrativo/Financeiro\n" +
                  "4. Outros Setores: Limpeza, portaria, biblioteca, cozinha e coordenação\n"))
        
        if setor <= 0 or setor > 4:
            print("Opção inválida de setor.")
        
        else:
            print("Você escolheu o setor: " + setores[setor])
            print("O seu salário é: R$ " + str(salario))
            contador += 1

            F = Funcionario(nome, idade, setor, salario)


P = Pessoa(nome, idade)
print(P.apresentar())