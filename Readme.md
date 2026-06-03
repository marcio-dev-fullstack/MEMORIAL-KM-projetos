# MEMORIAL-KM-projetos

Como utilizar para seus projetos

Como rodar:

Certifique-se de que o python-docx foi instalado corretamente com o comando python -m pip install python-docx.

Salve o arquivo JSON e o arquivo .py na pasta C:\PROJETOS\MEMORIAL-KM.

No terminal PowerShell do VS Code, digite:

python gerador_memorial.py

---

Para facilitar o fluxo de trabalho, o script Python chamado `publicar.py` que automatiza todo o processo de versionamento e envio para o GitHub. Este script utiliza a biblioteca `os` para executar comandos no terminal diretamente do seu ambiente de desenvolvimento.

### Script `publicar.py`
### Como utilizar no terminal

Após criar o arquivo `publicar.py`, você pode utilizá-lo de duas formas simples no terminal do VS Code:

**1. Para um commit com mensagem padrão:**

```bash
python publicar.py

```

**2. Para um commit com uma mensagem específica (recomendado):**

```bash
python publicar.py "Minha mensagem de alteração aqui"

```

### Por que esta automação ajuda?

* **Velocidade:** Você reduz de 3 comandos manuais para apenas 1 comando simples.
* **Padronização:** Garante que todos os arquivos (incluindo novos scripts) sejam adicionados corretamente antes do envio.
* **Foco no Código:** Você economiza tempo de digitação, permitindo que foque mais na lógica do `gerador_memorial.py` ou nos seus outros sistemas.
