import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 3
RMOTOR = 0

# Digital ports
CLONE_SWITCH = 0
RIGHT_BUTTON = 13

IS_CLONE = w.digital(CLONE_SWITCH)
IS_PRIME = not IS_CLONE


if IS_PRIME:
    # Servos
    servoClaw = 0

    #camera channels
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

    #color tolerances
    COLOR_PROXIMITY=20
    ORANGE_AREA=500
    RGY_AREA=100

    #Claw position values
    clawOpen = 0
    clawAlmostOpen= 500
    clawHalfCrossed = 640
    clawMiddle = 650
    clawStacked = 1000
    clawRedHalfOpen = 1300
    clawGreenHalfOpen = 1450
    clawCrossed = 2047

    #Tophat
    FRONT_TOPHAT = 0
    onBlack = 3000
else:
    # Servos
    servoClaw = 0

    # camera channels
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

    # color tolerances
    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 100

    # Claw position values
    clawOpen = 0
    clawAlmostOpen = 500
    clawHalfCrossed = 640
    clawMiddle = 650
    clawStacked = 1080
    clawRedHalfOpen = 1400
    clawGreenHalfOpen = 1550
    clawCrossed = 2047

    # Tophat
    FRONT_TOPHAT = 0
    onBlack = 3000