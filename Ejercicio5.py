class SimulatedTuringMachineCopy:
    def __init__(self, input_str, blank_symbol='␣'):
        self.tape = list(input_str) + [blank_symbol] * 100
        self.blank = blank_symbol
        self.head = 0
        self.original = []

    def run(self):
        # Leer la palabra original y almacenarla
        while self.tape[self.head] in ['a', 'b', 'c']:
            self.original.append(self.tape[self.head])
            self.head += 1

        # Ahora copiamos la palabra al final
        for symbol in self.original:
            self.tape[self.head] = symbol
            self.head += 1

    def get_tape(self):
        return ''.join(self.tape).strip(self.blank)

# Prueba
input_str = "bb"
tm = SimulatedTuringMachineCopy(input_str)
tm.run()
print(f"Entrada: {input_str} → Salida: {tm.get_tape()}")
