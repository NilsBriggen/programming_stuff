normal = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class Rotor():
    def __init__(self):
        self.rotor_1 = ["W", "T", "O", "K", "A", "S", "U", "Y", "V", "R", "B", "X", "J", "H", "Q", "C", "P", "Z", "E", "F", "M", "D", "I", "N", "L", "G"]
        self.rotor_2 = ["G", "J", "L", "P", "U", "B", "S", "W", "E", "M", "C", "T", "Q", "V", "H", "X", "A", "O", "F", "Z", "D", "R", "K", "Y", "N", "I"]
        self.rotor_3 = ["J", "W", "F", "M", "H", "N", "B", "P", "U", "S", "D", "Y", "T", "I", "X", "V", "Z", "G", "R", "Q", "L", "A", "O", "E", "K", "C"]
        self.rotor_4 = ["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q", "U", "I", "R", "H", "X", "L", "N", "F", "T", "G", "K", "D", "C", "M", "W", "B"]
        self.rotor_5 = ["H", "E", "J", "X", "Q", "O", "T", "Z", "B", "V", "F", "D", "A", "S", "C", "I", "L", "W", "P", "G", "Y", "N", "M", "U", "R", "K"]
        self.rotated_1 = []
        self.rotated_2 = []
        self.roteted_3 = []
        self.rotor_list = [self.rotor_1, self.rotor_2, self.rotor_3, self.rotor_4, self.rotor_5]

    def set_rotors(chosen_rotors, starting_pos, self):
        self.used_rotors=[]
        for a in range(0, 2):
            self.used_rotors.append(self.rotor_list[chosen_rotors[a]])
        for list in self.used_rotors:
            a=0
            for letter in list:
                position = list.index(letter) + starting_pos[a], letter
                if position >= len(list):
                    position = position % len(list)
                letter = list[position]
                exec("self.rotated"+a+".append(letter)")
            a+=1

    #def encode(input_letter, chosen_rotors, self):
        