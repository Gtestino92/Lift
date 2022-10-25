from decimal import Decimal
K = 5 #debe ser divisor de 100
FPS = 60

T_BLOCK_SEG = 5
T_BLOCK_TIMER = int(T_BLOCK_SEG * 1000 / K)
CAPACITY_MAX = 3
#TIMESTEP = Decimal(0.01).__round__(2)
TIMESTEP = 1

STEP = K * Decimal(0.01).__round__(2)

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 900

LIFT_WIDTH = 30
LIFT_HEIGHT = 30

PERSON_WIDTH = 20
PERSON_HEIGHT = 20

POS_LIFT_INIT_Y = SCREEN_HEIGTH-LIFT_HEIGHT
POS_LIFT_INIT_X = int(SCREEN_WIDTH/2)  - int(LIFT_WIDTH/2)

POS_PERSON_INIT_Y = SCREEN_HEIGTH-PERSON_HEIGHT
POS_PERSON_INIT_X = int(SCREEN_WIDTH/2) + int(LIFT_WIDTH/2) - int(PERSON_WIDTH/2)

FLOOR_WIDTH = 40
FLOOR_HEIGHT = 40

POS_FLOOR_INIT_Y = SCREEN_HEIGTH-FLOOR_HEIGHT
POS_FLOOR_INIT_X = int(SCREEN_WIDTH/2)  - int(FLOOR_WIDTH/2)

FLOOR_COLOR = "Blue"
FLOOR_COLOR_PRESSED_LEFT = "Green"
FLOOR_COLOR_PRESSED_RIGHT = "Yellow"

END = 10
T1 = FPS * 2
T2 = FPS * 4


T_EVENT_PERSON_SEG = 30
T_EVENT_PERSON_MS = T_EVENT_PERSON_SEG * 1000
T_EVENT_PERSON = int(T_EVENT_PERSON_MS/ K)

MAX_TOTALS = 10000