# Sistema-de-Banco-
Criando e ativando ambiente virtual

PS C:\Users\joseb\Documents\Sistema de banco> python -m venv breno
PS C:\Users\joseb\Documents\Sistema de banco> breno\Scripts\activate

**Sistema de Banco com Salvamento de Extrato em TXT em Python**

Este é um sistema simples de banco implementado em Python que permite realizar operações bancárias básicas, como depósito, saque e consulta de saldo, além de salvar o extrato das transações em um arquivo de texto (.txt).

### Requisitos
- Python 3.x instalado

### Como Usar
1. Faça o download ou clone este repositório.
2. Abra o terminal e navegue até o diretório onde o arquivo `bank_system.py` está localizado.
3. Execute o arquivo `bank_system.py` digitando `python bank_system.py` no terminal.
4. Siga as instruções na tela para interagir com o sistema de banco.

### Funcionalidades
- **Depósito**: Adiciona fundos à conta bancária.
- **Saque**: Retira fundos da conta bancária.
- **Consulta de Saldo**: Exibe o saldo atual da conta bancária.
- **Salvar Extrato**: Salva todas as transações realizadas em um arquivo de texto chamado `extrato.txt`.

### Exemplo de Uso
```python
# Inicializar o sistema
python bank_system.py

# Escolher uma opção do menu
Escolha uma opção:
1. Depositar
2. Sacar
3. Consultar Saldo
4. Sair

# Realizar uma operação, por exemplo, depositar
Opção selecionada: 1
Digite o valor a depositar: 100

# O extrato é atualizado e salvo em extrato.txt
```

### Observações
- Certifique-se de ter permissões de escrita no diretório onde o arquivo `extrato.txt` será salvo.
- Este sistema é apenas uma implementação básica e pode ser estendido com mais funcionalidades, como transferências entre contas, autenticação de usuário, entre outros.

Este README fornece uma visão geral simples do sistema de banco. Sinta-se à vontade para modificar e estender conforme necessário.
