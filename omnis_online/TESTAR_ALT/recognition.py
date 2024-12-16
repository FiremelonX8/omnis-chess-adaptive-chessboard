import speech_recognition as sr


class Reconhecimento:
    def __init__(self):
        self.rec = sr.Recognizer()
        self.jogada_f = None

    def validar_jogada(self, jogada):
        try:
            partes = jogada.split()
            for j in range(len(partes)):
                self.jogadas_f += partes[j]

            '''if len(partes) == 2:
                self.jogada_f = partes[0] + partes[1]'''

            if len(self.jogadas_f.split()) > 1:
                raise ValueError("Jogada incompleta.")
        except Exception as e:
            print(f"Erro na validação: {e}")
            return None

    def reconhecerJogada(self):
        while True:
            with sr.Microphone() as mic:
                self.rec.adjust_for_ambient_noise(mic)
                print("Fale o movimento (ex: 'e2 e4'):")
                try:
                    audio = self.rec.listen(mic, timeout=6)
                    jogada = self.rec.recognize_google(
                        audio, language='pt-BR').lower()
                    jogada_valida = self.validar_jogada(jogada)
                    if jogada_valida:
                        return jogada_valida
                    else:
                        print("Movimento inválido. Tente novamente.")
                except sr.UnknownValueError:
                    print("Não entendi. Por favor, repita.")
                except sr.RequestError as e:
                    print(f"Erro no serviço de reconhecimento: {e}")
                except sr.WaitTimeoutError:
                    print(f"Você não falou nada em 8 segundos")
