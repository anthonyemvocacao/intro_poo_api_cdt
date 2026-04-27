def aula_tratamento_erros():
    print("--- Desafio 1: Divisao ---")
    try:
        numerador = int(input("Digite o numerador "))    
        denominador = int(input("digite o denominador: "))
        resultado = numerador / denominador
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")
    except ZeroDivisionError:
        print("Erro: não podes dividir por zero.")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    else:
        print(f"Sucesso! Resultado: {resultado}")
    finally:
        print("--- fim da divisão ---")
        aula_tratamento_erros()