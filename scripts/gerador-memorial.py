import os
import json
from docx import Document
from datetime import datetime

def formatar_moeda(valor):
    """Formata o valor para o padrão brasileiro."""
    return f"R$ {valor:,.2f}"

def gerar_memorial(caminho_json, pasta_saida):
    """Lê o arquivo JSON e gera o documento Word."""
    try:
        with open(caminho_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except Exception as e:
        print(f"Erro ao ler {caminho_json}: {e}")
        return

    # Iniciar documento
    doc = Document()
    doc.add_heading('MEMORIAL DESCRITIVO E AVALIAÇÃO TÉCNICA', 0)
    
    # Data automática
    data = datetime.now().strftime('%d de %B de %Y')
    doc.add_paragraph(f"Conceição do Araguaia - PA, {data}")
    
    # 1. Descrição
    doc.add_heading('1. Descrição do Imóvel', level=1)
    doc.add_paragraph(dados.get('descricao', 'Sem descrição fornecida.'))
    
    # 2. Orçamento
    doc.add_heading('2. Orçamento Sintético', level=1)
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    hdr = table.rows[0].cells
    hdr[0].text, hdr[1].text, hdr[2].text = 'Item', 'Descrição', 'Valor (R$)'
    
    valor_total = 0
    for item in dados.get('orcamento', []):
        row = table.add_row().cells
        row[0].text = item['item']
        row[1].text = item['desc']
        row[2].text = formatar_moeda(item['valor'])
        valor_total += item['valor']
    
    # Linha de Total
    row_total = table.add_row().cells
    row_total[1].text = "TOTAL DO EMPREENDIMENTO"
    row_total[2].text = formatar_moeda(valor_total)
    
    # 3. Responsabilidade Técnica
    doc.add_heading('3. Responsabilidade Técnica', level=1)
    doc.add_paragraph(f"ART Vinculada: {dados.get('num_art', 'A preencher')}")
    doc.add_paragraph("\n\n__________________________________________")
    doc.add_paragraph(f"{dados['engenheiro']}\nEngenheiro Civil\nCREA-PA: {dados['crea']}")
    
    # Salvar
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
        
    nome_arquivo = f"Memorial_{dados['projeto'].replace(' ', '_')}.docx"
    doc.save(os.path.join(pasta_saida, nome_arquivo))
    print(f"Laudo gerado com sucesso: {nome_arquivo}")

def main():
    # Define caminhos relativos robustos
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pasta_dados = os.path.join(base_dir, 'dados')
    pasta_saida = os.path.join(base_dir, 'output')
    
    # Verifica se pasta dados existe
    if not os.path.exists(pasta_dados):
        print(f"Erro: Pasta 'dados' não encontrada em {pasta_dados}")
        return

    # Processa todos os JSONs
    for arq in os.listdir(pasta_dados):
        if arq.endswith('.json'):
            gerar_memorial(os.path.join(pasta_dados, arq), pasta_saida)

if __name__ == "__main__":
    main()