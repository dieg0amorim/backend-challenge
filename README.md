# Desafio Backend-Challenge

Este projeto é uma aplicação Flask projetada para validar JSON Web Tokens (JWT). 
A aplicação está organizada de acordo com os princípios SOLID para garantir a modularidade e a sua manutenção.

- Deve ser um JWT válido
- Deve conter apenas 3 claims (Name, Role e Seed)
- A claim Name não pode ter carácter de números
- A claim Role deve conter apenas 1 dos três valores (Admin, Member e External)
- A claim Seed deve ser um número primo.
- O tamanho máximo da claim Name é de 256 caracteres.

#  Definição

Input: Um JWT (string).  
Output: Um boolean indicando se a valido ou não.

# Estrutura do Projeto

```


.github/workflows/
├──terraform-apply.yml
├──terraform-plan.yml

app/
├── app.py
├── requirements.txt
├── Dockerfile
├── utils/
│   ├── __init__.py
│   ├── prime_checker.py
│   └── jwt_validator.py
└── tests/
    ├── __init__.py
    ├── test_app.py
    └── utils/
        ├── __init__.py
        ├── test_prime_checker.py
        └── test_jwt_validator.py

──Insomnia_collection.json
──cloudwatch.tf
──cluster-ecs.tf
──grafana.tf
──jwt-validator.tf
──main.tf
──network.tf
──prometheus.tf
```

# Descrição dos Arquivos e Módulos

- github/workflows

Local onde esta armazenados os arquivos de configuração do CI/CD via Terraform Cloud através do github actions.
  
terraform-apply.yml

terraform-plan.yml

- app.py

Este arquivo contém o código principal da aplicação Flask.
Define um endpoint /validate para validar JWTs recebidos através de uma requisição POST.

Principais Componentes:

Rota /validate: Recebe um JSON com um token JWT e responde com a validade do token.
Bibliotecas Utilizadas: Flask para o servidor web e PrometheusMetrics para monitoramento.

- requirements.txt

Lista todas as dependências necessárias para executar a aplicação.
Inclui Flask, Prometheus Flask Exporter, PyJWT e pytest.

- Dockerfile

Contém as instruções para construir a imagem Docker da aplicação.
Define a imagem base, copia os arquivos, instala as dependências e define o comando de inicialização.

- utils/prime_checker.py

Este módulo contém a lógica para verificar se um número é primo.
Classe:

PrimeChecker
Método is_prime(num): Recebe um número inteiro e retorna True se o número for primo, caso contrário, retorna False.

- utils/jwt_validator.py

Este módulo contém a lógica para validação de JSON Web Tokens (JWTs).
Classe:

JWTValidator
Método validate(token): Recebe um token JWT e retorna True se o token for válido conforme regras específicas, caso contrário, retorna False.
Dependências Internas: Utiliza a classe PrimeChecker para verificar se o valor do campo Seed no JWT é um número primo.

- tests/test_app.py

Contém testes para a aplicação Flask, especificamente para a rota /validate.

Principais Componentes:

Testes Unitários: Verificam a funcionalidade da rota /validate com tokens válidos, inválidos e cenários onde o token está ausente.

- tests/utils/test_prime_checker.py

Contém testes unitários para o módulo prime_checker.py.

Principais Componentes:

Testes Unitários: Verificam a precisão do método is_prime com diversos números de entrada.

- tests/utils/test_jwt_validator.py

Contém testes unitários para o módulo jwt_validator.py.

Principais Componentes:

Testes Unitários: Verificam a precisão do método validate com tokens válidos e inválidos.

- Insomnia_collection.json

Arquivo que contém a coleção das requests via Insomnia.

- cloudwatch.tf

Arquivo terraform para deploy de log group do cloudwatch para aplicação API na AWS.

- cluster-ecs.tf

Arquivo terraform para deploy cluster que será utilizado para serviços ECS na AWS.

- grafana.tf

Arquivo terraform para deploy do serviço Grafana para visualização de dashboards e analise de monitoramento da aplicação jtw_validator em task ecs na AWS.

- jwt-validator.tf

Arquivo terraform para deploy de serviço ECS da aplicação exposta através da AWS.

- main.tf

Arquivo terraform com configurações de provider para provisionar infraestrutura aws.

- network.tf

Arquivo terraform para deploy das configurações de rede como VPC,subnets,IGW, security groups e suas respectivas regras.

- prometheus.tf

Arquivo terraform para deploy de prometheus em task ecs na AWS.

## Deploy de infraestrutura na AWS

### Github Actions - Workflow - Terraform Cloud

Dentro do diretório: github/workflows contém os arquivos terraform-plan.yml e terraform-apply.yml onde é disparado a esteira de validações CI/CD para provisionamento da infraestrutura na AWS.

Terraform Plan

<img width="942" alt="image" src="https://github.com/user-attachments/assets/a81e2914-f439-440b-afee-7f01407d65f0">


Terraform Apply

<img width="942" alt="image" src="https://github.com/user-attachments/assets/1fa12810-e7ac-4e57-944e-962721ae4127">


Simultaneamente no terraform cloud as "runs" vão sendo executadas onde esta configurado as informações da conta aws que será provisionada.

<img width="943" alt="terrraform cloud" src="https://github.com/user-attachments/assets/cb8bd230-e735-4a8c-9d3d-0c1d6478a418">


## Cluster ECS - AWS

Cluster "backend-challenge" provisionado para rodar os serviços e tasks ECS.

<img width="959" alt="cluster ecs" src="https://github.com/user-attachments/assets/43c644a4-62d7-45e4-9c07-fe0c3dc30ed0">

### No cluster ECS, encontraremos os seguintes serviços:

- JWT API service
- Prometheus
- Grafana

<img width="958" alt="services ecs" src="https://github.com/user-attachments/assets/60a839eb-5eaf-4180-8dca-c012fd28dca1">

## Log groups configurados no cloudwatch para analise dos logs:

<img width="949" alt="cw aws loggroups" src="https://github.com/user-attachments/assets/1fd22a55-f45c-4bed-9b26-e4944260c45f">


### Logs:

<img width="956" alt="cw logs jwt" src="https://github.com/user-attachments/assets/467de2a9-ee24-4a17-8190-5791aa027de6">


### API:

<img width="955" alt="api ecs" src="https://github.com/user-attachments/assets/c07cc19e-3299-4655-8b19-f1fa1f0cb927">

### API NETWORK:


<img width="950" alt="api network" src="https://github.com/user-attachments/assets/9ed412a8-c0a4-4d4b-80a5-300f400aa132">

## Prometheus Service

<img width="938" alt="image" src="https://github.com/user-attachments/assets/fb3f4d20-882c-4960-b841-ac77a9d22154">


## Grafana Service:

### Dashboard flask:

<img width="950" alt="image" src="https://github.com/user-attachments/assets/254193ea-2d9f-4da9-b407-0c82b1aeaecc">



### Dashboard de monitoração do próprio prometheus:

<img width="956" alt="image" src="https://github.com/user-attachments/assets/c4770e8f-1f29-4d2e-8d52-b97ade875338">


## Como Executar a Aplicação Local

### Com Docker

Construir a Imagem Docker:

```
bash
docker build -t my_flask_app .

```
### Executar o Container:
```
bash
docker run -d -p 5000:5000 --name my_flask_container my_flask_app
```

## Sem Docker

### Instalar as Dependências:

```
bash
pip install -r requirements.txt
```

### Executar a Aplicação:

```
bash
python app.py
```

## Como Executar os Testes

### Com Docker

```
bash
docker run --rm -v $(pwd):/app my_flask_app pytest
```

### Sem Docker

```
bash
pytest
```

# Massa de teste 

### Caso 1:
Entrada:
```
eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJTZWVkIjoiNzg0MSIsIk5hbWUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05sIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg
```
Saida:
```
verdadeiro
```
Justificativa:
Abrindo o JWT, as informações contidas atendem a descrição:
```json
{
  "Role": "Admin",
  "Seed": "7841",
  "Name": "Toninho Araujo"
}
```

### Caso 2:
Entrada:
```
eyJhbGciOiJzI1NiJ9.dfsdfsfryJSr2xrIjoiQWRtaW4iLCJTZrkIjoiNzg0MSIsIk5hbrUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05fsdfsIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg
```
Saida:
```
falso
```
Justificativa:
JWT invalido

### Caso 3:
Entrada:
```
eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiRXh0ZXJuYWwiLCJTZWVkIjoiODgwMzciLCJOYW1lIjoiTTRyaWEgT2xpdmlhIn0.6YD73XWZYQSSMDf6H0i3-kylz1-TY_Yt6h1cV2Ku-Qs
```
Saida:
```
falso
```
Justificativa:
Abrindo o JWT, a Claim Name possui caracter de números
```json
{
  "Role": "External",
  "Seed": "72341",
  "Name": "M4ria Olivia"
}
```

### Caso 4:
Entrada:
```
eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiTWVtYmVyIiwiT3JnIjoiQlIiLCJTZWVkIjoiMTQ2MjciLCJOYW1lIjoiVmFsZGlyIEFyYW5oYSJ9.cmrXV_Flm5mfdpfNUVopY_I2zeJUy4EZ4i3Fea98zvY
```
Saida:
```
falso
```
Justificativa:
Abrindo o JWT, foi encontrado mais de 3 claims.
```json
{
  "Role": "Member",
  "Org": "BR",
  "Seed": "14627",
  "Name": "Valdir Aranha"
}
```
## Teste curl de API-jwt exposta na AWS com as seguintes validações:

<img width="958" alt="teste curl" src="https://github.com/user-attachments/assets/f192feff-8237-405b-9a04-3f6afb58d36a">

## Conclusão

Esta aplicação demonstra uma implementação limpa e modular usando Flask, seguindo os princípios de design SOLID. O projeto é configurado para fácil implantação com Docker e inclui testes abrangentes para garantir a qualidade do código.

