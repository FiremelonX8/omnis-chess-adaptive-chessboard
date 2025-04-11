class Move():
    def __init__(self, recognizedCommand):
        self.recognizedCommand = recognizedCommand

    def convertTextToNumbers(concatenated, textToNumbers):
        converted = 0
        for key, symbol in textToNumbers.items():
            converted = concatenated.replace(key, symbol)
        print("CONVERTED: ", converted)
        return converted

    def __str__(self):
        return f"Move: {self.recognizedCommand}"

    def mapCommand(self, vRec, textToNumbers):
        mappedCommand = None
        if len(self.recognizedCommand.strip()) > 1:
            concatenated = vRec.concatenate(self.recognizedCommand)
            print("Concatenated command:", concatenated)
            mappedCommand = self.convertTextToNumbers(
                concatenated, textToNumbers)

        if mappedCommand is not None:
            print(f"Mapped command: {mappedCommand}")
        else:
            print("No command found")
        return mappedCommand
