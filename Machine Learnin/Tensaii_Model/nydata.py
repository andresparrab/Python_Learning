#make a function that produce stress values based on features and probability
#check that the heart rate are in realistic intervals
#run the function multiple times and finally save it it to a csv dataframe
#eye openes  0,1
#eye pupils 4+-3 mm
# v.right.gaze_direction_normalized.x, NO need for now
#pitch = -90,90
#roll = -90,90
#heightFromFloor = 130-200
#stress 1,5
import random
import pandas as pd
df=pd.DataFrame()
def run_scenario():
    heartR = [100]
    eye_openess = [0]
    eye_pupils = [4]
    pitch = [0]
    roll = [0]
    heightFromFloor= [150]
    stress = []
    for tid in range(1,300):
        if heartR[-1] in range(82,180):
            heartR.append(heartR[-1]+random.randint(-2,2))
        if eye_openess[-1] in range(0,2):
            eye_openess.append(random.randint(0,1))
        if eye_pupils[-1] in range(3,7):
            eye_pupils.append(eye_pupils[-1]+random.randint(-1,1))
        if pitch[-1] in range(-80,90):
            pitch.append(pitch[-1]+random.randint(-10,10))
        if roll[-1] in range(-80,90):
            roll.append(roll[-1]+random.randint(-10,10))
        if heightFromFloor[-1] in range(130,190):
            heightFromFloor.append(heightFromFloor[-1]+random.randint(-20,20))

    return heartR, eye_openess, eye_pupils, pitch,roll,heightFromFloor

hr,eo,ep,p,r,hf = run_scenario()
  #  stress.append(getstress(heartR_now))
#return heartR,stress

print('heartR. max: %i, min: %i ' % (max(hr),min(hr)))
print('Eye openess. max: %i, min: %i ' % (max(eo),min(eo)))
print('Eye pupils. max: %i, min: %i ' % (max(ep),min(ep)))
print('Head pitch. max: %i, min: %i ' % (max(p),min(p)))
print('Head roll. max: %i, min: %i ' % (max(r),min(r)))
print('Head from floor. max: %i, min: %i ' % (max(hf),min(hf)))

#df['Heartrate'] = hr
# df['Eye openess'] =eo
# df['Eye pupils'] =ep
# df['Head Pitch'] =p
# df['Head Roll'] = r
#print(df)