# 📦 PotterDB API to S3

Este projeto é uma aplicação simples em Python desenvolvida como atividade prática. O objetivo é consumir dados da API **PotterDB**, salvar os dados localmente em formato JSON e, em seguida, enviar esse arquivo para um bucket (como o AWS S3). Também há uma função que lê o arquivo direto do bucket e imprime no terminal.

---

## 🎯 Objetivo

- Praticar o uso do **Postman** para testar requisições HTTP (GET, POST, etc).
- Desenvolver habilidades com:
  - Consumo de APIs REST.
  - Manipulação de arquivos JSON.
  - Integração com serviços de armazenamento em nuvem (AWS S3).

---

## 🚀 Funcionalidades

1. 🔍 Consulta à **API PotterDB** para buscar dados de personagens.
2. 💾 Salvamento dos dados em um arquivo `.json`.
3. ☁ Envio do arquivo JSON para um bucket (como o **AWS S3**).
4. 🖨 Função que acessa o arquivo diretamente do bucket e exibe os dados no terminal.

---

## 🛠 Tecnologias utilizadas

- Python 3.x
- Bibliotecas:
  - `requests` (requisições HTTP)
  - `boto3` (integração com AWS S3)
  - `json` (manipulação de arquivos JSON)
- Postman (testes com a API)
- AWS S3 (armazenamento em nuvem)

---

## 📁 Estrutura do projeto

```bash
📦 potterdb-api-to-s3
├── index.py
└── README.md
