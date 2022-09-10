# heights and positions are available as lists
# Import numpy
#from turtle import position
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions=np.array(positions)
np_heights=np.array(heights)
# Heights of the goalkeepers: gk_heights
gk_heights=np_heights[np_positions=='GK']
# Heights of the other players: other_heights
other_heights=np_heights[np_positions!='Gk']
# Print out the median height of goalkeepers. Replace 'None'
goalkeepers=np.median(gk_heights)
print("Median height of goalkeepers: " + str(goalkeepers))
# Print out the median height of other players. Replace 'None'
players=np.median(other_heights)
print("Median height of other players: " + str(players))