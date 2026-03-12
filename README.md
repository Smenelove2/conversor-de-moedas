# Conversor de Moedas

Aplicação web desenvolvida com **Streamlit** para conversão de moedas em tempo real, utilizando cotações obtidas pela API **AwesomeAPI**.

O projeto permite selecionar a moeda de origem e a moeda de destino por meio de listas suspensas (`selectbox`), evitando erros de digitação e melhorando a experiência do usuário. A base de moedas disponíveis é carregada a partir do padrão **ISO 4217** em arquivo XML.

## Funcionalidades

- Conversão de moedas em tempo real
- Seleção de moedas por código e nome
- Leitura das moedas a partir de arquivo XML
- Interface simples e direta com Streamlit
- Validação básica de valor informado
- Tratamento para pares de moedas indisponíveis

## Tecnologias utilizadas

- **Python 3**
- **Streamlit**
- **Requests**
- **XML ElementTree**
- **AwesomeAPI** para obtenção das cotações

## Estrutura do projeto

```bash
conversor-de-moedas/
├── app.py
├── list-one.xml
├── list-one-moedas-ptbr.xml
├── Utils/
│   ├── request.py
│   └── utils.py
└── venv/
```

## Como funciona

A aplicação segue este fluxo:

1. Carrega a lista de moedas a partir do arquivo `list-one-moedas-ptbr.xml`
2. Exibe as moedas em dois campos de seleção:
   - moeda base
   - moeda destino
3. Recebe o valor numérico a ser convertido
4. Consulta a cotação do par selecionado na AwesomeAPI
5. Realiza a conversão e exibe o resultado em tela

## Pré-requisitos

Antes de executar o projeto, tenha instalado:

- Python 3.10 ou superior
- `pip`

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd conversor-de-moedas
```

Crie e ative um ambiente virtual:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install streamlit requests
```

## Como executar

No terminal, dentro da pasta do projeto, rode:

```bash
streamlit run app.py
```

O Streamlit abrirá a aplicação localmente no navegador.

## Arquivos principais

### `app.py`
Arquivo principal da interface. Responsável por:

- montar a página
- exibir os campos de seleção
- receber o valor a converter
- chamar as funções de requisição e conversão
- mostrar o resultado ao usuário

### `Utils/request.py`
Responsável por consultar a cotação da moeda na API.

### `Utils/utils.py`
Contém funções auxiliares do sistema, como:

- carregamento do XML de moedas
- conversão do valor com base na cotação

### `list-one.xml`
Arquivo XML original com base no padrão ISO 4217.

### `list-one-moedas-ptbr.xml`
Versão adaptada do XML com os nomes das moedas traduzidos para português.

## Exemplo de uso

- Moeda base: `BRL - Real brasileiro`
- Moeda destino: `USD - Dólar americano`
- Valor: `100`

Resultado esperado:

```text
BRL 100 vale: USD 19.16
```

> O valor exibido depende da cotação retornada pela API no momento da consulta.

## Melhorias futuras

- Exibir símbolo monetário no resultado
- Melhorar o tratamento de erros da API
- Adicionar histórico de conversões
- Mostrar data e hora da cotação
- Criar arquivo `requirements.txt`
- Padronizar nomes e mensagens da interface

## Autor

Projeto desenvolvido para fins de estudo e prática com:

- Python
- Streamlit
- consumo de API
- manipulação de XML
