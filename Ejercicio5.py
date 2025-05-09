class TuringMachineCopyABC:
    def __init__(self, input_str, blank_symbol='␣'):
        self.tape = list(input_str) + [blank_symbol] * 100
        self.blank = blank_symbol
        self.head = 0
        self.state = 'mark_next'
        self.symbol_to_copy = None
        self.copy_pos = len(input_str)  # donde empieza la copia

    def step(self):
        if self.state == 'mark_next':
            # Buscar el siguiente símbolo sin marcar
            symbol = self.tape[self.head]
            if symbol == 'a':
                self.tape[self.head] = 'A'
                self.symbol_to_copy = 'a'
                self.state = 'copy_symbol'
                self.head += 1
            elif symbol == 'b':
                self.tape[self.head] = 'B'
                self.symbol_to_copy = 'b'
                self.state = 'copy_symbol'
                self.head += 1
            elif symbol == 'c':
                self.tape[self.head] = 'C'
                self.symbol_to_copy = 'c'
                self.state = 'copy_symbol'
                self.head += 1
            elif symbol in ['A', 'B', 'C']:
                self.head += 1
            elif symbol == self.blank:
                self.state = 'restore'
                self.head = 0

        elif self.state == 'copy_symbol':
            # Escribir copia al final
            self.tape[self.copy_pos] = self.symbol_to_copy
            self.copy_pos += 1
            self.head = 0
            self.state = 'mark_next'

        elif self.state == 'restore':
            # Restaurar letras marcadas
            symbol = self.tape[self.head]
            if symbol == 'A':
                self.tape[self.head] = 'a'
                self.head += 1
            elif symbol == 'B':
                self.tape[self.head] = 'b'
                self.head += 1
            elif symbol == 'C':
                self.tape[self.head] = 'c'
                self.head += 1
            elif symbol in ['a', 'b', 'c']:
                self.head += 1
            else:
                self.state = 'HALT'

    def run(self):
        steps = 0
        while self.state != 'HALT' and steps < 1000:
            self.step()
            steps += 1

    def get_tape(self):
        return ''.join(self.tape).strip(self.blank)

# Prueba
input_str = "aabca"
tm = TuringMachineCopyABC(input_str)
tm.run()
print(f"Entrada: {input_str} → Salida: {tm.get_tape()}")
