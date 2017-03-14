import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# 절대 경로 from game.sound.echo import echo_test

# 상대 경로 from ..sound.echo import echo_test

from ..sound.echo import echo_test

def render_text():
    print("render")
    echo_test()
