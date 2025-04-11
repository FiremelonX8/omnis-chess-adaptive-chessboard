class TextMove():
    def __init__(self, recognizedCommand):
        self.recognizedCommand = recognizedCommand

    def convertTextToNumbers(self, concatenated, textToNumbers):
        try:
            converted = concatenated
            for key, symbol in textToNumbers.items():
                converted = converted.replace(key, symbol)
            if len(converted) != 4:  # Chess moves are 4 characters
                return None
            return converted
        except Exception as e:
            print(f"Conversion error: {e}")
            return None

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
