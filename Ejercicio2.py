class TuringMachineDuplicateZeros:
    def __init__(self, input_str, blank_symbol='␣'):
        self.tape = list(input_str) + [blank_symbol] * 100
        self.blank = blank_symbol
        self.original_length = len(input_str)
        self.state = 'copy'
        self.source_index = self.original_length - 1  # Último 0 original
        self.target_index = self.original_length * 2 - 1  # Último lugar de la duplicación

    def step(self):
        if self.state == 'copy':
            if self.source_index >= 0:
                if self.tape[self.source_index] == '0':
                    self.tape[self.target_index] = '0'
                    self.source_index -= 1
                    self.target_index -= 1
                else:
                    self.source_index -= 1  # ignorar blancos si hay
            else:
                self.state = 'HALT'

    def run(self):
        steps = 0
        while self.state != 'HALT' and steps < 1000:
            self.step()
            steps += 1

    def get_tape(self):
        return ''.join(self.tape).strip(self.blank)

# Ejemplo
input_str = "000"
tm = TuringMachineDuplicateZeros(input_str)
tm.run()
print("Resultado:", tm.get_tape())  # Esperado: 000000
