""""
    1. Considere as linguagens definidas pelas expressões regulares a seguir. Implemente, para
    cada uma das linguagens, um autômato finito que reconheça cadeias pertencentes a
    linguagem. Esse autômato não deve conter não-determinismos, transições em vazio, estados
    inacessíveis e nem estados inúteis.
    a) (ab*c*)*
    b) aaa(b | c)* | (b | c)* aaa
    c) a*b | ab*
    d) a*b* (a | ac*)
"""

class AFD:
    def __init__(self, states, symbols, transitions, initial_states, final_states):
        self.states = states
        self.symbols = symbols
        self.transitions = transitions
        self.initial_states = initial_states
        self.final_states = final_states

    def accept(self, word):
        current_state = self.initial_states  # Começando no estado inicial
        for symbol in word:  # Para cada simbolo na palavra
            if symbol in self.symbols:
                current_state = self.transitions.get((current_state, symbol))
                if current_state is None:
                    return False
            else:
                return False
        return current_state in self.final_states


if __name__ == "__main__":

    #  a) (ab*c*)*
    print("a) (ab*c*)*")
    afd_a = AFD(
        states={'q0', 'q1', 'q2'},
        symbols={'a', 'b', 'c'},
        transitions={
            ('q0', 'a'): 'q1',
            ('q1', 'a'): 'q2',
            ('q1', 'b'): 'q1',
            ('q1', 'c'): 'q1',
            ('q2', 'a'): 'q1',
            ('q2', 'b'): 'q1',
            ('q2', 'c'): 'q1'
        },
        initial_states='q0',
        final_states={'q1', 'q2'}
    )

    #  Testando o automato
    print(afd_a.accept('aaaaa'))
    print(afd_a.accept('abcbcbcbcb'))
    print(afd_a.accept('abcabcabc'))
    print(afd_a.accept('cccccc'))
    print(afd_a.accept('bbbbbbb'))

    #  b) aaa(b | c)* | (b | c)* aaa
    print("b) aaa(b | c)* | (b | c)* aaa")
    afd_b = AFD(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'},
        symbols={'a', 'b', 'c'},
        transitions={
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q4',
            ('q0', 'c'): 'q4',
            ('q1', 'a'): 'q2',
            ('q2', 'a'): 'q3',
            ('q3', 'b'): 'q3',
            ('q3', 'c'): 'q3',
            ('q4', 'b'): 'q4',
            ('q4', 'c'): 'q4',
            ('q4', 'a'): 'q5',
            ('q5', 'a'): 'q6',
            ('q6', 'a'): 'q7',
        },
        initial_states='q0',
        final_states={'q3', 'q7'}
    )

    #  Testando o automato
    print(afd_b.accept("aaabcbcbcb"))
    print(afd_b.accept("aaa"))
    print(afd_b.accept("bcbcbcbcbcaaa"))
    print(afd_b.accept("aaa"))
    print(afd_b.accept("bcbcbcbcb"))
    print(afd_b.accept("bbbbbb"))
    print(afd_b.accept("cccccc"))

    #  c) a*b | ab*
    print("c) a*b | ab*")
    afd_c = AFD(
        states={'q0q1q2', 'q1', 'q2', 'q1q4', 'q2q4', 'q4'},
        symbols={'a', 'b'},
        transitions={
            ('q0q1q2', 'a'): 'q1q4',
            ('q0q1q2', 'b'): 'q2',
            ('q1q4', 'a'): 'q1',
            ('q1q4', 'b'): 'q2q4',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2q4', 'b'): 'q4',
            ('q4', 'b'): 'q4',
        },
        initial_states='q0q1q2',
        final_states={'q0q1q2', 'q4', 'q2q4', 'q1q4', 'q2'}
    )

    # Testando o autômato
    print(afd_c.accept("aaaaaab"))
    print(afd_c.accept("abbbbb"))
    print(afd_c.accept("abababab"))
    print(afd_c.accept("aaaaaaa"))
    print(afd_c.accept("bbbbbbb"))

    #  d) a*b* (a | ac*)
    print("d) a*b* (a | ac*)")
    afd_d = AFD(
        states={'q0', 'q1', 'q2', 'q3', 'q0q2'},
        symbols={'a', 'b', 'c'},
        transitions={
            ('q0', 'a'): 'q0q2',
            ('q0', 'b'): 'q1',
            ('q1', 'a'): 'q2',
            ('q1', 'b'): 'q1',
            ('q0q2', 'a'): 'q0q2',
            ('q0q2', 'b'): 'q1',
            ('q0q2', 'c'): 'q3',
            ('q2', 'c'): 'q3',
            ('q3', 'c'): 'q3'
        },
        initial_states='q0',
        final_states={'q0q2', 'q2', 'q3'}
    )

    # Testando o autômato
    print(afd_d.accept("a"))
    print(afd_d.accept("aaabbbba"))
    print(afd_d.accept("ababababa"))
    print(afd_d.accept("accccccccc"))
    print(afd_d.accept("ababababab"))
    print(afd_d.accept("abcccccccc"))

