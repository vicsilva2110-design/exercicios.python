# 1. Coleta de dados
nome_empresa = input("Digite o nome da empresa: ")
faturamento = float(input("Digite o faturamento mensal (R$): "))
valor_emprestimo = float(input("Digite o valor do empréstimo solicitado (R$): "))
 
# 2. Cálculo da parcela em 12x
parcela_mensal = valor_emprestimo / 12
 
# 3. Descobrindo a porcentagem do faturamento
porcentagem_parcela = (parcela_mensal / faturamento) * 100
 
# 4. Árvore de Decisão
if porcentagem_parcela <= 30:
    status = "APROVADO"
elif porcentagem_parcela <= 50:
    status = "EM ANÁLISE (Risco Moderado)"
else:
    status = "RECUSADO"
 
# 5. Resultado formatado com f-string
print("\n--- RESUMO DA AUDITORIA DE CRÉDITO ---")
print(f"Empresa: {nome_empresa}")
print(f"Faturamento Mensal: R$ {faturamento:.2f}")
print(f"Empréstimo Solicitado: R$ {valor_emprestimo:.2f}")
print(f"Valor da Parcela (12x): R$ {parcela_mensal:.2f} ({porcentagem_parcela:.1f}% do faturamento)")
print(f"Parecer Final: {status}")