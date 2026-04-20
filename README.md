# 🚀 Automação Serverless de Emissão e Envio de NFSe

## 📌 Visão Geral

Este projeto implementa uma automação completa para emissão de Notas Fiscais de Serviço (NFSe), utilizando uma arquitetura **serverless e orientada a eventos na AWS**.

A solução elimina processos manuais, garantindo:

- Emissão automática de NFSe
- Armazenamento seguro dos documentos
- Envio automático por e-mail com anexo
- Baixíssimo custo operacional

---

## 💡 Motivação

Este projeto surgiu a partir de uma necessidade real.

Durante minha rotina como prestador de serviços, enfrentei dificuldades em controlar o prazo de emissão e envio de Notas Fiscais de Serviço (NFSe) para a consultoria contratante. Em alguns casos, isso resultava em risco de atraso e impacto financeiro.

Paralelamente, eu estava me preparando para a certificação AWS Certified Cloud Practitioner e buscava uma forma prática de aplicar os conceitos estudados.

Diante disso, decidi transformar esse problema pessoal em uma solução automatizada utilizando serviços da AWS.

---

## 🎯 Objetivo

Criar uma solução que:

- Automatize a emissão de NFSe
- Elimine a dependência de execução manual
- Garanta envio dentro do prazo
- Utilize arquitetura serverless
- Sirva como laboratório prático para aprendizado em cloud

---

## ⚙️ Tecnologias Utilizadas

- AWS ECS (Fargate)
- AWS Lambda
- Amazon S3
- Amazon EventBridge
- Python 3
- Playwright (RPA)
- Boto3 (AWS SDK)
- SMTP (Gmail)

---

## 🔁 Fluxo de Execução

1. O **EventBridge** dispara a execução mensal (cron)
2. Uma **task no ECS Fargate** é iniciada
3. O script:
   - Acessa o portal NFSe
   - Emite a nota fiscal
   - Baixa o PDF
   - Faz upload para o S3
4. O **S3 dispara um evento**
5. A **Lambda é acionada automaticamente**
6. A Lambda:
   - Baixa o PDF
   - Envia o e-mail com anexo via SMTP

---

## 💰 Custo Estimado

| Serviço       | Custo mensal |
|--------------|-------------|
| ECS Fargate  | ~$0.01      |
| Lambda       | $0 (free tier) |
| S3           | ~$0.01      |
| EventBridge  | $0          |
| SMTP (Gmail) | $0          |

### 💡 Total:
> **Menos de $1 por ano**

---

## 📦 Armazenamento Inteligente (S3 Lifecycle)

Os arquivos são automaticamente movidos para camadas mais baratas:

- 0–60 dias → S3 Standard
- Após 60 dias → Glacier Instant Retrieval

Ideal para:
- Notas fiscais (acesso raro)
- Redução de custos
- Retenção para imposto

---

## 🔐 Segurança

- Uso de IAM Roles (sem credenciais hardcoded)
- Comunicação segura entre serviços AWS
- Upload via SDK oficial (boto3)

### Melhorias futuras:
- AWS Secrets Manager para credenciais
- Criptografia no S3 (SSE-KMS)

---

## 📈 Diferenciais

- Arquitetura **serverless**
- Orientado a eventos (event-driven)
- Totalmente automatizado
- Baixo custo
- Escalável
- Independente de máquina local

---

## 🧠 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conceitos como:

- Arquitetura orientada a eventos
- Computação serverless
- Orquestração de serviços AWS
- Automação de processos com RPA
- Controle de custos em cloud
- Segurança com IAM Roles

Além disso, o projeto permitiu consolidar conhecimentos práticos relevantes para a certificação AWS Cloud Practitioner.

---

## 🔄 Before vs After

| Antes | Depois |
|------|-------|
| Emissão manual | Automação completa |
| Risco de atraso | Execução programada |
| Dependência da máquina local | 100% em cloud |
| Envio manual de e-mail | Envio automático com anexo |

---

## 🧠 Possíveis Evoluções

- Substituir SMTP por AWS SES
- Implementar retry e DLQ
- Adicionar fila com SQS
- Dashboard com CloudWatch
- Suporte multi-tenant (vários CNPJs)
- API com API Gateway

---

## 🎯 Objetivo do Projeto

Demonstrar habilidades em:

- Arquitetura cloud na AWS
- Automação de processos (RPA)
- Integração entre serviços gerenciados
- Otimização de custos
- Sistemas orientados a eventos

---

## 👨‍💻 Autor

Jefferson Cavalcante

---

## 📄 Licença

Este projeto é de uso educacional e demonstração de portfólio.
