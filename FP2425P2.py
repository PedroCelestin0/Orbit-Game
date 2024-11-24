#2.1.1 - TAD posicao - representa uma posição do tabuleiro

#construtor - cria_posicao(col: str, lin: int) -> posicao
def cria_posicao(col, lin):
    """
    Cria uma posição no tabuleiro

    Paramêtros:
    - col(str): A coluna da posição, representada por uma letra
    - lin(int): A linha da posição, representada por um número

    Retorna:
    - posição: Uma tupla que representa a posição

    Levanta:
    - ValueError: Se a coluna ou a linha forem inválidas
    """
    if type(col) != str or not col.islower() or ord(col) > ord("j") or ord(col) < ord("a") or type(lin) != int or 10 < lin or lin <= 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (col, lin)

#seletor - obtem_pos_col(p: posicao) -> str
def obtem_pos_col(p):
    """
    Devolve a coluna da posição

    Paramêtro:
    - p(tuple): A posição representada por um tuplo (coluna, linha)

    Retorna:
    - coluna: Uma string que representa a coluna
    """
    return p[0]

#seletor - obtem_pos_lin(p: posicao) -> int
def obtem_pos_lin(p):
    """
    Devolve a linha da posição

    Paramêtro:
    - p(tuple): A posição representada por um tuplo (coluna, linha)

    Retorna:
    - linha: Um inteiro que representa a linha
    """
    return p[1]

#reconhecedor - eh_posicao(arg) -> bool
def eh_posicao(arg):
    """
    Verifica se o argumento é uma posição

    Paramêtro:
    - arg: Qualquer tipo de dado que vai ser verificado

    Retorna:
    - True, se o argumento for uma posição
    - False, caso contrário
    """
    return type(arg) == tuple and len(arg) == 2 and type(arg[0]) == str and arg[0].islower() and type(arg[1]) == int and arg[1] > 0

#teste - posicoes_iguais(p1, p2) -> bool
def posicoes_iguais(p1, p2):
    """
    Verifica se as posições p1 e p2 são iguais

    Paramêtros:
    - p1(tuple): Uma posição
    - p2(tuple): Outra posição

    Retorna:
    - True, se as posições forem iguais
    - False, caso contrário
    """
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

#transformador - posicao_para_str(p) -> str
def posicao_para_str(p):
    """
    Converte uma posição para uma string

    Paramêtro:
    - p(tuple): A posição representada por um tuplo (coluna, linha)

    Retorna:
    - Uma string que representa a posição
    """
    return p[0] + str(p[1])

#transformador - str_para_posicao(s: str) -> posicao
def str_para_posicao(s):
    """
    Converte uma string para uma posição

    Paramêtro:
    - s(string): A string que representa uma posição

    Retorna:
    - Um tuplo que representa a posição (coluna, linha)
    """
    return (s[0], int(s[1]))

#função de alto nível - eh_posicao_valida(p, n) -> bool
def eh_posicao_valida(p, n):
    """
    Verifica se o argumento é uma posição válida no tabuleiro

    Paramêtros:
    - p(tuplo): A posição que vai ser verificada
    - n(int): O número de órbitas do tabuleiro

    Retorna:
    - True, se o argumento for uma posição válida
    - False, caso contrário
    """
    return ord(obtem_pos_col(p)) in range(ord("a"), ord("a") + (n * 2)) and 1 <= obtem_pos_lin(p) <= (n * 2)

#função de alto nível - obtem_posicoes_adjacentes(p, n, d) -> tuple
def obtem_posicoes_adjacentes(p, n, d):
    """
    Devolve as posições adjacentes à posição inserida

    Paramêtros:
    - p(tuplo): A posição
    - n(int): O número de órbitas do tabuleiro
    - d(bool): True - considera as posições adjacentes ortogonais e diagonais; False - só as ortogonais

    Retorna:
    - Uma lista com as posições adjacentes
    """
    res = []
    pos_adj = [(0,-1), (1,0), (0,1), (-1,0)]
    if d:
        pos_adj = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]

    for i in pos_adj:
        coluna = chr(ord(obtem_pos_col(p)) + i[0])
        linha = obtem_pos_lin(p) + i[1]

        #verifica se a posição está dentro dos limites do tabuleiro
        if eh_posicao_valida((coluna, linha), n):
            res.append((coluna, linha))

    return res

def obtem_orbita(p, n):
    """
    Cálcula a orbita da posição inserida

    Paramêtros:
    - p(tuplo): A posição
    - n(int): O número de órbitas do tabuleiro

    Retorna:
    - Um inteiro que representa a órbita em que a posição se encontra
    """
    coluna = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10}
    centro = n + 0.5
    c = coluna[obtem_pos_col(p)]
    distancia_c = abs(c - centro)
    distancia_l = abs(obtem_pos_lin(p) - centro)
    return (int(max(distancia_c, distancia_l)) + 1)

#função de alto nível - ordena_posicoes(t, n) -> tuple
def ordena_posicoes(t, n):
    """
    Ordena as posições pela ordem de leitura do tabuleiro

    Paramêtros:
    - t(list): Lista das posições a serem ordenadas
    - n(int): O número de órbitas do tabuleiro

    Retorna:
    - Uma lista com as posições ordenadas pela ordem de leitura
    """
    return sorted(t, key=lambda pos: (obtem_orbita(pos, n), obtem_pos_lin(pos), obtem_pos_col(pos)))

#2.1.2 - TAD pedra - representa uma pedra no jogo

#construtor - cria_pedra_branca() -> pedra
def cria_pedra_branca():
    """
    Cria uma pedra branca que representa um jogador

    Retorna:
    - Uma string que representa uma pedra branca
    """
    return "b"

#construtor - cria_pedra_preta() -> pedra
def cria_pedra_preta():
    """
    Cria uma pedra preta que representa um jogador

    Retorna:
    - Uma string que representa uma pedra preta
    """
    return "p"

#construtor - cria_pedra_neutra() -> pedra
def cria_pedra_neutra():
    """
    Cria uma pedra neutra que representa uma posição livre

    Retorna:
    - Uma string que representa uma pedra neutra
    """
    return "n"

#reconhecedor - eh_pedra(arg) -> bool
def eh_pedra(arg):
    """
    Verifica se o argumento é uma pedra válida

    Paramêtro:
    - arg: O argumento que vamos verificar se é uma pedra

    Retorna:
    - True, se o argumento for uma pedra válida
    - False, caso contrário
    """
    return type(arg) == str and arg in ("b", "p", "n")

#reconhecedor - eh_pedra_branca(p) -> bool
def eh_pedra_branca(p):
    """
    Verifica se a pedra é uma pedra branca

    Paramêtro:
    - p(str): A pedra

    Retorna:
    - True, se for uma pedra branca
    - False, caso contrário
    """
    return type(p) == str and p == "b"

#reconhecedor - eh_pedra_preta(p) -> bool
def eh_pedra_preta(p):
    """
    Verifica se a pedra é uma pedra preta

    Paramêtro:
    - p(str): A pedra

    Retorna:
    - True, se for uma pedra preta
    - False, caso contrário
    """
    return type(p) == str and p == "p"

#teste - pedras_iguais(p1, p2) -> bool
def pedras_iguais(p1, p2):
    """
    Verifica se as pedras são iguais

    Paramêtros:
    - p1(tuple): Uma pedra
    - p2(tuple): Outra pedra

    Retorna:
    - True, se as pedras forem iguais
    - False, caso contrário
    """
    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2

#transformador - pedra_para_str(p) -> str
def pedra_para_str(p):
    """
    Converte a representação de uma pedra para um caracter

    Paramêtro:
    - p(str): Representação da pedra ("p" para preta, "b" para branca, "n" para neutra)

    Retorna:
    - Uma string que reperesenta a pedra ("X" para preta, "O" para branca, " " para neutra)
    """
    if eh_pedra_branca(p):
        return "O"
    elif eh_pedra_preta(p):
        return "X"
    else:
        return " "
    
#função de alto nível - eh_pedra_jogador(p) -> bool
def eh_pedra_jogador(p):
    """
    Verifica se é uma pedra de um jogador
    Paramêtro:
    - p(str): Uma pedra

    Retorna:
    - True, se p é uma pedra de um jogador
    - False, caso contrário
    """
    return eh_pedra_branca(p) or eh_pedra_preta(p)

#função de alto nível - pedra_para_int(p) -> int
def pedra_para_int(p):
    """
    Converte a representação de uma pedra para um inteiro

    Paramêtro:
    - p(str): Representação da pedra ("p" para preta, "b" para branca, "n" para neutra)

    Retorna:
    - Um inteiro que reperesenta a pedra ("1" para preta, "-1" para branca, "0" para neutra)
    """
    if eh_pedra_preta(p):
        return 1
    elif eh_pedra_branca(p):
        return -1
    else:
        return 0

#2.1.3 - TAD tabuleiro - representa o tabuleiro do jogo

#construtor - cria_tabuleiro_vazio(n) -> tabuleiro
def cria_tabuleiro_vazio(n):
    """
    Cria um tabuleiro vazio com n orbitas

    Paramêtro:
    - n(int): O número de órbitas do tabuleiro

    Retorna:
    - Uma lista de listas que representa o tabuleiro vazio

    Levanta:
    - ValueError: Se n não for um inteiro entre 2 e 5
    """
    if type(n) != int or not 2 <= n <= 5:
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")
    
    tab = []
    for i in range(2 * n):
        l = [cria_pedra_neutra()] * (2 * n)
        tab.append(l)
    return tab

#pega na posição e transforma num tuplo de coordenadas ex: a1 = (0,0)
def converte_para_coord(p):
    """
    Converte uma posição (coluna, linha) para coordenadas numericas

    Paramêtro:
    - p(tuple): A posição

    Retorna:
    - Um tuplo com as coordenadas correspondestes a posição no tabuleiro
    """
    letra_para_num = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9}

    return (obtem_pos_lin(p) - 1, letra_para_num[obtem_pos_col(p)])

#transforma um tuplo de coordenadas de novo para a sua representação inicial ex: (0,0) = a1
def converte_para_pos(p):
    """
    Converte coordenadas numericas para a representação original da posição

    Paramêtro:
    - p(tuple): A coordenadas

    Retorna:
    - Um tuplo que representa a posição
    """
    num_para_letras = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j"}

    return (num_para_letras[p[1]], p[0] + 1)

#construtor - cria_tabuleiro_(n, tp, tb) -> tabuleiro
def cria_tabuleiro(n, tp, tb):
    """
    Cria um tabuleiro com n orbitas com pedras pretas e brancas

    Paramêtros:
    - n(int): O número de órbitas do tabuleiro
    - tp(tuple): Tuplo com todas as posições das pedras pretas
    - tb(tuple): Tuplo com todas as posições das pedras brancas

    Retorna:
    - Uma lista de listas que representa o tabuleiro 

    Levanta:
    - ValueError: Caso algum dos argumentos fornecidos for inválido
    """
    if type(n) != int or not 2 <= n <= 5 or type(tp) != tuple or type(tb) != tuple:
        raise ValueError("cria_tabuleiro: argumentos invalidos")
    for i in tp:
        if not eh_posicao_valida(i, n):
            raise ValueError("cria_tabuleiro: argumentos invalidos")
    for j in tb:
        if not eh_posicao_valida(j, n):
            raise ValueError("cria_tabuleiro: argumentos invalidos")

    tab = cria_tabuleiro_vazio(n)
    for i in tp:
        l, c = converte_para_coord(i)
        tab[l][c] = cria_pedra_preta()

    for j in tb:
        l, c = converte_para_coord(j)
        tab[l][c] = cria_pedra_branca()

    return tab

#construtor - cria_copia_tabuleiro_(t) -> tabuleiro
def cria_copia_tabuleiro(t):
    """
    Cria uma cópia do tabuleiro

    Paramêtro:
    - t(list): tabuleiro original

    Retorna:
    - Uma lista de listas que represnta uma cópia do tabuleiro
    """
    novo_tab = []
    for l in t:
        nova_l = []
        for pos in l:
            nova_l.append(pos)
        novo_tab.append(nova_l)
    
    return novo_tab

#seletor - obtem_numero_orbitas(t) -> int
def obtem_numero_orbitas(t):
    """
    Obtém o número de órbitas do tabuleiro

    Paramêtro:
    - t(list): tabuleiro

    Retorna:
    - Um inteiro que representa o número de órbitas do tabuleiro
    """
    return (len(t))//2

#seletor - obtem_pedra(t, p) -> pedra
def obtem_pedra(t, p):
    """
    Obtém qual a pedra da posição inserida

    Paramêtros:
    - t(list): tabuleiro
    - p(tuple): posição

    Retorna:
    - Uma string que representa qual pedra está na posição
    """
    l, c = converte_para_coord(p)
    return t[l][c]

#seletor - obtem_linha_horizontal(t, p) -> tuple
def obtem_linha_horizontal(t, p):
    """
    Obtém todas as posições e pedras da mesma linha da pedra inserida

    Paramêtros:
    - t(list): tabuleiro
    - p(tuple): posição

    Retorna:
    - Uma lista de tuplos que contem as posições e a pedra que está nessa posição
    """
    linhas = ()
    l = obtem_pos_lin(p)
    for i in range(ord("a"), ord("a") + len(t)):
        linhas += (((chr(i), l), obtem_pedra(t, cria_posicao(chr(i), l))),)
    return linhas

#seletor - obtem_linha_vertical(t, p) -> tuple
def obtem_linha_vertical(t, p):
    """
    Obtém todas as posições e pedras da mesma coluna da pedra inserida

    Paramêtros:
    - t(list): tabuleiro
    - p(tuple): posição

    Retorna:
    - Uma lista de tuplos que contem as posições e a pedra que está nessa posição
    """
    colunas = ()
    c = obtem_pos_col(p)
    for i in range(1, len(t) + 1):
        colunas += (((c, i), obtem_pedra(t, cria_posicao(c, i))),)
    return colunas

#seletor - obtem_linha_diagonais(t, p) -> tuple, tuple
def obtem_linhas_diagonais(t, p):
    """
    Obtém todas as posições e pedras das diagonais da pedra inserida

    Paramêtros:
    - t(list): tabuleiro
    - p(tuple): posição

    Retorna:
    - Um tuplo que contem duas listas uma que contem as posições e a pedra que está nessa posição da diagonal e outra da antidiagonal
    """
    l, c = converte_para_coord(p)
    diagonal, antidiagonal = [], []
    num_para_letras = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j"}

    #determina a diagonal
    lin, col = l, c
    while lin >= 0 and col >= 0:                           #calcula todas as posições para cima e para a esquerda da inserida
        diagonal += [((num_para_letras[col], lin + 1), obtem_pedra(t, cria_posicao(str(num_para_letras[col]), lin + 1))),]
        lin -= 1
        col -= 1
    lin, col = l + 1, c + 1
    while lin < len(t) and col < len(t):                   #calcula todas as posições para baixo e para a direita da inserida
        diagonal += [((num_para_letras[col], lin + 1), obtem_pedra(t, cria_posicao(str(num_para_letras[col]), lin + 1))),]
        lin += 1
        col += 1

    #determina a antidiagonal
    lin, col = l, c
    while lin >= 0 and col < len(t):                       #calcula todas as posições para cima e para a direita da inserida
        antidiagonal += [((num_para_letras[col], lin + 1), obtem_pedra(t, cria_posicao(str(num_para_letras[col]), lin + 1))),]
        lin -= 1
        col += 1
    lin, col = l + 1, c - 1
    while lin < len(t) and col >= 0:                       #calcula todas as posições para baixo e para a direita da inserida
        antidiagonal += [((num_para_letras[col], lin + 1), obtem_pedra(t, cria_posicao(str(num_para_letras[col]), lin + 1))),]
        lin += 1
        col -= 1

    diagonal.sort(key=lambda x: (obtem_pos_col(x[0]), obtem_pos_lin(x[0])))
    antidiagonal.sort(key=lambda x: (obtem_pos_col(x[0]), obtem_pos_lin(x[0])))

    return diagonal, antidiagonal

#seletor - obtem_posicoes_pedra(t, j) -> tuple
def obtem_posicoes_pedra(t, j):
    """
    Obtém todas as posições ocupadas pelas pedras do tipo inserido

    Paramêtros:
    - t(list): tabuleiro
    - j(str): representação de uma pedra

    Retorna:
    - Uma lista com as posições ocupadas pelo jogador inserido
    """
    pos_pedras = ()
    for i in range(len(t)):
        for m in range(len(t)):
            if t[i][m] == j:
                pos_pedras += (converte_para_pos((i, m)),)

    return ordena_posicoes(pos_pedras, obtem_numero_orbitas(t))

#modificador - coloca_pedra(t, p, j) -> tabuleiro
def coloca_pedra(t, p, j):
    """
    Coloca uma pedra na posição inserida

    Paramêtros:
    - t(list): tabuleiro
    - p(tuple): posição onde a pedra vai ser colocada
    - j(str): representação de uma pedra

    Retorna:
    - o tabuleiro já alterado com a nova pedra na posição inserida
    """
    l, c = converte_para_coord(p)
    t[l][c] = j
    return t

#modificador - remove_pedra(t, p) -> tabuleiro
def remove_pedra(t, p):
    """
    Remove a pedra na posição inserida

    Paramêtros:
    - t(list): tabuleiro
    - p(tuple): posição onde a pedra vai ser removida

    Retorna:
    - o tabuleiro já alterado sem a pedra
    """
    l, c = converte_para_coord(p)
    t[l][c] = 0
    return t

#reconhecedor - eh_tabuleiro(arg) -> bool
def eh_tabuleiro(arg):
    """
    Verifica se o argumento é um tabuleiro válido

    Paramêtro:
    - arg: O argumento que vamos verificar se é um tabuleiro

    Retorna:
    - True, se o argumento for um tabuleiro válido
    - False, caso contrário
    """
    if type(arg) != list or not 2 <= obtem_numero_orbitas(arg) <= 5:
        return False
    for i in arg:
        if len(i) != (obtem_numero_orbitas(arg) * 2) or type(i) != list:
            return False
    return True

#teste - tabuleiros_iguais(t1, t2) -> bool
def tabuleiros_iguais(t1, t2):
    """
    Verifica se os tabuleiros são iguais

    Paramêtros:
    - t1(list): Um tabuleiro
    - t2(list): Outro tabuleiro

    Retorna:
    - True, se os tabuleiros são iguais
    - False, caso contrário
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2

#transformador - tabuleiro_para_str(t) -> str
def tabuleiro_para_str(t):
    """
    Converte um tabuleiro (representado por uma lista de listas) em uma cadeia de caracteres

    A função transforma o tabuleiro numa representação gráfica onde:
    - As casas jogáveis são separadas por "-"
    - As linhas do tabuleiro são separadas por uma linha de "|"

    Parâmetro:
    - t(list): O tabuleiro que é uma lista de listas

    Retorna:
    - Uma string que representa graficamente o tabuleiro
    """
    #cria a linha inicial com as letras correspondentes de cada coluna
    tab = "    "
    for i in range(len(t) - 1):
        tab += chr(ord("a") + i) + "   "
    tab += chr(ord("a") + len(t) - 1) + "\n"

    for j in range(len(t)):
        
        #adiciona o número correspondente à linha
        if j != 9:
            tab += "0" + str(j + 1) + " "
        else:
            tab += str(j + 1) + " "

        #transforma cada posição na sua string correspondente
        for m in range(len(t)):
            tab += "[" + pedra_para_str(t[j][m]) + "]"

            #adiciona "-" entre cada posição
            if m < len(t) - 1:
                tab += "-"

        #cria uma linha de separação entre linhas com "|"
        if j < len(t) - 1:
            tab += "\n    "
            for n in range(len(t) - 1):
                tab += "|   "
            tab += "|\n"

    return tab
               
#função de alto nível - move_pedra(t, p1, p2) -> tabuleiro
def move_pedra(t, p1, p2):
    """
    Move a pedra de uma posição para outra

    Paramêtros:
    - t(list): tabuleiro
    - p1(tuple): posição inicial da pedra
    - p2(tuple): posição final da pedra

    Retorna:
    - o tabuleiro já alterado
    """
    t = coloca_pedra(t, p2, obtem_pedra(t, p1))
    return coloca_pedra(t, p1, cria_pedra_neutra())

def sentido_horario(t, p):
    """
    Ordena as posições da mesma órbita pelo sentido horário

    Paramêtros:
    - t(list): tabuleiro
    - p(tuple): posição

    Retorna:
    - Uma lista de posições ordenadas pelo sentifo horário
    """
    n = obtem_orbita(p, obtem_numero_orbitas(t))
    res = []
    orbitas = obtem_numero_orbitas(t)
    comp = int(orbitas * 2)

    for i in range(1, n + 5):
        linha_cima = i - 1
        linha_baixo = comp - i
        coluna_esquerda = i - 1
        coluna_direita = comp - i
        pos = []

        #percorre a linha de cima, da esquerda para a direita
        for coluna in range(coluna_esquerda, coluna_direita + 1):
            pos.append((linha_cima, coluna))

        #percorre a coluna da direita, de cima para baixo
        for linha in range(linha_cima + 1, linha_baixo + 1):
            pos.append((linha, coluna_direita))

        #percorre a linha de baixo, da direita para a esquerda
        for coluna in range(coluna_direita - 1, coluna_esquerda - 1, -1):
            pos.append((linha_baixo, coluna))

        #percorre a coluna mais a esquerda de baixo para cima
        for linha in range(linha_baixo - 1, linha_cima, -1):
            pos.append((linha, coluna_esquerda))

        if converte_para_coord(p) in pos:
            break

    for i in pos:
        res += [converte_para_pos(i)]
        
    return res

#função de alto nível - obtem_posicao_seguinte(t, p, s) -> posicao
def obtem_posicao_seguinte(t, p, s):
    """
    Obtém a posição seguinte da pedra inserida na mesma órbita, ou pelo sentido horário ou sentido anti-horário

    Paramêtros:
    - t(list): tabuleiro
    - p(tuple): posição
    - s(bool): True se o movimento for no sentido horário ou False se for no sentifo anti-horário

    Retorna:
    - Um tuplo que representa a posição seguinte conforme o sentido especificado
    """
    n = obtem_numero_orbitas(t)
    orbita_p = obtem_orbita(p, n)                                         #calcula a órbita da posição inserida
    posicoes = sentido_horario(t, p)
    pos = []

    #cria uma lista com todas as posições da mesma órbita que a posição inserida
    for i in posicoes:
        if obtem_orbita(i, obtem_numero_orbitas(t)) == orbita_p:
            pos += [i]
    
    indices = len(pos) - 1
    for j in range(len(pos)):
        if pos[j] == p:
            if s:
                if pos[j] != pos[indices]:                                #caso a posição inserida não seja a última da lista
                    return pos[j + 1]
                else:
                    return pos[0]                                         #se a posição for a última da lista retorna a 1º da lista
                
            else:
                if pos[j] != pos[0]:                                      #caso a posição inserida não seja a primeira da lista
                    return pos[j - 1]
                else:
                    return pos[indices]                                   #se a posição for a 1º da lista retorna a última da lista
        
#função de alto nível - roda_tabuleiro(t) -> tabuleiro
def roda_tabuleiro(t):
    """
    Roda todas as pedras do tabuleiro no sentido anti-horário nas respetivas órbitas

    Paramêtro:
    - t(list): tabuleiro

    Retorna:
    - Uma lista de listas que é o tabuleiro já rotacionado
    """
    #retorna uma posição de cada orbita do tabuleiro
    def orbitas(n):
        """
        Retorna um tuplo com uma posição de cada órbita

        Paramêtro:
        - n(int): O número de órbitas do tabuleiro

        Retorna:
        - Um tuplo com uma posição de cada órbita
        """
        if n == 2:
            return (cria_posicao("b", 2), cria_posicao("a", 1))
        elif n == 3:
            return (cria_posicao("c", 3), cria_posicao("b", 2), cria_posicao("a", 1))
        elif n == 4:
            return (cria_posicao("d", 4), cria_posicao("c", 3), cria_posicao("b", 2), cria_posicao("a", 1))
        elif n == 5:
            return (cria_posicao("e", 5), cria_posicao("d", 4), cria_posicao("c", 3), cria_posicao("b", 2), cria_posicao("a", 1))

    for i in orbitas(obtem_numero_orbitas(t)):
        orbita = sentido_horario(t, i)                                    #cria uma lista com todas as posições da mesma órbita
        pedra1 = obtem_pedra(t, i)                                        #guarda o valor da 1º pedra

        #move as pedras para a posição seguinte
        for j in range(len(orbita) - 1):
            pedra = obtem_pedra(t, orbita[j + 1])
            coloca_pedra(t, orbita[j], pedra)
        
        coloca_pedra(t, orbita[-1], pedra1)                               #coloca a 1º peça em ultimo
    
    return t

#função de alto nível - verifica_linha_pedras(t, p, j, k) -> bool
def verifica_linha_pedras(t, p, j, k):
    """
    Verifica se há uma linha com pelo menos k pedras iguais consecutivas

    Paramêtros:
    - t(list): Tabuleiro
    - p(tuple): Posição
    - j(str): Representação da pedra
    - k(int): Número mínimo de pedras consecutivas

    Retorna:
    - True, se existe uma linha com pelo menos k pedras iguais consecutivas
    - False, caso contrário
    """
    #verifica se a posição inserida tem uma peça do jogador
    if obtem_pedra(t, p) != j:
        return False
    
    lil = obtem_linha_horizontal(t, p)
    col = obtem_linha_vertical(t, p)
    dia, antidia = obtem_linhas_diagonais(t, p)

    def posicoes(tuplo):
        """
        Remove o valor da pedra de cada posição

        Paramêtro:
        - tuplo(tuple): Tuplo que contem as posições e a pedra que esta tem

        Retorna:
        - Um novo tuplo que contem só as posições
        """
        n_tuplo = ()
        for t in tuplo:
            n_tuplo += (t[0],)
        return n_tuplo

    #cria tuplos com todas as posições da mesma linha, coluna e diagonais da posição inserida
    linha = posicoes(lil)
    coluna = posicoes(col)
    diag = posicoes(dia)
    antidiag = posicoes(antidia)

    def contador(pos):
        """
        Conta a sequencia de pedras consecutivas

        Paramêtro:
        - pos(tuple): Tuplo que contem as posições

        Retorna:
        - True, se existe uma sequencia com pelo menos k pedras iguais consecutivas
        - False, caso contrário
        """
        contador = 0
        sequencia = []

        for i in pos:

            if obtem_pedra(t, i) == j:
                contador += 1
                sequencia += [i]
                if contador == k and p in sequencia:
                    return True
                
            else:
                contador = 0
                sequencia = []
        
        return False
    
    if contador(linha) or contador(coluna) or contador(diag) or contador(antidiag):
        return True
    
    else:
        return False
    
#função 2.2.1 - eh_vencedor(t, j) -> bool
def eh_vencedor(t, j):
    """
    Verifica se o jogador ganhou o jogo

    Paramêtro:
    - t(list): Tabuleiro
    - j(str): Representação da pedra

    Retorna:
    - True, se o jogador ganhou
    - False, caso contrário
    """
    posicoes = sentido_horario(t, cria_posicao("a", 1))
    for i in posicoes:
            if verifica_linha_pedras(t, i, j, (obtem_numero_orbitas(t) * 2)):
                return True
    
    return False

#função 2.2.2 - eh_fim_jogo(t) -> bool
def eh_fim_jogo(t):
    """
    Verifica se o jogo acabou

    Paramêtro:
    - t(list): Tabuleiro

    Retorna:
    - True, se o jogado terminou
    - False, caso contrário
    """
    if eh_vencedor(t, cria_pedra_branca()):
        return True
    elif eh_vencedor(t, cria_pedra_preta()):
        return True
    elif obtem_posicoes_pedra(t, cria_pedra_neutra()) == ():
        return True
    return False

#função 2.2.3 - escolhe_posicao_manual(t) -> posicao
def escolhe_movimento_manual(t):
    """
    Pede ao jogador para inserir uma posição livre

    Paramêtro:
    - t(tist): Tabuleiro

    Retorna:
    - Uma string que representa a posição escolhida pelo jogador
    """    
    #pede ao jogador para inserir uma posição do tabuleiro
    pos = input("Escolha uma posicao livre:")

    while ord(pos[0]) not in tuple(range(ord("a"), ord("a") + obtem_numero_orbitas(t) * 2)) \
      and pos[1] not in tuple(range(1, obtem_numero_orbitas(t) * 2)) or obtem_pedra(t, str_para_posicao(pos)) != cria_pedra_neutra():

        #pede ao jogador para inserir uma posição do tabuleiro
        pos = input("Escolha uma posicao livre:")

    return str(pos)

#função 2.2.4 - escolhe_posicao_auto(tm j, lvl) -> posicao
def escolhe_movimento_auto(t, j, lvl):
    """
    Escolhe automaticamente uma posição com base na dificuldade escolhida pelo jogador

    Paramêtro:
    - t(list): Tabuleiro
    - j(str): Representação da pedra
    - lvl(str): Nível de dificuldade

    Retorna:
    - Uma string que representa a posição escolhida
    """
    pos_livre = obtem_posicoes_pedra(t, cria_pedra_neutra())

    if lvl == "facil":
        
        #simula um tabuleiro, coloca uma pedra numa posição livre e roda o mesmo
        for i in pos_livre:
            tab = cria_copia_tabuleiro(t)
            coloca_pedra(tab, i, j)
            tab = roda_tabuleiro(tab)

            #acha as posições adjacentes a pedra inserida e verifica se essa pedra ficou adjacente a uma igual a colocada
            pos_adj = obtem_posicoes_adjacentes(i, obtem_numero_orbitas(t), True)
            for m in pos_adj:
                if pedras_iguais(obtem_pedra(tab, m), j):
                    return posicao_para_str(i)
            
            #caso não haja uma posição livre adjacente a uma pedra própria, joga na 1º posição livre em ordem de leitura
            posicoes = ordena_posicoes(pos_livre, obtem_numero_orbitas(t))
            return posicao_para_str(posicoes[0])
        
    if lvl == "normal":

        if j == cria_pedra_preta():
            adv = cria_pedra_branca()
        elif j == cria_pedra_branca():
            adv = cria_pedra_preta()

        for L in range(obtem_numero_orbitas(t) * 2, 0, -1):
            for pos in ordena_posicoes(pos_livre, obtem_numero_orbitas(t)):
                
                #encontra a melhor posição para fazer uma linha com L peças seguidas
                tab = cria_copia_tabuleiro(t)
                coloca_pedra(tab, pos, j)
                tab = roda_tabuleiro(tab)
                if verifica_linha_pedras(tab, pos, j, L):
                    return posicao_para_str(pos)
       
            for pos in ordena_posicoes(pos_livre, obtem_numero_orbitas(t)):

                #caso seja necessário, bloqueia o adversário
                tab = cria_copia_tabuleiro(t)
                coloca_pedra(tab, pos, adv)
                tab = roda_tabuleiro(tab)
                tab = roda_tabuleiro(tab)
                if verifica_linha_pedras(tab, pos, adv, L):
                    return posicao_para_str(pos)
            
            #caso não haja uma posição livre adjacente a uma pedra própria, joga na 1º posição livre em ordem de leitura
            posicoes = ordena_posicoes(pos_livre, obtem_numero_orbitas(t))
            return posicao_para_str(posicoes[0])

#função 2.2.5 - orbito(n, modo, jog) -> int
def orbito(n, modo, jog):
    """
    Executa o jogo orbito

    Paramêtro:
    - n(int): Número de órbitas do tabuleiro
    - modo(str): Modo de jogo
    - jog(str): Símbolo que representa a pedra do jogador

    Retorna:
    - Uma mensagem a dizer quem ganhou o jogo

    Levanta:
    - ValueError: Caso algum dos argumentos fornecidos for inválido
    """    
    if type (n) != int or not 2 <= n <= 5 or modo not in ("facil", "normal", "2jogadores") or jog not in ("X", "O"):
        raise ValueError("orbito: argumentos invalidos")
    
    print("Bem-vindo ao ORBITO-2.")
    if modo == "facil":
        print("Jogo contra o computador (facil).")
    elif modo == "normal":
        print("Jogo contra o computador (normal).")
    else:
        print("Jogo para dois jogadores.")

    if modo == "facil" or modo == "normal":
        if jog == "X":
            print("O jogador joga com 'X'.")
            t = cria_tabuleiro_vazio(n)
            print(tabuleiro_para_str(t))

            while not eh_fim_jogo(t):

                print("Turno do jogador.")
                pos = escolhe_movimento_manual(t)
                t = coloca_pedra(t, str_para_posicao(pos), cria_pedra_preta())
                t = roda_tabuleiro(t)
                print(tabuleiro_para_str(t))

                if eh_vencedor(t, cria_pedra_branca()):
                    print("DERROTA")
                    return -1
                
                if eh_fim_jogo(t):
                    print("EMPATE")
                    return 0

                print("Turno do computador (" + modo + "):")
                pos = escolhe_movimento_auto(t, cria_pedra_branca(), modo)
                t = coloca_pedra(t, str_para_posicao(pos), cria_pedra_branca())
                t = roda_tabuleiro(t)
                print(tabuleiro_para_str(t))

                if eh_vencedor(t, cria_pedra_preta()):
                    print("VITORIA")
                    return 1
                
                if eh_fim_jogo(t):
                    print("EMPATE")
                    return 0
                
        if jog == "O":
            print("O jogador joga com 'O'.")
            t = cria_tabuleiro_vazio(n)
            print(tabuleiro_para_str(t))

            while not eh_fim_jogo(t):

                print("Turno do computador (" + modo + "):")
                pos = escolhe_movimento_auto(t, cria_pedra_preta(), modo)
                t = coloca_pedra(t, str_para_posicao(pos), cria_pedra_preta())
                t = roda_tabuleiro(t)
                print(tabuleiro_para_str(t))

                if eh_vencedor(t, cria_pedra_branca()):
                    print("VITORIA")
                    return -1
                
                if eh_fim_jogo(t):
                    print("EMPATE")
                    return 0

                print("Turno do jogador.")
                pos = escolhe_movimento_manual(t)
                t = coloca_pedra(t, str_para_posicao(pos), cria_pedra_branca())
                t = roda_tabuleiro(t)
                print(tabuleiro_para_str(t))

                if eh_vencedor(t, cria_pedra_preta()):
                    print("DERROTA")
                    return 1
                
                elif eh_fim_jogo(t):
                    print("EMPATE")
                    return 0
                
    else:
        t = cria_tabuleiro_vazio(n)
        print(tabuleiro_para_str(t))
        
        while not eh_fim_jogo(t):

            print("Turno do jogador 'X'.")
            pos = escolhe_movimento_manual(t)
            t = coloca_pedra(t, str_para_posicao(pos), cria_pedra_preta())
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))

            if eh_vencedor(t, cria_pedra_branca()):
                print("VITORIA DO JOGADOR 'O'")
                return -1
                
            if eh_fim_jogo(t):
                print("EMPATE")
                return 0
            
            print("Turno do jogador 'O'.")
            pos = escolhe_movimento_manual(t)
            t = coloca_pedra(t, str_para_posicao(pos), cria_pedra_branca())
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))

            if eh_vencedor(t, cria_pedra_preta()):
                print("VITORIA DO JOGADOR 'X'")
                return 1
                
            if eh_fim_jogo(t):
                print("EMPATE")
                return 0
            