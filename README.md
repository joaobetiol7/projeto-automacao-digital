# 🏭 Desafio de Automação Digital
## Gestão de Peças, Qualidade e Armazenamento

Este projeto foi desenvolvido como parte da disciplina de **Algoritmos e Lógica de Programação**, com o objetivo de simular um sistema de automação industrial para controle de qualidade de peças produzidas.

---

## 🎯 Objetivo

Criar um sistema em Python capaz de:

- Receber dados de peças (ID, peso, cor e comprimento)
- Avaliar automaticamente a qualidade das peças
- Separar peças aprovadas e reprovadas
- Armazenar peças aprovadas em caixas com limite de 10 unidades
- Gerar relatórios consolidados da produção

---

## ⚙️ Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

1. ✅ Cadastrar nova peça  
2. 📋 Listar peças aprovadas e reprovadas  
3. ❌ Remover peça cadastrada  
4. 📦 Listar caixas fechadas  
5. 📊 Gerar relatório final  

---

## 🧠 Regras de Negócio

Uma peça será considerada **APROVADA** se atender a TODOS os critérios:

- Peso entre **95g e 105g**
- Cor **azul** ou **verde**
- Comprimento entre **10cm e 20cm**

Caso contrário, será **REPROVADA**, com o motivo registrado.

---

## 📦 Lógica de Armazenamento

- Apenas peças aprovadas são armazenadas
- Cada caixa comporta **até 10 peças**
- Ao atingir o limite, a caixa é automaticamente fechada
- Uma nova caixa é iniciada

---

## 📊 Relatórios Gerados

O sistema fornece:

- Total de peças aprovadas  
- Total de peças reprovadas  
- Motivos das reprovações  
- Quantidade de caixas utilizadas  

---

## ▶️ Como Executar o Projeto

### ✅ Pré-requisitos:
- Python 3 instalado
- ### 🚀 Passo a passo:

Clone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
python main.py
```

---

## 💻 Exemplo de Uso

Entrada:
```text
ID: 001  
Peso: 100  
Cor: azul  
Comprimento: 15  
```

Saída:
```text
Peça APROVADA e armazenada na caixa 1
```

Entrada:
```text
ID: 002  
Peso: 120  
Cor: vermelho  
Comprimento: 25  
```

Saída:
```text
Peça REPROVADA  
Motivos:  
- Peso fora do padrão  
- Cor inválida  
- Comprimento fora do padrão  
```

---

## 🧩 Estrutura do Projeto

```text
📁 projeto
 ├── main.py
 ├── README.md
```
