import speech_recognition as sr

class Reconhecimento:
    def __init__(self):
        self.rec = sr.Recognizer()
        self.jogada_f = None

    def validar_jogada(self, jogada):
        try:
            partes = jogada.split()
            if len(partes) == 2:
                self.jogada_f = partes[0] + partes[1]
                return self.jogada_f
            else:
                raise ValueError("Jogada incompleta.")
        except Exception as e:
            print(f"Erro na validação: {e}")
            return None

    def reconhecerJogada(self):
        while True:
            with sr.Microphone() as mic:
                self.rec.adjust_for_ambient_noise(mic)
                print("Fale o movimento (e.g., 'e2 e4'):")
                try:
                    audio = self.rec.listen(mic)
                    jogada = self.rec.recognize_google(audio, language='pt-BR').lower()
                    jogada_valida = self.validar_jogada(jogada)
                    if jogada_valida:
                        return jogada_valida
                    else:
                        print("Movimento inválido. Tente novamente.")
                except sr.UnknownValueError:
                    print("Não entendi. Por favor, repita.")
                except sr.RequestError as e:
                    print(f"Erro no serviço de reconhecimento: {e}")
