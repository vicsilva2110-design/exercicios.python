# ==========================================
# MÓDULOS DE PROCESSAMENTO (def)
# ==========================================
def calcular_bonus(salario):
    """Calcula o bônus padrão de 15% da ArkeTech"""
    return salario * 0.15

# ==========================================
# INTERFACE DO SISTEMA
# ==========================================
print("==========================================")
print("        RH ARKETECH - BÔNUS INICIAL       ")
print(("==========================================\n"))

while True:
   print("\n--- NOVO REGISTRO ---")

   # O .strip() remove espaços em brancos digitados sem querer
   nome = input("Nome completo (ou digite '0' para sair): ")

   if nome == '0':
       print("\n👋 Encerrando o painel de bônus. Bom trabalho!")
       break

    # Blindagem 1: Impede que o nome fique em branco se o usuario so apertar "enter"

    if not nome:
        print("  ERRO: O campo de nome não pode ficar vazio. ")
        continue 

    cargo = input("cargo contratado: ").strip()

    # Blindagem 2: a zona de perigo (tratamento de exeções)
    try:
        salario_base = float(input("salario base (use ponto. ex 1500.00) R$ "))

        # Blindagem 3: Regra de negocio (não existe salario negativo ou zero)
        if salario_base <+ 0:
            print("\n ERRO LOGISTICO: o salario deve ser maior que zero. tente novamente. ")
