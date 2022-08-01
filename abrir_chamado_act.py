{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7cced74d",
   "metadata": {},
   "source": [
    "Abrir chamado para act digital\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c259a288",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pyautogui\n",
      "  Downloading PyAutoGUI-0.9.53.tar.gz (59 kB)\n",
      "Collecting pymsgbox\n",
      "  Downloading PyMsgBox-1.0.9.tar.gz (18 kB)\n",
      "  Installing build dependencies: started\n",
      "  Installing build dependencies: finished with status 'done'\n",
      "  Getting requirements to build wheel: started\n",
      "  Getting requirements to build wheel: finished with status 'done'\n",
      "    Preparing wheel metadata: started\n",
      "    Preparing wheel metadata: finished with status 'done'\n",
      "Collecting PyTweening>=1.0.1\n",
      "  Downloading pytweening-1.0.4.tar.gz (14 kB)\n",
      "Collecting pyscreeze>=0.1.21\n",
      "  Downloading PyScreeze-0.1.28.tar.gz (25 kB)\n",
      "  Installing build dependencies: started\n",
      "  Installing build dependencies: finished with status 'done'\n",
      "  Getting requirements to build wheel: started\n",
      "  Getting requirements to build wheel: finished with status 'done'\n",
      "    Preparing wheel metadata: started\n",
      "    Preparing wheel metadata: finished with status 'done'\n",
      "Collecting pygetwindow>=0.0.5\n",
      "  Downloading PyGetWindow-0.0.9.tar.gz (9.7 kB)\n",
      "Collecting mouseinfo\n",
      "  Downloading MouseInfo-0.1.3.tar.gz (10 kB)\n",
      "Collecting pyrect\n",
      "  Downloading PyRect-0.2.0.tar.gz (17 kB)\n",
      "Collecting pyperclip\n",
      "  Using cached pyperclip-1.8.2.tar.gz (20 kB)\n",
      "Building wheels for collected packages: pyautogui, pygetwindow, pyscreeze, PyTweening, mouseinfo, pymsgbox, pyperclip, pyrect\n",
      "  Building wheel for pyautogui (setup.py): started\n",
      "  Building wheel for pyautogui (setup.py): finished with status 'done'\n",
      "  Created wheel for pyautogui: filename=PyAutoGUI-0.9.53-py3-none-any.whl size=36614 sha256=2fe3cca088bdddff581151306dd3530b04523c05d96814beba39a2a24cc97df9\n",
      "  Stored in directory: c:\\users\\consultor\\appdata\\local\\pip\\cache\\wheels\\d8\\97\\e4\\d2edca92a87d3b5fbfb527264750a17b4ba297b9a7cab6e67f\n",
      "  Building wheel for pygetwindow (setup.py): started\n",
      "  Building wheel for pygetwindow (setup.py): finished with status 'done'\n",
      "  Created wheel for pygetwindow: filename=PyGetWindow-0.0.9-py3-none-any.whl size=11081 sha256=d908ad01f977af7529cc2f2fa40f457335985a10b82f8f22dc4b486d64abfc25\n",
      "  Stored in directory: c:\\users\\consultor\\appdata\\local\\pip\\cache\\wheels\\44\\ab\\20\\423c3a444793767e4e41f8377bc902f77bee212e68dcce85a5\n",
      "  Building wheel for pyscreeze (PEP 517): started\n",
      "  Building wheel for pyscreeze (PEP 517): finished with status 'done'\n",
      "  Created wheel for pyscreeze: filename=PyScreeze-0.1.28-py3-none-any.whl size=13009 sha256=69298f2c0a5b12002acc063c97f15c34653d708adfc3a7eb656c721cbda87cba\n",
      "  Stored in directory: c:\\users\\consultor\\appdata\\local\\pip\\cache\\wheels\\a2\\5b\\86\\99f1d8fac5d92de0ccb3f0d4ad15e3f4278baf75a9b0f20b93\n",
      "  Building wheel for PyTweening (setup.py): started\n",
      "  Building wheel for PyTweening (setup.py): finished with status 'done'\n",
      "  Created wheel for PyTweening: filename=pytweening-1.0.4-py3-none-any.whl size=5854 sha256=45b76a8bcc928e54e41a021e02aa0b3da368f9243dac8cf3511a12bbad4ca868\n",
      "  Stored in directory: c:\\users\\consultor\\appdata\\local\\pip\\cache\\wheels\\a4\\5d\\d2\\ba4c8f82163233ffaadcf383c1e34d7d92635d357d13e7b78d\n",
      "  Building wheel for mouseinfo (setup.py): started\n",
      "  Building wheel for mouseinfo (setup.py): finished with status 'done'\n",
      "  Created wheel for mouseinfo: filename=MouseInfo-0.1.3-py3-none-any.whl size=10906 sha256=8e50690bbf42f0505e41862ad6aa81ff1d1ee3c61fd65a4c8563cb3cfeec6a1e\n",
      "  Stored in directory: c:\\users\\consultor\\appdata\\local\\pip\\cache\\wheels\\61\\73\\b9\\6fb1131ab36e650206e3aa0ad7a68907b41b32ac2d4f75f543\n",
      "  Building wheel for pymsgbox (PEP 517): started\n",
      "  Building wheel for pymsgbox (PEP 517): finished with status 'done'\n",
      "  Created wheel for pymsgbox: filename=PyMsgBox-1.0.9-py3-none-any.whl size=7406 sha256=818a44e025858037ad25988d15e8bd14b5fa93258546e575544e8177ab9195e7\n",
      "  Stored in directory: c:\\users\\consultor\\appdata\\local\\pip\\cache\\wheels\\7f\\13\\8c\\584c519464297d9637f9cd29fd1dcdf55e2a2cab225c76a2db\n",
      "  Building wheel for pyperclip (setup.py): started\n",
      "  Building wheel for pyperclip (setup.py): finished with status 'done'\n",
      "  Created wheel for pyperclip: filename=pyperclip-1.8.2-py3-none-any.whl size=11137 sha256=e6687cf4c84bb8499a4d9a65a3ce7d54e2b374d904997ed65687d2db1d196f37\n",
      "  Stored in directory: c:\\users\\consultor\\appdata\\local\\pip\\cache\\wheels\\0c\\09\\9e\\49e21a6840ef7955b06d47394afef0058f0378c0914e48b8b8\n",
      "  Building wheel for pyrect (setup.py): started\n",
      "  Building wheel for pyrect (setup.py): finished with status 'done'\n",
      "  Created wheel for pyrect: filename=PyRect-0.2.0-py2.py3-none-any.whl size=11196 sha256=a701eb4307d76a9cd004cfcf0d6af9dc8a91eabad97ccd9096a4d20ae9c2294e\n",
      "  Stored in directory: c:\\users\\consultor\\appdata\\local\\pip\\cache\\wheels\\25\\80\\fa\\27bb4a1c2e21f64ec71390489d52e57b7cc8afbe79bd595c5e\n",
      "Successfully built pyautogui pygetwindow pyscreeze PyTweening mouseinfo pymsgbox pyperclip pyrect\n",
      "Installing collected packages: pyrect, pyperclip, PyTweening, pyscreeze, pymsgbox, pygetwindow, mouseinfo, pyautogui\n",
      "Successfully installed PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.2.0 pyscreeze-0.1.28\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "8e5cb268",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyautogui as py\n",
    "import time \n",
    "import pyperclip as pyper\n",
    "\n",
    "py.PAUSE = 1\n",
    "\n",
    "py.hotkey(\"ctrl\", \"t\")\n",
    "pyper.copy(r\"http://ti.actdigital.com/\")\n",
    "py.hotkey(\"ctrl\", \"v\")\n",
    "py.hotkey(\"enter\")\n",
    " \n",
    "#Preenche o formulário de abertura de chamado\n",
    "time.sleep(5)\n",
    "#Preenchge o nome\n",
    "py.hotkey(\"tab\")\n",
    "nome = \"Ramon da Silva\"\n",
    "py.write(nome)\n",
    "\n",
    "#Preenche telefone\n",
    "py.hotkey(\"tab\")\n",
    "telefone = \"(47)99682-1589\"\n",
    "py.write(telefone)\n",
    "\n",
    "#Preenche telefone\n",
    "py.hotkey(\"tab\")\n",
    "email = \"ramon.santos@actdigital.com\"\n",
    "py.write(email)\n",
    "\n",
    "#Preenche telefone\n",
    "py.hotkey(\"tab\")\n",
    "py.click(445, 517)\n",
    "\n",
    "#Preenche cliente\n",
    "py.hotkey(\"tab\")\n",
    "cliente = \"Indefinido\"\n",
    "py.write(cliente)\n",
    "\n",
    "#Preenche estado\n",
    "py.hotkey(\"tab\")\n",
    "uf = \"Tocantins\"\n",
    "py.write(uf)\n",
    "\n",
    "#Preenche estado\n",
    "py.hotkey(\"tab\")\n",
    "gestor = \"Daniel\"\n",
    "py.write(gestor)\n",
    "\n",
    "#Preenche estado\n",
    "py.hotkey(\"tab\")\n",
    "gestor = r\"\"\"\n",
    "    Gostaria de solicitar a verificação.\n",
    "\"\"\"\n",
    "py.write(gestor)\n",
    "\n",
    "#Clica no botão para enviar a solicitação\n",
    "#py.click(666, 604)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0a21d532",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Point(x=666, y=604)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "time.sleep(5)\n",
    "py.position()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ecc859c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e32dabfc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
