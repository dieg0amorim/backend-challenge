# Desafio Backend-Challenge

Este projeto é uma aplicação Flask projetada para validar JSON Web Tokens (JWT) e verificar se um número específico é primo. 
A aplicação está organizada de acordo com os princípios SOLID para garantir a modularidade e a sua manutenção.

- Deve ser um JWT válido
- Deve conter apenas 3 claims (Name, Role e Seed)
- A claim Name não pode ter carácter de números
- A claim Role deve conter apenas 1 dos três valores (Admin, Member e External)
- A claim Seed deve ser um número primo.
- O tamanho máximo da claim Name é de 256 caracteres.

# Estrutura do Projeto

```
app/
│
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
```

# Descrição dos Arquivos e Módulos

##### app.py

Descrição:

Este arquivo contém o código principal da aplicação Flask.
Define um endpoint /validate para validar JWTs recebidos através de uma requisição POST.
Principais Componentes:

Rota /validate: Recebe um JSON com um token JWT e responde com a validade do token.
Bibliotecas Utilizadas: Flask para o servidor web e PrometheusMetrics para monitoramento.

- requirements.txt
Descrição:

Lista todas as dependências necessárias para executar a aplicação.
Inclui Flask, Prometheus Flask Exporter, PyJWT e pytest.

- Dockerfile
Descrição:

Contém as instruções para construir a imagem Docker da aplicação.
Define a imagem base, copia os arquivos, instala as dependências e define o comando de inicialização.

- utils/prime_checker.py
Descrição:

Este módulo contém a lógica para verificar se um número é primo.
Classe:

PrimeChecker
Método is_prime(num): Recebe um número inteiro e retorna True se o número for primo, caso contrário, retorna False.

- utils/jwt_validator.py
Descrição:

Este módulo contém a lógica para validação de JSON Web Tokens (JWTs).
Classe:

JWTValidator
Método validate(token): Recebe um token JWT e retorna True se o token for válido conforme regras específicas, caso contrário, retorna False.
Dependências Internas: Utiliza a classe PrimeChecker para verificar se o valor do campo Seed no JWT é um número primo.

- tests/test_app.py
Descrição:

Contém testes para a aplicação Flask, especificamente para a rota /validate.
Principais Componentes:

Testes Unitários: Verificam a funcionalidade da rota /validate com tokens válidos, inválidos e cenários onde o token está ausente.

- tests/utils/test_prime_checker.py
Descrição:

Contém testes unitários para o módulo prime_checker.py.
Principais Componentes:

Testes Unitários: Verificam a precisão do método is_prime com diversos números de entrada.

- tests/utils/test_jwt_validator.py
Descrição:

Contém testes unitários para o módulo jwt_validator.py.
Principais Componentes:

Testes Unitários: Verificam a precisão do método validate com tokens válidos e inválidos.

#  Definição
Input: Um JWT (string).  
Output: Um boolean indicando se a valido ou não.



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
