# 📘 Sistema de Cadastro de Alunos e Responsáveis

Este projeto é um **CRUD completo** para gerenciar **alunos** e seus **respectivos responsáveis**, permitindo realizar operações como cadastrar, listar, editar e excluir registros de maneira prática e organizada.

A aplicação foi desenvolvida com foco em simplicidade, eficiência e escalabilidade, permitindo que escolas, cursos e instituições realizem o controle básico de alunos de forma rápida.

---

## 🚀 Funcionalidades

* 👦 **Cadastro de Alunos**: Adicione novos alunos com informações pessoais e acadêmicas.
* 👨‍👩‍👦 **Cadastro de Responsáveis**: Registre responsáveis vinculados aos alunos.
* 🔄 **Edição de Registros**: Atualize dados de alunos e responsáveis.
* ❌ **Exclusão de Registros**: Remova alunos ou responsáveis individualmente.
* 📋 **Listagem Completa**: Exiba todos os alunos e visualize seus responsáveis associados.
* 🔗 **Relacionamento Aluno ↔ Responsável**: Cada aluno pode ter um ou mais responsáveis cadastrados.
* 🗂️ **Organização Intuitiva**: Interface clara para navegação e manipulação dos dados.

---

## 🛠️ Tecnologias Utilizadas

* **Banco de Dados**: MySQL com o pymysql
* **Python**: POO e integração ao Banco de Dados

---

## 🔧 Configuração do Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/ArthurEnzol/CadAluno.git
   ```

2. **Instale as dependências:**

   ```bash
   pip install pymysql
   ```

3. **Arquivo `.env` já incluso:**
   Você **não precisa criar apenas editar** o `.env`. Ele já está anexado no projeto.
   Basta editar o necessário e seguir os próximos passos

5. **Inicie o servidor:**

   ````bash
   py view.py
   ```:**

---

## 📚 Funcionalidades do CRUD

### 👦 Alunos

* Criar aluno
* Editar aluno
* Listar alunos
* Excluir aluno
* Relacionar alunos aos seus responsáveis

### 👨‍👩‍👦 Responsáveis

* Criar responsável
* Editar responsável
* Listar responsáveis
* Excluir responsável
* Associar a um ou mais alunos

---

## 📌 Estrutura do Projeto

* `/CadAluno`

  * `/.env` — Definição das crendenciais
  * `/controller` — Lógica principal das operações
  * `/dal` — Lógica entre o banco de dados e o python
  * `/model` — Criação dos modelos de cada elemento
  * `/view` — Executa a parte visual no terminal

---

## ✨ Autor

Desenvolvido por **Arthur Enzol** — Sinta-se livre para contribuir!

