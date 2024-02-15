import pyautogui as po  # Importa a biblioteca pyautogui e a renomeia como 'po'
print('-' * 26)
print('Converso De Moedas')  # Imprime um cabeçalho para o conversor de moedas
print('-' * 26)
real = float(input('Quantos reais você quer troca em Dolar? R$:'))  # Solicita ao usuário a quantidade de reais a serem trocados por dólares e armazena o valor em 'real'
dolar = real / 4.95  # Calcula a quantidade equivalente de dólares com base na taxa de conversão
# Imprime uma mensagem indicando o valor em reais e o valor equivalente em dólares
print('Você quer trocar R$: {:.2f} por USD: {:.2f}'.format(real, dolar))

conferir = str(input('Você vai querer trocar o valor acima? S/N: ')).upper()  # Solicita ao usuário uma confirmação para realizar a troca e converte a resposta para maiúsculas

if conferir == 'S':  # Verifica se o usuário confirmou a troca
    print('Só um minuto, estamos levando você para área de troca.')  # Imprime uma mensagem indicando que está redirecionando para a área de troca
    po.PAUSE = 6  # Define um intervalo de pausa de 6 segundos entre as operações
    po.press('win')  # Pressiona a tecla Windows para abrir o menu Iniciar
    po.write('Microsoft Edge')  # Escreve 'Microsoft Edge' para abrir o navegador
    po.press("ENTER")  # Pressiona a tecla Enter para confirmar a seleção do navegador
    po.PAUSE = 15  # Define um intervalo de pausa de 15 segundos para aguardar o carregamento da página
    po.write('https://wise.com/br/currency-converter/brl-to-usd-rate')  # Escreve a URL do conversor de moedas
    po.press("ENTER")  # Pressiona a tecla Enter para acessar a página
else:
    print('Não foi possível fazer a troca.')  # Imprime uma mensagem indicando que a troca não foi realizada
