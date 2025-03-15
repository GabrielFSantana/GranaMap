# GranaMap

## 📌 Sobre o Projeto
GranaMap é um sistema desenvolvido em **Python + Flask** para auxiliar no gerenciamento de economia pessoal. Ele permite registrar valores economizados e acompanhar o progresso por meio de gráficos interativos.

## 🚀 Funcionalidades
- 📊 **Gráfico de progresso** mostrando a quantia economizada e a meta.
- ➕ **Adicionar valores** para acompanhar a economia.
- 🗑️ **Remover valores** do histórico.
- 📜 **Histórico** com todas as contribuições.
- 🎥 **Dicas de economia** com vídeos.
- 👨‍💻 **Página sobre o desenvolvedor**.

## 🛠️ Tecnologias Utilizadas
- 🐍 **Python (Flask)** - Backend
- 🗄️ **SQLite** - Banco de Dados
- 📊 **Chart.js** - Gráficos
- 🎨 **HTML, CSS e JavaScript** - Frontend

## 📂 Estrutura do Projeto
```
GranaMap/
│── static/        # Arquivos CSS, JS, imagens
│── templates/     # Páginas HTML
│── app.py         # Código principal
│── database.db    # Banco de Dados SQLite
│── requirements.txt  # Dependências do projeto
│── README.md      # Documentação do projeto
```

## ▶️ Como Rodar o Projeto
### 1️⃣ Criar e ativar o ambiente virtual
```sh
python -m venv venv
```
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```sh
  source venv/bin/activate
  ```

### 2️⃣ Instalar as dependências
```sh
pip install -r requirements.txt
```

### 3️⃣ Rodar o servidor Flask
```sh
python app.py
```
Acesse: **http://127.0.0.1:5000/**

## ☁️ Como Subir no GitHub
```sh
git init
git add .
git commit -m "Primeiro commit"
git branch -M main
git remote add origin https://github.com/seu-usuario/granamap.git
git push -u origin main
```

## 📜 Licença
Este projeto foi desenvolvido por **Gabriel F. Santana** e está disponível para uso pessoal e contribuições. 🚀
