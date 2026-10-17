"""
TaskTracker - Sistema de Gerenciamento de Tarefas (CLI)
Aluno: Claudio Simões Pereira Miglio de Melo
Curso: Ciência de Dados e Machine Learning
"""

# Lista global para armazenar as tarefas cadastradas
tarefas = []

def validar_titulo() -> str:
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: O título da tarefa não pode ser vazio. Tente novamente.")

def validar_prioridade() -> str:
    prioridades_validas = {
        "ALTA": "Alta",
        "MEDIA": "Média",
        "MÉDIA": "Média",
        "BAIXA": "Baixa"
    }
    
    while True:
        prioridade = input("Digite a prioridade (Alta, Média, Baixa): ").strip().upper()
        if prioridade in prioridades_validas:
            return prioridades_validas[prioridade]
        print("Erro: Prioridade inválida! Escolha estritamente entre Alta, Média ou Baixa.")

def cadastrar_tarefa():
    print("CADASTRO DE NOVA TAREFA")
    
    titulo = validar_titulo()
    descricao = input("Digite a descrição da tarefa: ").strip()
    prioridade = validar_prioridade()
    data_limite = input("Digite a data limite (opcional, ex: DD/MM/AAAA): ").strip()
    
    if not data_limite:
        data_limite = "Não informada"

    tarefa = {
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")

def visualizar_tarefas():
    print("\n--- LISTA DE TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for i, t in enumerate(tarefas, start=1):
        print(f"Tarefa #{i}")
        print(f"  • Título:      {t['titulo']}")
        print(f"  • Descrição:   {t['descricao']}")
        print(f"  • Prioridade:  {t['prioridade']}")
        print(f"  • Data Limite: {t['data_limite']}")
        print(f"  • Status:      {t['status']}")
        print("-" * 35)
    print()

def menu():
    while True:
        print("TASKTRACKER - MENU")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        
        opcao = input("Escolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker.")
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 3.")

if __name__ == "__main__":
    menu()