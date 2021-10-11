import re


class analizator():
    AF1_tokens = {"else": "ELSE",
                  "bool": "BOOL",
                  "int": "INT",
                  "if": "IF",
                  "float": "FLOAT",
                  "string": "STRING"}

    AF2_tokens = {"\s*([a-zA-Z]+([0-9]+[a-zA-Z]+|[0-9]+[a-zA-Z]*)+)\s*": "IDENTIFY",
                  "\s*[a-zA-Z]+\s*": "CHARCONST",
                  "\s*[0-9]+,[0-9]+\s*": "FLOATCONST",
                  "\s*[0-9]+\s*": "INTCONST"}

    AF3_tokens = {"+": "PLUS",
                  "-": "MINUS",
                  "*": "MULTIPLICATION",
                  "/": "DIVISION",
                  "=": "ASIGNATION",
                  "==": "BOOLCOPARISON",
                  "<": "MINOR",
                  "<=": "MINOREQUAL",
                  "<>": "DIFFERENT",
                  ">": "HIGHER",
                  ">=": "HIGHEREQUAL",
                  "(": "OPENPARENTHESIS",
                  ")": "CLOSEPARENTHESIS",
                  "{": "OPENBRACKETS",
                  "}": "CLOSEBRACKETS",
                  ";": "SEMICOLON"}

    def token_list(self, txt, AF1=AF1_tokens, AF2=AF2_tokens, AF3=AF3_tokens):
        i = True
        sol = []
        while i == True:
            try:
                eater = txt[0:8] or txt
                x = re.search(
                    "\s*else\s*|\s*bool \s*|\s*int \s*|\s*if\s*|\s*float \s*|\s*string \s*", eater)
                assert x.start() == 0
                txt = txt[len(x[0]):]
                sol.append(['KEYWORD', x[0]])
            except:
                try:
                    x = re.search(
                        "\s*([a-zA-Z]+([0-9]+[a-zA-Z]+|[0-9]+[a-zA-Z]*)+)\s*", txt)
                    assert x.start() == 0
                    txt = txt[len(x[0]):]
                    sol.append(['IDENTIFY', x[0]])
                except:
                    try:
                        x = re.search("\s*[a-zA-Z]+\s*", txt)
                        assert x.start() == 0
                        txt = txt[len(x[0]):]
                        sol.append(['CHARCONST', x[0]])
                    except:
                        try:
                            x = re.search("\s*[0-9]+,[0-9]+\s*", txt)
                            assert x.start() == 0
                            txt = txt[len(x[0]):]
                            sol.append(['FLOATCONST', x[0]])
                        except:
                            try:
                                x = re.search("\s*[0-9]+\s*", txt)
                                assert x.start() == 0
                                txt = txt[len(x[0]):]
                                sol.append(['NUMCONST', x[0]])
                            except:
                                try:
                                    eater = txt[0:4] or txt
                                    x = re.search(
                                        "\s*\+\s*|\s*\-\s*|\s*\*\s*|\s*/\s*|\s*=\s*|\s*==\s*|\s<s*|\s*<=\s*|\s*<>\s*|\s*>\s*|\s*>=\s*|\s*\(\s*|\s*\)\s*|\s*\{\s*|\s*\}\s*|\s*;\s*", eater)
                                    assert x.start() == 0
                                    txt = txt[len(x[0]):]
                                    sol.append(['OTHER', x[0]])
                                except:
                                    if len(txt) != 0:

                                        sol.append(['err', txt])
                                        i = False
                                    else:

                                        i = False
        for i in range(len(sol)):

            if sol[i][0] == 'KEYWORD':
                tok = sol[i][1].replace(' ', '')
                sol[i][0] = AF1[tok]
            if sol[i][0] == 'OTHER':
                tok = sol[i][1].replace(' ', '')
                sol[i][0] = AF3[tok]
        print(sol)
        return sol
