# Classe Aluno
class Aluno:
    def __init__(self, nome, turma, nota):
        self.nome = nome
        self.turma = turma
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome}, Turma: {self.turma}, Nota: {self.nota}"

# Instanciando dois alunos
aluno1 = Aluno("João", "1º Ano", 8.5)
aluno2 = Aluno("Maria", "2º Ano", 9.0)

# Imprimindo os dados dos alunos
print(aluno1)
print(aluno2)

# Classe Produto
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total_em_estoque(self):
        return self.preco * self.quantidade

# Instanciando dois produtos
produto1 = Produto("Caderno", 15.50, 30)
produto2 = Produto("Caneta", 3.00, 100)

# Exibindo o valor total em estoque
valor_total = produto1.valor_total_em_estoque() + produto2.valor_total_em_estoque()
print(f"Valor total em estoque: R${valor_total:.2f}")
