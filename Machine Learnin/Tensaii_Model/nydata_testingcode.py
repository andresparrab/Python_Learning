#make a function that produce stress values based on features and probability
#check that the heart rate are in realistic intervals
#run the function multiple times and finally save it it to a csv dataframe
#eye openes  0,1
#eye pupils 4+-3 mm
# v.right.gaze_direction_normalized.x, NO need for now
#pitch = -90,90
#stress 1,5
import random
import pandas as pd
df=pd.DataFrame()
def run_scenario():
    heartR = [100]
    eye_openess = [1]
    eye_pupils = [4]
    pitch = [0]
    stress = []
    nhr= [(heartR[-1]+random.randint(-2,2)) for tid in range(1,30) if heartR[-1] in range(100,160)]
    for tid in range(1,300):
        heartR.append(heartR[tid-1]+random.randint(-2,2))
        eye_openess.append(random.randint(0,1))
        eye_pupils.append(eye_pupils[tid-1]+random.randint(-1,1))
        pitch.append(pitch[tid-1]+random.randint(-10,10))
    return heartR, eye_openess, eye_pupils, pitch,nhr

h,eo,ep,p,nh = run_scenario()
  #  stress.append(getstress(heartR_now))
#return heartR,stress

print('heartR. max: %i, min: %i ' % (max(h),min(h)))
print('Eye openess. max: %i, min: %i ' % (max(eo),min(eo)))
print('Eye pupils. max: %i, min: %i ' % (max(ep),min(ep)))
print('Head pitch. max: %i, min: %i ' % (max(p),min(p)))
print('nh is :::: ', nh)
# print(max(run_scenario()))
# print(min(run_scenario()))