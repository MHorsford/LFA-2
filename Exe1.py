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
            ('q1', 'b'): 'q1',
            ('q1', 'c'): 'q2',
            ('q2', 'c'): 'q2',
            ('q2', 'a'): 'q1',
        },
        initial_states='q0',
        final_states={'q1', 'q2'}
    )

    print(afd_a.accept('abc'))
    print(afd_a.accept('abcc'))
    print(afd_a.accept('abccc'))
    print(afd_a.accept('ac'))
    print(afd_a.accept('bcc'))

    #  b) aaa(b | c)* | (b | c)* aaa
    print("b) aaa(b | c)* | (b | c)* aaa")
    afd_b = AFD(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
        symbols={'a', 'b', 'c'},
        transitions={
            ('q0', 'a'): 'q1',
            ('q1', 'a'): 'q2',
            ('q2', 'a'): 'q3',
            ('q3', 'b'): 'q3',
            ('q3', 'c'): 'q3',
            ('q0', 'b'): 'q4',
            ('q0', 'c'): 'q4',
            ('q4', 'b'): 'q4',
            ('q4', 'c'): 'q4',
            ('q4', 'a'): 'q1'
        },
        initial_states='q0',
        final_states={'q3', 'q4'}
    )

    print(afd_b.accept("aaabaaacbcaaa"))  # True
    print(afd_b.accept("aaaaaa"))  # True
    print(afd_b.accept("aaa"))  # False
    print(afd_b.accept("bcaaa"))  # False

    #  c) a*b | ab*
    print("c) a*b | ab*")
    afd_c = AFD(
        states={'q0', 'q1', 'q2'},
        symbols={'a', 'b'},
        transitions={
            ('q0', 'a'): 'q0',
            ('q0', 'b'): 'q1',
            ('q1', 'b'): 'q1'
        },
        initial_states='q0',
        final_states={'q1'}
    )

    # Testando o autômato
    print(afd_c.accept("b"))  # True
    print(afd_c.accept("aab"))  # True
    print(afd_c.accept("abb"))  # True
    print(afd_c.accept("aa"))  # False

    #  d) a*b* (a | ac*)
    print("d) a*b* (a | ac*)")
    afd_d = AFD(
        states={'q0', 'q1', 'q2', 'q3', 'q4'},
        symbols={'a', 'b', 'c'},
        transitions={
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q2',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'b'): 'q2',
            ('q2', 'a'): 'q4',
            ('q1', 'c'): 'q3',
            ('q3', 'c'): 'q3',
            ('q3', 'a'): 'q4'
        },
        initial_states='q0',
        final_states={'q1', 'q3', 'q4'}
    )

    # Testando o autômato
    print(afd_d.accept("aaac"))  # True
    print(afd_d.accept("abca"))  # True
    print(afd_d.accept("aabc"))  # False

