class TuringMachineShiftRight:
    def __init__(self, input_str, blank_symbol='␣'):
        self.tape = list(input_str) + [blank_symbol] * 100  # espacio extra
        self.blank = blank_symbol
        self.head = 0
        self.state = 'seek_end'

    def step(self):
        if self.state == 'seek_end':
            # Buscar el final de la cadena
            if self.tape[self.head] in ['a', 'b']:
                self.head += 1
            else:
                # Retrocede una posición para empezar el desplazamiento
                self.head -= 1
                self.state = 'shift_right'

        elif self.state == 'shift_right':
            if self.head >= 0:
                current = self.tape[self.head]
                self.tape[self.head + 1] = current
                self.head -= 1
            else:
                self.state = 'write_blank'

        elif self.state == 'write_blank':
            self.tape[0] = self.blank
            self.state = 'HALT'

    def run(self):
        steps = 0
        while self.state != 'HALT' and steps < 1000:
            self.step()
            steps += 1

    def get_tape(self):
        return ''.join(self.tape).strip(self.blank)

# Ejemplo de uso
input_str = "abba"
tm = TuringMachineShiftRight(input_str)
tm.run()
print("Resultado:", tm.get_tape())
