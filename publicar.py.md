Este é um manual técnico estruturado em formato Markdown para o seu script `publicar.py` (ou, no contexto do seu fluxo atual, o `gerar_todos.py`).

---

# Manual Técnico: Automatizador de Memoriais Técnicos (`publicar.py`)

## 1. Visão Geral

O `publicar.py` é uma ferramenta de automação desenvolvida para engenheiros civis que buscam otimizar a emissão de memoriais descritivos e laudos de avaliação mercadológica. O script processa arquivos de dados (JSON) e gera automaticamente documentos formatados (`.docx`) seguindo as normas técnicas da ABNT.

## 2. Arquitetura do Sistema

O sistema utiliza uma estrutura modular para separar dados de lógica:

* **/dados**: Repositório de arquivos `.json` contendo as variáveis de cada projeto.
* **/scripts**: Onde reside o núcleo da lógica de automação (`publicar.py`).
* **/output**: Diretório de destino para os laudos gerados.

## 3. Pré-requisitos

* **Python 3.x** instalado.
* Biblioteca `python-docx`:
```bash
python -m pip install python-docx

```



## 4. Configuração dos Dados (Input)

Para cada imóvel, crie um arquivo `.json` na pasta `/dados` com a seguinte estrutura:

```json
{
    "projeto": "Nome do Imóvel",
    "cidade": "Conceição do Araguaia - PA",
    "engenheiro": "SEU NOME",
    "crea": "0000000000",
    "num_art": "ART-123456",
    "descricao": "Descrição técnica detalhada...",
    "orcamento": [
        {"item": "1.0", "desc": "Descrição do item", "valor": 1000.00}
    ]
}

```

## 5. Execução

O script pode ser executado via terminal ou através da `Task` configurada no VS Code:

### Via Terminal:

```bash
python publicar.py

```

### Via Atalho (VS Code):

Pressione `Ctrl + Shift + B` para disparar a tarefa de geração automática configurada no seu `tasks.json`.

## 6. Padronização Normativa

O documento gerado atende aos requisitos básicos da **ABNT NBR 14653**:

* Identificação completa do profissional responsável (nome e registro CREA-PA).
* Seção dedicada à Responsabilidade Técnica.
* Orçamento sintético estruturado.
* Data de emissão automática (relevante para validade de laudos).

## 7. Manutenção

* **Adicionar Novos Memoriais**: Basta copiar um arquivo JSON existente, alterar os campos e rodar o script novamente.
* **Backup**: Recomenda-se o versionamento da pasta `dados/` utilizando Git para manter o histórico de todas as avaliações já emitidas.

---

*Desenvolvido por Marcio Rodrigues de Oliveira - Engenharia e Software.*