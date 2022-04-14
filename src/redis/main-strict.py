# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python e Redis."""

from redis import StrictRedis

con = StrictRedis(host='localhost', port=6379)

print(f'Conetado em: {con}')

# Deletando as chaves do banco.
for key in con.keys():
    con.delete(key)

# Exibir chaves existentes.
print(f'\nChaves existentes: {con.keys()}')

# Inserindo uma chave e valor.
print('\nCriando uma nova chave:')
con.set('chave1', 'valor1')
print(f'Chaves existentes: {con.keys()}')

# Acessando valor de uma chave.
print('Valor da chave:', con.get('chave1'))

# Criando outra chave.
print('\nCriando outra chave:')
con.set('chave2', 1)
print(f'Chaves existentes: {con.keys()}')
print('Valor da chave2:', con.get('chave2'))

# Incrementando valor da chave.
print('incrementando a chave2:', con.incr('chave2'))
print('incrementando a chave2:', con.incr('chave2'))
print('decrementando a chave2:', con.decr('chave2'))

# Removendo uma chave.
print('\nRemovendo a chave2:')
con.delete('chave2')

# Caso a chave não exista é retornado None.
print('Tentando exibir a chave que foi removida')
print('Valor da chave:', con.get('chave2'))
print(f'Chaves existentes: {con.keys()}')
