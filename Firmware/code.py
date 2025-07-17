import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# ========== MATRIX CONFIG ==========
keyboard.row_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
                     board.GP7, board.GP8, board.GP9, board.GP10)
keyboard.col_pins = (board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,
                     board.GP16, board.GP17, board.GP18, board.GP19, board.GP20)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ========== RGB CONFIG ==========
rgb = RGB(pixel_pin=board.GP0, num_pixels=87, rgb_order=(1, 0, 2))  # Adjust num_pixels
keyboard.modules.append(rgb)

# ========== ENCODER ==========
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# Encoder on GP21 and GP22
encoder.pins = ((board.GP21, board.GP22, board.GP26),)  # (A, B, Switch)
encoder.map = (((KC.VOLD, KC.VOLU), KC.MUTE),)  # Clockwise, Counterclockwise, Switch

# ========== LAYERS ==========
keyboard.modules.append(Layers())

# ========== KEYMAP ==========
keyboard.keymap = [
    [  # Layer 0
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9,
        KC.TAB, KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,  KC.Y,  KC.U,  KC.I,  KC.O,
        KC.CAPS,KC.A,  KC.S,  KC.D,  KC.F,  KC.G,  KC.H,  KC.J,  KC.K,  KC.L,
        KC.LSFT,KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,  KC.N,  KC.M,  KC.COMM, KC.DOT,
        KC.LCTL,KC.LGUI,KC.LALT,KC.SPC, KC.RALT, KC.RCTL, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT,
    ],
]

if __name__ == '__main__':
    keyboard.go()
