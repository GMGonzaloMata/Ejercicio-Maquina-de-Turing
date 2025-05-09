class TuringMachineAccept_01n0:
    def __init__(self, input_str, blank_symbol='␣'):
        self.tape = list(input_str) + [blank_symbol]
        self.head = 0
        self.blank = blank_symbol
        self.state = 'q0'
        self.accepted = False

    def step(self):
        symbol = self.tape[self.head]

        if self.state == 'q0':
            if symbol == '0':
                self.head += 1
                self.state = 'q1'
            else:
                self.state = 'REJECT'

        elif self.state == 'q1':
            if symbol == '1':
                self.head += 1
            elif symbol == '0':
                self.head += 1
                self.state = 'q2'
            else:
                self.state = 'REJECT'

        elif self.state == 'q2':
            if symbol == self.blank:
                self.state = 'ACCEPT'
            else:
                self.state = 'REJECT'

    def run(self):
        steps = 0
        while self.state not in ['ACCEPT', 'REJECT'] and steps < 100:
            self.step()
            steps += 1
        self.accepted = (self.state == 'ACCEPT')

    def result(self):
        return "Aceptada" if self.accepted else "Rechazada"

# Ejemplos de prueba
for w in ["00", "010", "0110", "01110", "01", "0", "0010", "110"]:
    tm = TuringMachineAccept_01n0(w)
    tm.run()
    print(f"Cadena: {w.ljust(6)} → {tm.result()}")
