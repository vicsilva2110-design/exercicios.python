# ==========================================
# SISTEMA INTEGRADO ARKETECH - 14 EXERCÍCIOS
# ==========================================
 
print("=== 1. Onboarding de Colaboradores ===")
nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")
print(f"Bem-vindo(a) ao sistema da ArkeTech, {nome}! Seu cargo é {cargo}.\n")
 
 
print("=== 2. Cálculo de Horas Extras ===")
valor_hora = float(input("Digite o valor da hora de trabalho (R$): "))
horas_extras = float(input("Digite a quantidade de horas extras trabalhadas: "))
total_pagar = valor_hora * horas_extras
print(f"O valor total a ser pago por horas extras é: R$ {total_pagar:.2f}\n")
 
 
print("=== 3. Reembolso Corporativo ===")
transporte = float(input("Digite o valor do transporte: "))
alimentacao = float(input("Digite o valor da alimentação: "))
hospedagem = float(input("Digite o valor da hospedagem: "))
total_reembolso = transporte + alimentacao + hospedagem
print(f"O valor final do reembolso é: R$ {total_reembolso:.2f}\n")
 
 
print("=== 4. Simulador de Margem de Lucro ===")
custo = float(input("Digite o custo de fabricação do produto (R$): "))
preco_venda = custo * 1.35
print(f"O preço de venda recomendado é: R$ {preco_venda:.2f}\n")
 
 
print("=== 5. Validador de Idade para Contratação ===")
ano_nascimento = int(input("Digite o ano de nascimento do candidato: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
apto = idade <= 24
print(f"Idade: {idade} anos. Apto para Jovem Aprendiz? {apto}\n")
 
 
print("=== 6. Controle de Catraca ===")
status = input("Digite o status da credencial (ativa / bloqueada): ").strip().lower()
if status == "ativa":
    print("Acesso Liberado")
else:
    print("Acesso Negado: Procure a portaria")
print()
 
 
print("=== 7. Esteira de Aprovação de Crédito B2B ===")
faturamento = float(input("Digite o faturamento da empresa cliente (R$): "))
if faturamento > 100000:
    print("Limite aprovado: R$ 20.000")
elif faturamento >= 50000:
    print("Limite aprovado: R$ 10.000")
else:
    print("Crédito Reprovado")
print()
 
 
print("=== 8. Auditoria de Desempenho ===")
faltas = int(input("Digite o número de faltas: "))
vendas = float(input("Digite o valor total de vendas (R$): "))
if faltas == 0 and vendas > 50000:
    print("PLR Aprovada")
else:
    print("PLR Negada")
print()
 
 
print("=== 9. Precificação Dinâmica por Região ===")
regiao = input("Digite a sigla da região (S, SE, CO, NE, N): ").strip().upper()
match regiao:
    case "SE" | "S":
        frete = 15.00
    case "CO":
        frete = 25.00
    case "NE" | "N":
        frete = 35.00
    case _:
        frete = 0.00
        print("Região desconhecida.")
 
if frete > 0:
    print(f"O valor do frete para a região {regiao} é: R$ {frete:.2f}")
print()
 
 
print("=== 10. Alerta de Estoque Mínimo ===")
estoque = int(input("Digite a quantidade atual do produto no estoque: "))
if estoque <= 15:
    print("COMPRA URGENTE")
elif estoque <= 50:
    print("ESTOQUE REGULAR")
else:
    print("ESTOQUE CHEIO")
print()
 
 
print("=== 11. Menu de Autoatendimento Contínuo ===")
print("Instrução: Digite '0000' para sair do loop do ponto.")
while True:
    matricula = input("Digite a matrícula para bater o ponto: ")
    if matricula == "0000":
        print("Sistema de manutenção ativado. Encerrando o loop...")
        break
    print(f"Ponto registrado com sucesso para a matrícula {matricula}!\n")
print()
 
 
print("=== 12. Geração Automática de E-mails ===")
funcionarios = ["Ana", "Carlos", "Beatriz", "Daniel"]
print("Gerando e-mails corporativos:")
for nome_func in funcionarios:
    email = f"{nome_func.lower()}@arketech.com"
    print(email)
print()
 
 
print("=== 13. Bloqueio por Tentativas de Login ===")
senha_correta = "Admin123"
tentativas = 0
max_tentativas = 3
while tentativas < max_tentativas:
    senha_digitada = input("Digite a senha (Dica: Admin123): ")
    if senha_digitada == senha_correta:
        print("Login efetuado com sucesso!")
        break
    else:
        tentativas += 1
        restantes = max_tentativas - tentativas
        print(f"Senha incorreta. Você ainda tem {restantes} tentativa(s).")
if tentativas == max_tentativas:
    print("Conta bloqueada por excesso de tentativas.")
print()
 
 
print("=== 14. Balanço Mensal de Vendas ===")
valores_meses = [12000.0, 15000.0, 18000.0]
total_faturamento = 0.0
for valor in valores_meses:
    total_faturamento += valor
print(f"Valores do trimestre: {valores_meses}")
print(f"O faturamento total do trimestre é: R$ {total_faturamento:.2f}")
print("\n=== FIM DO PROGRAMA INTEGRADO ===")