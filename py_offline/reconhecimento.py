import speech_recognition as sr
import vosk

class Reconhecimento:
    def __init__(self):
        self.rec = sr.Recognizer()
        self.jogada_f = None

    def validar_jogada(self, jogada):
        try:
            jogada = jogada.split(' ')
            self.jogada_f = jogada[0] + jogada[1]
        # except jogada[0].isnull() or jogada[1].isnull():
            # print('Jogada não reconhecida!')'''
        except IndexError:
            print('Não foi possível reconhecer a jogada! Repita')
        except sr.UnknownValueError:
            print('Não foi possível reconhecer a jogada! Repita')
        sfor_cform = [jogada, self.jogada_f]
        return sfor_cform

    def reconhecer_audio(self):
        while True:
            with sr.Microphone() as mic:
                self.rec.adjust_for_ambient_noise(mic)
                print('Falar')
                audio = self.rec.listen(mic)
                frase = self.rec.recognize_vosk(
                    audio, language='pt-BR').lower()
                if frase == 'jogar':
                    print('Jogando')
                    audio_jogada = self.rec.listen(mic)
                    jogada = self.rec.recognize_vosk(
                        audio_jogada, language='pt-BR').lower()
                    print(jogada)
                    self.jogada_f = self.validar_jogada(jogada)
                    print(self.jogada_f[0], self.jogada_f[1])
                    return self.jogada_f
