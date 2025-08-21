 Gerenciamento de Estudantes

Sistema de gerenciamento acadêmico desenvolvido em Django e Django REST Framework, com suporte a estudantes, cursos, matrículas e disciplinas.

O objetivo do projeto é fornecer uma API para manipulação de dados acadêmicos, permitindo o cadastro e listagem de estudantes, gerenciamento de cursos e controle de matrículas.

🚀 Funcionalidades

👨‍🎓 Estudantes

Cadastro de estudantes com nome e registro acadêmico

Listagem de estudantes

📘 Cursos

Cadastro de cursos com nome e turno

Listagem de cursos

📝 Matrículas

Associação de estudantes a cursos

Registro de data de matrícula

📖 Disciplinas

Cadastro de disciplinas vinculadas a cursos

Controle de quais disciplinas cada estudante está cursando

🔗 Associação Matrícula ↔ Disciplinas

Cada matrícula pode estar ligada a múltiplas disciplinas

Consulta de quais estudantes cursam determinada disciplina

🛠️ Tecnologias utilizadas

Python 3.12

Django 5.x

Django REST Framework

SQLite em desenvolvimento

pip para gerenciamento de pacotes

⚙️ Instalação e uso
1️⃣ Clonar o repositório
git clone https://github.com/LeoFonseca98/gerenciamento_de_estudante.git
cd gerenciamento_de_estudante

2️⃣ Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Instalar dependências
pip install -r requirements.txt

5️⃣ Aplicar migrações
python manage.py migrate

6️⃣ Criar superusuário
python manage.py createsuperuser

7️⃣ Rodar o servidor
python manage.py runserver

Acesse: http://127.0.0.1:8000/admin/

🌐 Endpoints da API

Cursos

 GET /api/v1/curso/ → lista cursos
 
 POST /api/v1/curso/ → cria curso

Disciplinas

 GET /api/v1/disciplina/ → lista disciplinas
 
 POST /api/v1/disciplina/ → cria disciplina

Estudantes

 GET /api/v1/estudante/ → lista estudantes
 
 POST /api/v1/estudante/ → cria estudante

Inscrição em Disciplinas

 GET /api/v1/inscricao/ → lista inscrições em Disciplina
 
 POST /api/v1/inscricao/ → cria inscrição em Disciplina

Matrículas

 GET /api/v1/matricula/ → lista matrículas
 
 POST /api/v1/matricula/ → cria matrícula



