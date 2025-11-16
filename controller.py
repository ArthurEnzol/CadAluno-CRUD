from colorama import init, Fore, Back, Style
from dal import view_student_dall, view_responsable_dall, save_student_dall, save_responsable_dall, delete_student_dall, delete_responsable_dall, update_student_dall, update_responsable_dall
from model import Student, Responsable
from datetime import date, datetime


def view_responsable_string(responsable):
    try:
        return (
            f"\n📘 Cadastro do Aluno\n"
            f"🆔 ID: {responsable['id']}\n"
            f"👤 Nome: {responsable['username']}\n"
            f"🎂 Idade: {responsable['age']} anos\n"
            f"🏫 Escola: {responsable['school']}\n"
            f"📚 Série: {responsable['grade']}º ano\n"
        )
    except Exception as e:
        return f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m"


def save_student_controller(username, age, school, grade):
    try:
        student = Student(
            username=username,
            age=age,
            school=school,
            grade=grade,
            id_=None
        )
        save_student_dall(student)
    except Exception as e:
        return f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m"

def delete_student_controller(username, age, school, grade):
    try:
        student = Student(
            username=username,
            age=age,
            school=school,
            grade=grade,
            id_=None
        )
        delete_student_dall(student)
    except Exception as e:
        return f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m"

def update_student_controller(username, age, school, grade, id_):
    try:
        student = Student(
            username=username,
            age=age,
            school=school,
            grade=grade,
            id_=id_
        )
        update_student_dall(student)
    except Exception as e:
        return f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m"

def view_student_controller():
    try:
        name = input(Fore.MAGENTA + "\nDigite o nome do Aluno -> ")
        result = view_student_dall(name)
        return (
            f"\n📘 Cadastro do Aluno\n"
            f"🆔 ID: {result[0]['id']}\n"
            f"👤 Nome: {result[0]['username']}\n"
            f"🎂 Idade: {result[0]['age']} anos\n"
            f"🏫 Escola: {result[0]['school']}\n"
            f"📚 Série: {result[0]['grade']}º ano\n"
        )
    except Exception as e:
        return f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m"

def save_responsable_controller(number, name, pay, pay_day: datetime, children):
    try:
        responsable = Responsable(
            number=number,
            name=name,
            pay=pay,
            pay_day=pay_day,
            children=children,
            id_=None
        )
        save_responsable_dall(responsable)
    except Exception as e:
        return f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m"

def delete_responsable_controller(number, name, pay, pay_day:datetime, children):
    try:
        responsable = Responsable(
            number=number,
            name=name,
            pay=pay,
            pay_day=pay_day,
            children=children,
            id_=None
        )
        delete_responsable_dall(responsable)
    except Exception as e:
        return f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m"

def update_responsable_controller(number, name, pay, pay_day: date, children, id_):
    try:
        responsable = Responsable(
            number=number,
            name=name,
            pay=pay,
            pay_day=pay_day,
            children=children,
            id_=id_
        )
        update_responsable_dall(responsable)
    except Exception as e:
        return f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m"

def view_responsable_controller():
    try:
        name = input(Fore.MAGENTA + "\nDigite o nome do Responsável -> ")
        result = view_responsable_dall(name)
        return (
            f"\n📘 Cadastro do Aluno\n"
            f"🆔 ID: {result[0]['id']}\n"
            f"👤 Nome: {result[0]['username']}\n"
            f"🎂 Idade: {result[0]['age']} anos\n"
            f"🏫 Escola: {result[0]['school']}\n"
            f"📚 Série: {result[0]['grade']}º ano\n"
        )
    except Exception as e:
        return f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m"

init(autoreset=True)


def show_menu():
    try:
        print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "\n🔷 BEM-VINDO AO SISTEMA 🔷\n")
        print(Fore.GREEN + "1️⃣ Criar cadastro")
        print(Fore.RED + "2️⃣ Deletar cadastro")
        print(Fore.YELLOW + "3️⃣ Ver cadastros")
        print(Fore.CYAN + "4️⃣ Editar/Atualizar cadastro")
        option = int(input(Fore.MAGENTA + "\nEscolha uma opção digitando o número correspondente -> "))
        return option
    except Exception as e:
        print(f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m")
        exit()


def registration_menu():
    try:
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + "\n📋 MENU DE CADASTRO 📋\n")
        print(Fore.BLUE + "1️⃣ Cadastrar Aluno")
        print(Fore.LIGHTBLUE_EX + "2️⃣ Cadastrar Responsável")
        choice = int(input(Fore.MAGENTA + "\nEscolha o tipo de cadastro -> "))
        return choice
    except Exception as e:
        print(f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m")
        exit()

def update_menu():
    try:
        print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "\n🆕 MENU DE ATUALIZAÇÃO 🆕\n")
        print(Fore.BLUE + "1️⃣ Atualizar Alunos")
        print(Fore.LIGHTBLUE_EX + "2️⃣ Atualizar Responsáveis")
        choice = int(input(Fore.MAGENTA + "\nEscolha o tipo de atualização -> "))
        return choice
    except Exception as e:
        print(f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m")
        exit()

def view_menu() :
    try:
        print(Back.YELLOW + Fore.BLACK + Style.BRIGHT + "\n🔍 MENU DE VISUALIZAÇÃO 🔍\n")
        print(Fore.BLUE + "1️⃣ Ver Alunos")
        print(Fore.LIGHTBLUE_EX + "2️⃣ Ver Responsáveis")
        choice = int(input(Fore.MAGENTA + "\nEscolha o tipo de visualização -> "))
        return choice
    except Exception as e:
        print(f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m")
        exit()

def delete_menu() :
    try:
        print(Back.RED + Fore.WHITE + Style.BRIGHT + "\n🗑️ MENU DE EXCLUSÃO 🗑️\n")
        print(Fore.BLUE + "1️⃣ Deletar Aluno")
        print(Fore.LIGHTBLUE_EX + "2️⃣ Deletar Responsável")
        choice = int(input(Fore.MAGENTA + "\nEscolha o tipo de exclusão -> "))
        return choice
    except Exception as e:
        print(f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m")
        exit()

def collect_delete_data():
    try:
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + "\n📋 REMOVER ALUNO 📋\n")
        full_name = input(Fore.CYAN + "👤 Nome completo do aluno: ")
        return full_name
    except Exception as e:
        print(f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m")
        exit()


def collect_student_data():
    try:
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + "\n📋 CADASTRO DE ALUNO 📋\n")
        id_ = input(Fore.CYAN + "👤 ID do aluno: ")
        full_name = input(Fore.CYAN + "👤 Nome completo do aluno: ")
        age = input(Fore.YELLOW + "🎂 Idade: ")
        school = input(Fore.BLUE + "🏫 Nome da escola: ")
        grade = int(input(Fore.MAGENTA + "📚 Série/Ano escolar (Apenas Número): "))

        print(Fore.GREEN + "\n✅ Dados coletados com sucesso!\n")

        return {
            "username": full_name,
            "age": age,
            "school": school,
            "grade": grade,
            "id": id_
        }

    except Exception as e:
        print(Fore.RED + f"❌ Algo de errado aconteceu não foi possível fazer o cadastro. {e}")
        return None


def collect_responsable_data():

    try:
        print(Back.LIGHTBLUE_EX + Fore.BLACK + Style.BRIGHT + "\n📋 CADASTRO DE RESPONSÁVEL 📋\n")
        id_ = input(Fore.CYAN + "👤 ID do responsável: ")
        full_name = input(Fore.CYAN + "👤 Nome completo do responsável: ")
        phone_number = input(Fore.YELLOW + "📞 Número de telefone: ")
        children_name = input(Fore.BLUE + "🧒 Nome da criança: ")
        has_paid = input(Fore.GREEN + "💰 Já realizou o pagamento? (s/n): ").strip().lower()

        if has_paid == "s" :
            payment_date_str = input(Fore.MAGENTA + "📅 Data do pagamento (DD/MM/AAAA): ")
            payment_date = datetime.strptime(payment_date_str, "%d/%m/%Y").date()
        else :
            payment_date = None

        print(Fore.GREEN + "\n✅ Dados do responsável coletados com sucesso!\n")

        return {
            "full_name" : full_name,
            "phone_number" : phone_number,
            "has_paid" : has_paid,
            "payment_date" : payment_date,
            "children_name" : children_name,
            "id": id_
        }
    except Exception as e:
        print(Fore.RED + f"❌ Algo de errado aconteceu não foi possível fazer o cadastro. {e}")
        return None

def save():
    try:
        x = input(Fore.CYAN + "💾 Deseja salvar este cadastro agora? Digite 's' para confirmar ou 'n' para cancelar -> ".strip().lower())
        if x == "n" or "s":
            return x
        else:
            print(f"❌ Algo de errado aconteceu, digite corretamente.")
            return None
    except Exception as e:
        print(f"\033[91m⚠️ Ops! Ocorreu algum erro: {e}\033[0m")
        exit()