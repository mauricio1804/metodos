import os
import math

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def avaliar_expressao(expr, x):
    substituicoes = {
        '^': '**', 'e': 'math.e', 'cos': 'math.cos', 'sin': 'math.sin', 'tan': 'math.tan',
        'log': 'math.log10', 'ln': 'math.log', 'exp': 'math.exp', 'sqrt': 'math.sqrt',
        'sec': '(1/math.cos)', 'csc': '(1/math.sin)', 'cot': '(1/math.tan)',
        'asin': 'math.asin', 'acos': 'math.acos', 'atan': 'math.atan',
        'asec': '(1/math.acos)', 'acsc': '(1/math.asin)', 'acot': '(1/math.atan)'
    }

    for antigo, novo in substituicoes.items():
        expr = expr.replace(antigo, novo)

    try:
        return eval(expr)
    except Exception as e:
        raise ValueError(f"Erro ao avaliar expressão: {e}")

def metodo_bisseccao(funcao, a, b, precisao, max_iter):
    """Executa o método da bisseção."""
    k = 0
    if funcao(a) * funcao(b) >= 0:
        print("O método de bisseção falhou. Verifique os limites.")
        return

    while abs(b - a) > precisao and k < max_iter:
        k += 1
        meio = (a + b) / 2
        f_meio = funcao(meio)

        if funcao(a) * f_meio < 0:
            b = meio
        else:
            a = meio

    raiz = (a + b) / 2
    print(f"Raiz aproximada: {raiz}, Iterações: {k}")

def metodo_regula_falsi(funcao, a, b, max_iter, precisao):
    """Executa o método de Regula Falsi."""
    if funcao(a) * funcao(b) >= 0:
        print("O método de Regula Falsi falhou. Verifique os limites.")
        return

    for k in range(max_iter):
        x = a - (funcao(a) * (b - a)) / (funcao(b) - funcao(a))

        if abs(funcao(x)) < precisao or abs(b - a) < precisao:
            print(f"Raiz aproximada: {x}, Iterações: {k + 1}")
            return

        if funcao(a) * funcao(x) > 0:
            a = x
        else:
            b = x

    print(f"Raiz aproximada: {x}, Iterações: {max_iter}")

def metodo_newton(funcao, derivada, x0, precisao, max_iter):
    """Executa o método de Newton."""
    for k in range(max_iter):
        fx = funcao(x0)
        fx_linha = derivada(x0)

        if fx_linha == 0:
            print("Derivada zero, não pode continuar.")
            return

        x1 = x0 - fx / fx_linha

        if abs(funcao(x1)) < precisao:
            print(f"Raiz aproximada: {x1}, Iterações: {k + 1}")
            return

        x0 = x1

    print(f"Raiz aproximada: {x0}, Iterações: {max_iter}")

def metodo_secante(funcao, x0, x1, precisao, max_iter):
    """Executa o método da Secante."""
    for k in range(max_iter):
        f0, f1 = funcao(x0), funcao(x1)

        if f1 - f0 == 0:
            print("Divisão por zero, não pode continuar.")
            return

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        if abs(funcao(x2)) < precisao:
            print(f"Raiz aproximada: {x2}, Iterações: {k + 1}")
            return

        x0, x1 = x1, x2

    print(f"Raiz aproximada: {x1}, Iterações: {max_iter}")

def metodo_iterativo(funcao, phi, x0, precisao, max_iter):
    """Executa o método iterativo."""
    for k in range(max_iter):
        x1 = phi(x0)

        if abs(funcao(x1)) < precisao:
            print(f"Raiz aproximada: {x1}, Iterações: {k + 1}")
            return

        x0 = x1

    print(f"Raiz aproximada: {x0}, Iterações: {max_iter}")

def selecionar_metodo():
    """Menu de seleção de método."""
    metodos = {
        '1': metodo_bisseccao,
        '2': metodo_regula_falsi,
        '3': metodo_newton,
        '4': metodo_secante,
        '5': metodo_iterativo,
    }

    clear_terminal()
    print("Escolha o método:")
    for k, v in metodos.items():
        print(f"{k}. {v.__name__.replace('metodo_', '').capitalize()}")
    print("6. Sair")

    return input("Digite o número do método desejado: ")

def main():
    while True:
        escolha = selecionar_metodo()

        if escolha == '6':
            print("Saindo do programa...")
            break

        if escolha not in {'1', '2', '3', '4', '5'}:
            print("Escolha inválida. Tente novamente.")
            continue

        funcao_str = input("Digite a expressão da função (use 'x' como variável): ")
        funcao = lambda x: avaliar_expressao(funcao_str, x)

        if escolha == '1':
            a, b = float(input("Limite inferior (a): ")), float(input("Limite superior (b): "))
            precisao = float(input("Precisão (δ): "))
            max_iter = int(input("Máx. iterações: "))
            metodo_bisseccao(funcao, a, b, precisao, max_iter)

        elif escolha == '2':
            a, b = float(input("Limite inferior (a): ")), float(input("Limite superior (b): "))
            precisao = float(input("Precisão (δ): "))
            max_iter = int(input("Máx. iterações: "))
            metodo_regula_falsi(funcao, a, b, max_iter, precisao)

        elif escolha == '3':
            derivada_str = input("Digite a derivada da função: ")
            derivada = lambda x: avaliar_expressao(derivada_str, x)
            x0 = float(input("Valor inicial (x0): "))
            precisao = float(input("Precisão (δ): "))
            max_iter = int(input("Máx. iterações: "))
            metodo_newton(funcao, derivada, x0, precisao, max_iter)

        elif escolha == '4':
            x0, x1 = float(input("x0: ")), float(input("x1: "))
            precisao = float(input("Precisão (δ): "))
            max_iter = int(input("Máx. iterações: "))
            metodo_secante(funcao, x0, x1, precisao, max_iter)

        elif escolha == '5':
            phi_str = input("Função de iteração: ")
            phi = lambda x: avaliar_expressao(phi_str, x)
            x0 = float(input("Valor inicial (x0): "))
            precisao = float(input("Precisão (δ): "))
            max_iter = int(input("Máx. iterações: "))
            metodo_iterativo(funcao, phi, x0, precisao, max_iter)

        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
