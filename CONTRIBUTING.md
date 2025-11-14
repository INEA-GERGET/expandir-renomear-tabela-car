# Como colaborar

O GERGET recebe contribuições de qualquer pessoa. Por favor, veja nossas [diretrizes para contribuição](https://github.com/INEA-GERGET/contributing). 

Espere que qualquer pull request passe por uma revisão por pares antes de ser aceito.

Para simplificar a colaboração, recomenda-se que os colaboradores regulares trabalhem em um único repositório, criando solicitações de pull entre branches em vez de entre repositórios.

O uso de fork é mais adequado para aceitar contribuições de pessoas não afiliadas a um projeto, como colaboradores de código aberto.

Não faça commits direto na main, use branches. Não faça merge sem a autorização de um owner ou um moderador. 

## Encontrou um bug?

Se você acha que encontrou um novo bug, sinta-se à vontade para registrar um problema e incluir as etapas para reproduzir o problema.
Por favor, inclua o seguinte no seu problema:
 - Seu ambiente conda ou pip (execute conda list ou pip freeze e copie/cole o resultado no problema)
 - Qualquer código (ou notebook) que você executou e que causou o problema

## Atualizando erros em scripts existentes

### Você vê um erro em um código existente? Há um erro de digitação, uma variável mal nomeada, e você sabe como corrigi-lo?
Faça a correção no código
Se você fez alterações no código, execute novamente
Faça uma cópia do branch dev_current no seu fork local
Adicione o código atualizado ao seu branch no seu fork
Abra um pull request do branch do seu fork para o branch dev_current deste repositório

## Boas práticas em Python

### Nomenclatura

Abaixo você encontra as convenções de nomeclatura mais utilizadas em Python.

**Pacotes**: Os sublinhados podem ser usados no nome do pacote e do módulo somente se isso melhorar a legibilidade.

**Variáveis e constantes**: Use o sublinhado para adicionar novas palavras às variáveis e constantes.

| Identificador  | Convenção |
| ------------- | ------------- |
| Módulo  | minúsculas  |
| Classe  | CapWords  |
| Funções  | minúsculas |
| Métodos  | minúsculas |
| Variáveis de tipo  | CapWords |
| Constantes  | MAIÚSCULAS |
| Pacotes  | minúsculas |

### Comentários

Os comentários em python devem ser feitos antes da sessão de código, explicando-o, com o uso de uma **#**. 

Certifique-se de que seus comentários sejam claros e facilmente compreensíveis para outros usuários.

Qualquer comentário que contradiga o código é pior do que nenhum comentário. Por isso, é muito importante que atualizemos o código e não nos esqueçamos de atualizar os comentários para evitar a criação de inconsistências. 

Os comentários devem ser frases completas, com a primeira letra em maiúscula. 

Um exemplo de comentário:

```python
# Imprime na tela a mensagem 
print("Bem vindo à Gerência de Gestão do Território e Informações Geoespaciais do INEA")
```

### Docstring

Ao definir uma função, módulo, classe ou método, você deve umsar uma string de documentação. Dessa forma uma docstring pode ser acessada em tempo de execução usando o atributo especial obj.__doc__ desse objeto.

Para fins de consistência, as cadeias de documentos são sempre colocadas entre aspas duplas triplas ("""). O exemplo a seguir ilustra uma docstring na função calculate_salary():

```python
def calculate_salary(hours, price=20):
    """ Return the salary according to the hours worked
    Arguments:
    hours: total hours investe
    price: price of each hours worked. Minimum price is 20 dollars
    """
    salary = hours * price
    return salary
```
