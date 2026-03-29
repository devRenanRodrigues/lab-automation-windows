import time
import os
import ctypes

# Aguarda ambiente estabilizar
time.sleep(8)

# 🔢 Ativar Num Lock
ctypes.windll.user32.keybd_event(0x90, 0, 0, 0)

# 🌐 Abre Chrome
os.system("start chrome")

# ⏳ Aguarda o navegador iniciar
time.sleep(8)

# 🌐 Abre portal do aluno
os.system('start chrome "https://aluno.sereduc.com/"')

print("Ambiente pronto!")