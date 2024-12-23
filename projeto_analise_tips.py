# -*- coding: utf-8 -*-
"""Projeto_Analise_tips.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KeXA_TXaTkljXv4u7MIHuMuiLOqnR-k8

Problema: Prever o valor da gorjeta com base em informações do cliente
Descrição: Restaurantes e estabelecimentos que dependem de gorjetas para os funcionários podem se beneficiar de um sistema que analisa padrões de pagamento. A análise de dados e Machine Learning podem ajudar a prever o valor da gorjeta que um cliente pode dar, com base em informações como:

Total da conta.
Gênero do cliente.
Dia da semana.
Se o cliente está sozinho ou em grupo.
"""

import os

username = "italofvaz" # insira o seu nome de usuário do git
os.environ["GITHUB_USER"] = username

!git config --global user.name "${GITHUB_USER}"

import os
from getpass import getpass

usermail = getpass()
os.environ["GITHUB_MAIL"] = usermail

!git config --global user.email "${GITHUB_MAIL}"

import getpass
usermail = getpass.getpass("italofvaz@hotmail.com")
os.environ["GITHUB_MAIL"] = usermail
!git config --global user.email "${GITHUB_MAIL}"

import os
from getpass import getpass

usertoken = getpass()
os.environ["GITHUB_TOKEN"] = usertoken

!git add .
!git commit -m "Commit message"
!git push origin main

!git clone https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/italofvaz/Machine_Learn_tips.git

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/Machine_Learn_tips/

import seaborn as sns
import pandas as pd

# Carregar o dataset
data = sns.load_dataset('tips')

data.head()

"""PROBLEMAS:

Prever o valor da gorjeta com base nas informações fornecidas.
Verificar a correlação entre tip e outras variáveis
Analisar a influência de variáveis categóricas como day e time na gorjeta média.
Identificar outliers e padrões nos dados.
"""

!git add .
!git status

!git commit -m "novo prdojeto ML"

!git push origin main
!git status

!git remote -v

!git remote set-url origin https://github.com/italofvaz/Machine_Learn_tips.git