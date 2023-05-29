import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define la gramática
grammar = CFG.fromstring("""
    A -> 's' 'w' 'i' 't' 'c' 'h' ' ' V ' ' C ' ' 'o''t''h''e''r''w''i''s''e' ' ' P ' ' 'e' 'n' 'd'
    C -> M  C1
    C1 -> ' 'C | 
    M -> 'c' 'a' 's' 'e' ' ' INT  ' ' P
    P -> Q P1
    P1 -> '+' Q P1 | '-' Q P1 | 
    Q -> S Q1
    Q1 -> '*' S Q1 | '/' S Q1 | 
    S -> V | K
    V -> let T
    T -> let T | dig T | '_' T1 | 
    T1 -> let T | dig T |
    K -> INT K1
    K1 -> '.' N | 
    INT -> '-'N | N
    N -> dig N1
    N1 -> N | 
    let -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
    dig -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")



# Create a parser with the grammar
parser = ChartParser(grammar)

# Define la sentencia a analizar


 #Switch var_1 case -10 1.5 case 1 -1-1 otherwise 10/10 end
while True:
    # Solicita la entrada del usuario
    sentence = list(input("Sentence: "))

    try:
        # Intenta generar el árbol sintáctico
        trees = list(parser.parse(sentence))
        if trees:
            for tree in trees:

                tree.pretty_print()
                tree.draw()
            break  # Si la sentencia es válida, sal del bucle
        else:
            print("Sentencia invalida. Por favor, inténtalo de nuevo.")
    except ValueError as e:
        # Muestra el mensaje de error y solicita una nueva entrada
        print("Ocurrió un error al analizar la sentencia:", e)
        print("Por favor, inténtalo de nuevo.")