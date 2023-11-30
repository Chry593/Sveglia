# -*- coding: utf-8 -*-
"""
sveglia
"""
import time,pygame

def suono_sveglia(filepath):
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()





def sveglia(filepath):
    
    ora = int(input("Inserisci ora per la sveglia: "))
    minuti = int(input("Inserisci minuti per la sveglia: "))
    assert 0 <= ora <= 23 and 0 <= minuti <= 59 , "non è un ora valida" 
    orario_sveglia = f"{ora}:{minuti}"
    
    
    #finche ora di adesso diversa dall'ora della sveglia
    while True:
        
        local = time.localtime()
        formatted_time = time.strftime("%H:%M", local)

        
        if formatted_time == orario_sveglia:
            suono_sveglia(filepath)
            time.sleep(45)
            pygame.mixer.quit()
            break
    return orario_sveglia

    