def verificar_vitorias(totalvitorias):

    match totalvitorias:
        case x if x <= 10:
            Ranque = "Ferro"
        case x if 11 <= x <= 20:
            Ranque = "Bronze"
        case x if 21 <= x <= 50:
            Ranque = "Prata"
        case x if 51 <= x <= 80:
            Ranque = "Ouro"
        case x if 81 <= x <= 90:
            Ranque = "Diamante"
        case x if 91 <= x <= 100:
            Ranque = "Lendário"
        case _:
            Ranque = "Imortal"

    return Ranque


winstr = input("Quantas vitorias você teve:")
losestr = input("Quantas derrotas você teve:")
derrotas = int(losestr)
vitorias =int(winstr)

totalvitorias = vitorias - derrotas


print(f"O Herói tem de saldo de **{totalvitorias}** está no nível de **{verificar_vitorias(totalvitorias)}**")  
