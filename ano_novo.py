#FELIZ 2024 DO PAPAI BONEL

import random

def mensagens_2024():
    mensagens = [
        "Engenharia de requisitos é obrigatória para o sucesso do projeto!",
        "Engenharia de software é o método ciêntifico para o desenvolvimento de sistemas",
        "Evite gambiarras nos seus projetos!",
        "Estude sistemas de apoio à decisão!",
        "Lembre-se da garantia da qualidade!",
        "Sei que vc é gênio/a, mas teste o que desenvolveu!"
    ]

    #Aleatorizando as mensagens
    random.shuffle(mensagens)

    print("FELIZ 2024! Muita saúde, paz e amor! E....")

    #Exibindo as mensagens em ordem aleatória
    #Faça o download no meu GitHub, execute e veja o resultado
    #Fique à vontade para alterar o código, testar e compartilhar
    for mensagem in mensagens:
        print(mensagem)

# Chamando a função para exibir as mensagens de Ano Novo
mensagens_2024()
