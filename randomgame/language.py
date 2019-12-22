from translator import *
import text_to_speech as speech

try:
    translator = GoogleTranslator()
    with open('translated_file.txt',mode='a',encoding='utf-8') as translated_file:
        with open('translate.txt',mode = 'r') as translate_file:
            for line in translate_file: 
                gr =  translator.translate(line, dest='el')        
                print(gr)
                speech.speak(gr,"el")
                translated_file.write(gr +'\n')
except IOError as err:
    print('File is too dirty to read!!!')
    raise err
# use google



