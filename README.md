# 📚 Sistema de Gerenciamento de Biblioteca Terminal

Este projeto é uma aplicação de terminal em Python desenvolvida como trabalho final da disciplina. 
O sistema simula o gerenciamento de uma biblioteca, 
integrando conceitos fundamentais de programação e Programação Orientada a Objetos (POO).

---

## 👥 Integrantes do Grupo

* Integrante 1
* Integrante 2
* Integrante 3
* Integrante 4
* Integrante 5
* Integrante 6

---

## 🛠️ Funcionalidades e Conceitos Aplicados

O projeto foi dividido em blocos funcionais para demonstrar o domínio dos seguintes tópicos:

* **Bloco 1:** Variáveis, tipos de dados, `type()`, conversão de tipos (`int`) e `f-strings`.
* **Bloco 2:** Operadores aritméticos, de comparação, lógicos (`and`), `abs()` e verificações de identidade (`is` / `is not`).
* **Bloco 3:** Manipulação de listas (`append`), medição de tamanho (`len`) e busca (`in`).
* **Bloco 4:** Estruturas de repetição (`for`, `while`) e sequência de números (`range()`).
* **Bloco 5 (POO):** Abstração, encapsulamento (atributos protegidos), herança e polimorfismo com as classes `Livro`, `LivroDigital`, `Usuario` e `Emprestimo`.
* **Bloco 6:** Funções com parâmetros, uso de dicionários e interatividade via `input()`.

---

## 📐 Diagrama Simples de Classes

```text
       +-------------------+
       |       Livro       |
       +-------------------+
       | - titulo: str     |
       | - _autor: str     |
       +-------------------+
                 ^
                 |  (Herança)
       +-------------------+
       |   LivroDigital    |
       +-------------------+
       | - formato: str    |
       +-------------------+

 +-------------------+       +-------------------+
 |      Usuario      |       |    Emprestimo     |
 +-------------------+       +-------------------+
 | - nome: str       | <---->| - usuario: obj    |
 | - matricula: str  |       | - livro: obj      |
 +-------------------+       +-------------------+
