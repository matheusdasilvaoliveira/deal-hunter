# 🛒 Deal Hunter

Monitor de promoções no Telegram, desenvolvido para identificar automaticamente ofertas relevantes e encaminhá-las para um chat privado.

O projeto nasceu de uma necessidade simples: **não perder uma boa promoção de PS5** em meio a centenas de mensagens de grupos de ofertas.

A ideia é transformar esse problema em um pequeno sistema de monitoramento capaz de acompanhar mensagens, identificar ofertas de PS5, analisar seus preços e alertar quando uma oportunidade realmente interessante aparecer.

---

## 🎯 Objetivo

Monitorar grupos de promoções no Telegram e identificar ofertas de:

* PlayStation 5 Slim Digital
* PlayStation 5 Slim com leitor

As ofertas identificadas serão analisadas considerando informações como:

* 💰 preço;
* 💳 forma de pagamento;
* 📆 quantidade de parcelas;
* 🏪 loja;
* 🎟️ cupons;
* 💵 cashback;
* 🎮 versão do console;
* 💾 armazenamento;
* 🔗 link da oferta.

O sistema deverá então classificar a oportunidade e encaminhá-la para o chat privado do usuário.

---

## 💡 Motivação

Um grupo de promoções pode publicar dezenas ou centenas de ofertas por dia. Entre elas, apenas algumas são realmente relevantes.

O objetivo do projeto é evitar a necessidade de acompanhar manualmente todas essas mensagens.

Em vez de:

```text
Grupo do Telegram
       ↓
Centenas de mensagens
       ↓
Procurar manualmente por PS5
       ↓
Verificar preço
       ↓
Comparar com preços anteriores
```

queremos chegar a:

```text
Grupo do Telegram
       ↓
Monitoramento automático
       ↓
Detecção de PS5
       ↓
Extração das informações
       ↓
Análise da oferta
       ↓
Classificação
       ↓
🚨 Alerta no chat privado
```

---

## 📊 Estratégia de preços

O projeto não deverá simplesmente alertar sempre que encontrar a palavra `PS5`.

Uma oferta será avaliada com base em critérios definidos previamente.

Entre os indicadores planejados estão:

* preço atual;
* preço médio conhecido;
* menor preço conhecido;
* maior preço conhecido;
* últimos preços encontrados;
* diferença percentual em relação à média;
* modelo do console;
* forma de pagamento;
* loja;
* parcelamento;
* histórico da oferta.

Exemplo de alerta futuro:

```text
🚨 PS5 SLIM — OPORTUNIDADE EXCEPCIONAL

🎮 Modelo: PS5 Slim Digital
💾 Armazenamento: 825 GB

💰 Preço: R$ 2.699
💳 Pagamento: 12x sem juros
🏪 Loja: Amazon

📊 Média histórica: R$ 3.520
🏆 Menor preço conhecido: R$ 2.589

📉 23% abaixo da média

🔥 Oferta dentro do preço-alvo
🔗 Link da oferta
```

---

## 🏗️ Arquitetura planejada

A arquitetura será construída incrementalmente.

### Versão inicial

```text
Telegram
   │
   ▼
Telethon
   │
   ▼
Monitor de mensagens
   │
   ▼
Filtro PS5
   │
   ▼
Chat privado
```

### Evolução planejada

```text
                         ┌──────────────┐
                         │   Telegram   │
                         └──────┬───────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Message Monitor │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ PS5 Detector    │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Offer Parser    │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Price Analyzer  │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Offer Classifier│
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Alert Service   │
                       └────────┬────────┘
                                │
                                ▼
                         ┌──────────────┐
                         │ Chat privado │
                         └──────────────┘
```

---

## 🛠️ Tecnologias

A implementação inicial utiliza:

* **Python**
* **Telethon** — integração com a API do Telegram
* **python-dotenv** — gerenciamento de variáveis de ambiente

Tecnologias que poderão ser adicionadas conforme o projeto evoluir:

* Docker
* SQLite/PostgreSQL
* testes automatizados
* logging e observabilidade
* CI/CD
* cloud computing

A escolha das tecnologias será feita conforme as necessidades do sistema, evitando adicionar complexidade prematuramente.

---

## 📁 Estrutura inicial

```text
ps5-deal-hunter/
├── src/
│   └── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Essa estrutura será evoluída conforme novas responsabilidades forem adicionadas ao sistema.

---

## 🔐 Segurança

Credenciais e informações de autenticação nunca devem ser versionadas no repositório.

Arquivos como:

```text
.env
*.session
```

devem permanecer fora do Git.

O projeto utiliza variáveis de ambiente para armazenar credenciais da API do Telegram.

---

## 🚧 Status

**Em desenvolvimento.**

### Roadmap inicial

* [x] Criar projeto
* [x] Configurar ambiente Python
* [x] Criar aplicação na API do Telegram
* [ ] Conectar à conta do Telegram
* [ ] Identificar grupos disponíveis
* [ ] Selecionar grupo de promoções
* [ ] Monitorar novas mensagens
* [ ] Criar filtro inicial de PS5
* [ ] Encaminhar ofertas para o chat privado
* [ ] Extrair preço e informações da oferta
* [ ] Criar classificação de ofertas
* [ ] Criar histórico de preços
* [ ] Calcular métricas de preço
* [ ] Persistir dados
* [ ] Containerizar aplicação
* [ ] Fazer deploy para execução 24/7
* [ ] Criar monitoramento e logs

---

## 🎯 Filosofia do projeto

O projeto será desenvolvido de forma incremental, priorizando:

* simplicidade;
* separação de responsabilidades;
* código legível;
* testes automatizados;
* segurança;
* documentação;
* boas práticas de engenharia de software;
* decisões arquiteturais justificadas.

O objetivo não é apenas criar um script que encontre PS5.

O objetivo é utilizar o problema como um **projeto prático de engenharia de software**, aplicando conceitos de desenvolvimento, arquitetura, testes, persistência, automação, Docker e cloud.

---

## 📜 Licença

Este projeto é destinado inicialmente a fins pessoais e educacionais.

A definição de uma licença específica será realizada posteriormente.
