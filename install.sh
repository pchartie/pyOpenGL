brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi
pip3 --version
mkdir -v virtual_env
python3 -m venv virtual_env
. virtual_env/bin/activate
pip3 install --upgrade pip
pip3 install PyOpenGL PyOpenGL_accelerate
pip3 install pygame
cd sources
python3 main.py
