import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# 1. Ler arquivo CSV
df = pd.read_csv('vendas.csv')

# 2. Criar gráfico de barras
plt.figure(figsize=(10,6))
df.groupby('Produto')['Valor'].sum().plot(kind='bar')
plt.title('Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Valor Total')
plt.tight_layout()
plt.savefig('grafico_vendas.png')
plt.close()

# 3. Gerar resumo
total_vendas = df['Valor'].sum()
produto_mais_vendido = df.groupby('Produto')['Valor'].sum().idxmax()

# 4. Criar PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Relatório de Vendas", ln=True, align="C")
pdf.ln(10)
pdf.cell(200, 10, txt=f"Total de Vendas: R$ {total_vendas:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Produto Mais Vendido: {produto_mais_vendido}", ln=True)
pdf.ln(10)
pdf.image('grafico_vendas.png', x=10, y=60, w=180)

# 5. Salvar PDF
pdf.output("relatorio_vendas.pdf")
