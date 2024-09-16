import wave as wv
import string
op = input("squares-1 or notation-2?")
if op == 1:

    def read_aud(file_path):
        with wv.open(file_path, 'rb') as wf:
            #audio file parameters
            params = wf.getparams()
            #audio file frames
            frames = wf.readframes(wf.getnframes())
        return params, frames

    #write a new wav audio file
    def write_wav(out_path, params, frames):
        with wv.open(out_path, 'wb') as wf:
            #set the parameters
            wf.setparams(params)
            #write frames in file
            wf.writeframes(frames)    

    alphabet = list(string.ascii_uppercase[:8])

    for i in range(8):
        for j in range(8):
            #var read the audio file for number
            numDataTup = read_aud(f"audio/{i + 1}.wav")
            alpDataTup = read_aud(f"audio/{alphabet[j-8]}.wav")
            if numDataTup[0] == alpDataTup[0]:
                concatFrames = alpDataTup[1] + numDataTup[1]
                write_wav(f"{alphabet[j-8]}{i + 1}.wav", numDataTup[0], concatFrames)
            else:
                print("The files parameters are not equal")
    '''dataTup = read_aud(f"../audio/{i}.wav")
        if i > 7:
            varAlph = alphabet[i-8]
            dataTup = read_aud(f"../audio/{varAlph}.wav")'''
    
elif op==2:
    #do the code for concatenating the squares audio files
    pass
