# error: 맨 마지막 import 대상은 모듈(*.py) 여야 한다
# package(디렉토리)를 import 할 수도 있다.
# 단, package(디렉토리)에 __init__.py가 있으면~

# import pygame.sound.echo.test_echo
from pygame.sound.echo import test_echo

# pygame.sound.echo.test_echo()

test_echo()
