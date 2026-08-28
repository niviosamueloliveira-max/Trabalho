# ==========================================
# BLOCO 1: Variáveis, Tipos de Dados e Funções Básicas
# ==========================================

# Comentário explicativo
print("=== BLOCO 1: Variáveis e Tipos ===")
nome_biblioteca = "Biblioteca Municipal"  # Variável String
quantidade_livros = 12                  # Variável Inteiro
sistema_online = True                   # Variável Booleana

# Uso de type() e conversão de tipos
print("Tipo da variável quantidade:", type(quantidade_livros))
ano_texto = "2026"
ano_numero = int(ano_texto)  # Conversão de string para int
print(f"Ano convertido (f-string): {ano_numero}")


# ==========================================
# BLOCO 2: Operadores, abs() e Validações Lógicas
# ==========================================

print("\n=== BLOCO 2: Operadores e abs() ===")
meta_anual = 20
diferenca_meta = abs(quantidade_livros - meta_anual)  # Função abs()
print(f"Faltam {diferenca_meta} livros para atingir a meta.")

# Operadores de comparação, lógicos e de identidade (is / is not)
if quantidade_livros > 10 and sistema_online is True:
    print("Status: O sistema está operacional e com bom acervo.")

verificador = None
if verificador is not True:
    print("Verificação de identidade (is not) passou com sucesso.")


# ==========================================
# BLOCO 3: Estruturas de Dados (Listas)
# ==========================================

print("\n=== BLOCO 3: Manipulação de Listas ===")
generos_livros = ["Terror", "Ação", "Aventura"]

# append() e len()
generos_livros.append("Romance")
print(f"Total de gêneros cadastrados: {len(generos_livros)}")

# Operador in / not in
if "Terror" in generos_livros:
    print("O gênero Terror está disponível na lista.")

# Exemplo de pop() (opcional para remoção)
# genero_removido = generos_livros.pop()


# ==========================================
# BLOCO 4: Loops, range() e Estruturas de Repetição
# ==========================================

print("\n=== BLOCO 4: Loops e Range ===")
print("Listando índices e gêneros com for e range:")
for i in range(len(generos_livros)):
    print(f"- Posição [{i}]: {generos_livros[i]}")

# Loop while
contador = 1
print("Contagem regressiva de inicialização:")
while contador <= 2:
    print(f"Carregando sistema... {contador}")
    contador += 1


# ==========================================
# BLOCO 5: Programação Orientada a Objetos (POO)
# (Classes, Objetos, Abstração, Encapsulamento, Herança e Polimorfismo)
# ==========================================

print("\n=== BLOCO 5: POO ===")

# Classe Mãe (Demonstra Abstração e Encapsulamento com atributo protegido _autor)
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self._autor = autor  # Atributo protegido

    def exibir_info(self):
        return f"Livro: '{self.titulo}', Autor: {self._autor}"

# Classe Filha (Demonstra Herança)
class LivroDigital(Livro):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato

    # Polimorfismo (sobrescrevendo o método da classe pai)
    def exibir_info(self):
        base = super().exibir_info()
        return f"{base} [Formato Digital: {self.formato}]"

# Criando Objetos
livro_fisico = Livro("O Chamado de Cthulhu", "H.P. Lovecraft")
livro_eletronico = LivroDigital("Senhor dos Anéis", "J.R.R. Tolkien", "PDF")

print(livro_fisico.exibir_info())
print(livro_eletronico.exibir_info())


# ==========================================
# BLOCO 6: Funções com Parâmetros e Condicionais com input()
# ==========================================

print("\n=== BLOCO 6: Funções e Interação ===")

# Função com parâmetros
def cumprimentar_usuario(nome):
    return f"Olá, {nome}! Bem-vindo à busca de livros."

print(cumprimentar_usuario("Leitor"))

# Dicionário simples simulando a busca
genero_map = {
    "terror": [livro_fisico.titulo],
    "aventura": [livro_eletronico.titulo]
}

# input() e condicionais if / elif / else
escolha_usuario = input("Qual gênero você busca (terror ou aventura)? ").strip().lower()

if escolha_usuario in genero_map:
    print(f"Livros encontrados no gênero '{escolha_usuario}': {genero_map[escolha_usuario]}")
elif escolha_usuario == "":
    print("Atenção: Você não digitou nada.")
else:
    print("Gênero não encontrado em nossa base de dados.")
