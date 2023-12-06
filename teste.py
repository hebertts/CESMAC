def price(n,valor_emprestimo):
    taxa_n = 0.1 / n
    pmt = (valor_emprestimo * taxa_n)/(1 - (1+taxa_n)**-n)
    return pmt
valor = price(12,10000)
print(f'{valor:.2f}')
def credito_conta(renda,movimentacao):
    fator = 3.5
    credito = (renda + movimentacao) * fator
    return credito
credito = credito_conta(400,3000)
print(credito)

