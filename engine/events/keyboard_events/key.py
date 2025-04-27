import pygame
from enum import Enum

class Key(Enum):
    # Letters
    A = pygame.K_a
    B = pygame.K_b
    C = pygame.K_c
    D = pygame.K_d
    E = pygame.K_e
    F = pygame.K_f
    G = pygame.K_g
    H = pygame.K_h
    I = pygame.K_i
    J = pygame.K_j
    K = pygame.K_k
    L = pygame.K_l
    M = pygame.K_m
    N = pygame.K_n
    O = pygame.K_o
    P = pygame.K_p
    Q = pygame.K_q
    R = pygame.K_r
    S = pygame.K_s
    T = pygame.K_t
    U = pygame.K_u
    V = pygame.K_v
    W = pygame.K_w
    X = pygame.K_x
    Y = pygame.K_y
    Z = pygame.K_z

    # Numbers
    ZERO = pygame.K_0
    ONE = pygame.K_1
    TWO = pygame.K_2
    THREE = pygame.K_3
    FOUR = pygame.K_4
    FIVE = pygame.K_5
    SIX = pygame.K_6
    SEVEN = pygame.K_7
    EIGHT = pygame.K_8
    NINE = pygame.K_9

    # Function Keys
    F1 = pygame.K_F1
    F2 = pygame.K_F2
    F3 = pygame.K_F3
    F4 = pygame.K_F4
    F5 = pygame.K_F5
    F6 = pygame.K_F6
    F7 = pygame.K_F7
    F8 = pygame.K_F8
    F9 = pygame.K_F9
    F10 = pygame.K_F10
    F11 = pygame.K_F11
    F12 = pygame.K_F12

    # Arrows and navigation
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT
    HOME = pygame.K_HOME
    END = pygame.K_END
    PAGE_UP = pygame.K_PAGEUP
    PAGE_DOWN = pygame.K_PAGEDOWN
    INSERT = pygame.K_INSERT
    DELETE = pygame.K_DELETE

    # Modifiers and controls
    SHIFT = pygame.K_LSHIFT
    CTRL = pygame.K_LCTRL
    ALT = pygame.K_LALT
    CAPS_LOCK = pygame.K_CAPSLOCK
    TAB = pygame.K_TAB
    ESC = pygame.K_ESCAPE
    SPACE = pygame.K_SPACE
    ENTER = pygame.K_RETURN
    BACKSPACE = pygame.K_BACKSPACE

    # Symbols
    MINUS = pygame.K_MINUS
    EQUALS = pygame.K_EQUALS
    LEFT_BRACKET = pygame.K_LEFTBRACKET
    RIGHT_BRACKET = pygame.K_RIGHTBRACKET
    BACKSLASH = pygame.K_BACKSLASH
    SEMICOLON = pygame.K_SEMICOLON
    APOSTROPHE = pygame.K_QUOTE
    GRAVE = pygame.K_BACKQUOTE
    COMMA = pygame.K_COMMA
    PERIOD = pygame.K_PERIOD
    SLASH = pygame.K_SLASH

    # Numpad
    NUMPAD_0 = pygame.K_KP0
    NUMPAD_1 = pygame.K_KP1
    NUMPAD_2 = pygame.K_KP2
    NUMPAD_3 = pygame.K_KP3
    NUMPAD_4 = pygame.K_KP4
    NUMPAD_5 = pygame.K_KP5
    NUMPAD_6 = pygame.K_KP6
    NUMPAD_7 = pygame.K_KP7
    NUMPAD_8 = pygame.K_KP8
    NUMPAD_9 = pygame.K_KP9
    NUMPAD_ADD = pygame.K_KP_PLUS
    NUMPAD_SUBTRACT = pygame.K_KP_MINUS
    NUMPAD_MULTIPLY = pygame.K_KP_MULTIPLY
    NUMPAD_DIVIDE = pygame.K_KP_DIVIDE
    NUMPAD_DECIMAL = pygame.K_KP_PERIOD
    NUMPAD_ENTER = pygame.K_KP_ENTER
