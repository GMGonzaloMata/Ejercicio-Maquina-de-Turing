class TuringMachineParity:
    def __init__(self, input_str, blank_symbol='␣'):
        self.tape = list(input_str) + [blank_symbol] * 10
        self.head = 0
        self.blank = blank_symbol
        self.state = 'even'  # Empezamos asumiendo paridad par
        self.finished = False

    def step(self):
        symbol = self.tape[self.head]

        if symbol == '1':
            self.state = 'odd' if self.state == 'even' else 'even'
            self.head += 1

        elif symbol == '0':
            self.head += 1  # ignoramos los ceros

        elif symbol == self.blank:
            # Escribimos el bit de paridad
            self.tape[self.head] = '0' if self.state == 'even' else '1'
            self.finished = True

    def run(self):
        steps = 0
        while not self.finished and steps < 100:
            self.step()
            steps += 1

    def get_tape(self):
        return ''.join(self.tape).strip(self.blank)

# Ejemplos
for w in ["", "0", "1", "11", "101", "1110", "1111"]:
    tm = TuringMachineParity(w)
    tm.run()
    print(f"Entrada: {w.ljust(5)} → Salida: {tm.get_tape()}")
