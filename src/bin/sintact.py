

class grammar():
    terminals = {
        "ELSE": "ELSE",
        "IF": "IF",
        "BOOL": "T",
        "INT": "T",
        "FLOAT": "T",
        "STRING": "T",
        "IDENTIFY": "V",
        "CHARCONST": "V",
        "FLOATCONST": "D",
        "INTCONST": "D",
        "PLUS": "O",
        "MINUS": "O",
        "MULTIPLICATION": "O",
        "DIVISION": "O",
        "ASIGNATION": "=",
        "BOOLCOPARISON": "B",
        "MINOR": "B",
        "MINOREQUAL": "B",
        "DIFFERENT": "B",
        "HIGHER": "B",
        "HIGHEREQUAL": "B",
        "OPENPARENTHESIS": "(",
        "CLOSEPARENTHESIS": ")",
        "OPENBRACKETS": "{",
        "CLOSEBRACKETS": "}",
        "SEMICOLON": ";",
    }

    def descendente(terminals=terminals, tokens=[]):
        parcial = ""
        secuencia = []

        try:
            for token in tokens:
                secuencia.append(
                    [f"{terminals[token[0]]}", token[1].replace(' ', '')])
        except:
            parcial += token[1]+' <-- unespected token '
            return parcial

        def NTZ(secuencia, parcial):
            print(parcial+'z')
            if secuencia[0][0] == 'O':
                parcial += f"{secuencia[0][1]} "
                del secuencia[0]
                return secuencia, parcial
            elif secuencia[0][0] == 'B':
                parcial += f"{secuencia[0][1]} "
                del secuencia[0]
                return secuencia, parcial
            else:
                parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                return secuencia, parcial

        def NTX(secuencia, parcial):
            print(parcial+'x')
            if secuencia[0][0] == 'V':
                parcial += f"{secuencia[0][1]} "
                del secuencia[0]
                return secuencia, parcial
            elif secuencia[0][0] == 'D':
                parcial += f"{secuencia[0][1]} "
                del secuencia[0]
                return secuencia, parcial
            elif secuencia[0][0] == '(':
                parcial += f"{secuencia[0][1]} "
                del secuencia[0]
                secuencia, parcial = NTX(secuencia, parcial)
                secuencia, parcial = NTZ(secuencia, parcial)
                secuencia, parcial = NTX(secuencia, parcial)
                if secuencia[0][0] == ')':
                    parcial += f"{secuencia[0][1]} "
                    del secuencia[0]
                    return secuencia, parcial
                else:
                    parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                    return secuencia, parcial

            else:
                return f'<-- token {secuencia[0][1]} no esperado'

        def NTB(secuencia, parcial):
            print(parcial+'b')
            if secuencia[0][0] == 'V':
                parcial += f"{secuencia[0][1]} "
                del secuencia[0]
                return secuencia, parcial
            elif secuencia[0][0] == 'D':
                parcial += f"{secuencia[0][1]} "
                del secuencia[0]
                return secuencia, parcial
            else:
                parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                return secuencia, parcial

        def NTA(secuencia, parcial):
            print(parcial+'a')
            try:
                if secuencia[0][0] == '=':
                    parcial += f"{secuencia[0][1]} "
                    del secuencia[0]
                    secuencia, parcial = NTB(secuencia, parcial)
                    return secuencia, parcial
                elif secuencia[0][0] == ';':
                    return secuencia, parcial
                else:
                    parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                    return secuencia, parcial
            except:
                return secuencia, parcial

        def NTS(secuencia, parcial):
            print(parcial+'s')
            try:
                if secuencia[0][0] == 'T':
                    parcial += f"{secuencia[0][1]} "
                    del secuencia[0]
                    if secuencia[0][0] == 'V':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    secuencia, parcial = NTA(secuencia, parcial)

                    if secuencia[0][0] == ';':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]

                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial

                    secuencia, parcial = NTS(secuencia, parcial)
                    return secuencia, parcial

                elif secuencia[0][0] == 'V':
                    parcial += f"{secuencia[0][1]} "
                    del secuencia[0]
                    if secuencia[0][0] == '=':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    secuencia, parcial = NTX(secuencia, parcial)
                    if secuencia[0][0] == ';':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    secuencia, parcial = NTS(secuencia, parcial)
                    return secuencia, parcial
                elif secuencia[0][0] == 'IF':
                    parcial += f"{secuencia[0][1]} "
                    del secuencia[0]
                    if secuencia[0][0] == '(':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    secuencia, parcial = NTX(secuencia, parcial)
                    if secuencia[0][0] == ')':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    if secuencia[0][0] == '{':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    secuencia, parcial = NTS(secuencia, parcial)
                    if secuencia[0][0] == '}':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    if secuencia[0][0] == 'ELSE':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    if secuencia[0][0] == '{':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    secuencia, parcial = NTS(secuencia, parcial)
                    if secuencia[0][0] == '}':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    if secuencia[0][0] == ';':
                        parcial += f"{secuencia[0][1]} "
                        del secuencia[0]
                    else:
                        parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                        return secuencia, parcial
                    secuencia, parcial = NTS(secuencia, parcial)
                    return secuencia, parcial
                elif secuencia[0][0] == '}':
                    return secuencia, parcial

                else:
                    parcial += f'{secuencia[0][1]} <-- token {secuencia[0][1]} no esperado'
                    return secuencia, parcial
            except:
                return secuencia, parcial

        def start(secuencia, parcial):

            secuencia, parcial = NTS(secuencia, parcial)
            if(len(secuencia) == 0):
                parcial += ' <-- Ejecutado con exito'
                return parcial
            else:
                return parcial

        return start(secuencia, parcial)
