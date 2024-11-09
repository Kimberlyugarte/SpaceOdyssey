#Space Odyssey: The Musical Journey of Yuri Gagarin
# This composition captures the experience of Yuri Gagarin's journey into space, using ambient sounds, breathing effects, and melodic elements.
from earsketch import *

init()
setTempo(110)  # Setting an initial tempo for a calm, space-like atmosphere

# Ambient base layer for the vastness of space
fitMedia(YG_EDM_SUB_1, 1, 1, 10) # Sub-bass sound filling the space from measure 1 to 10
fitMedia(RD_RNB_SFX_SPACETAP_1, 2, 1, 3) # Adding a space-tap effect for a sense of mystery and depth
fitMedia(YG_EDM_REVERSEFX_1, 3, 1.5, 2.5) # Reversed sound effect for a rising tension

# Cosmonaut breathing sound to reflect Gagarin's calm and focused state
fitMedia(Y21_BREATH_1, 4, 1.5, 5.5) # Breathing sound placed in the early measures to symbolise anticipation
# Adding filter effects to the breathing to simulate changing air pressure as the cosmonaut ascends
setEffect(4, FILTER, FILTER_FREQ, 4000, 1, 600, 3) 
setEffect(4, FILTER, FILTER_FREQ, 4000, 3, 600, 5)

# Stretching the breathing sound to add a realistic, deep breathing effect as Yuri (The Cosmonaut)ascends into space
Sound = Y21_BREATH_1 
createAudioStretch(Y21_BREATH_1, 4)

# Transitioning to a slower tempo to reflect the calm and vastness of space
setTempo(80)
fitMedia(YG_EDM_PAD_4, 5, 2.25, 6) # Adding a soft pad to create a smooth ambient layer
# Adding a filter sweep to the pad for a gradual rise, giving a sense of movement
setEffect(5, FILTER, FILTER_FREQ, 600, 3, 3000, 5)
setEffect(5, FILTER, FILTER_FREQ, 2000, 5, 100, 6)

# Repeating the pad with a different filter to add variety to the space atmosphere
fitMedia(YG_EDM_PAD_4, 6, 5.5, 8)
setEffect(6, FILTER, FILTER_FREQ, 2000, 7, 100, 8)

# Gradually increasing the tempo to build a sense of progression in the journey
setTempo(90)
fitMedia(YG_EDM_PAD_1, 7, 2.75, 6.75) # Adding another pad layer to deepen the ambient texture
# Adding reverb for an expansive effect, making the sound feel like it's in a large, open space
setEffect(5, REVERB, REVERB_TIME, 500)

# Final tempo increase to indicate a transition to new heights or stages in the journey
setTempo(100)
fitMedia(Y24_HORN_DISTORT_1, 8, 4.75, 8) # Distorted horn sound for an intense, climactic feel

# Vocal sound layer to convey the awe and wonder of space, as if a choir were in the background
fitMedia(AK_UNDOG_OOHS_AHHS_2, 9, 5.75, 9.75)
# Sweeping filter on the vocal effect to make it rise and fall, adding emotional impact
setEffect(9, FILTER, FILTER_FREQ, 600, 5.5, 8000, 6.5)

finish()