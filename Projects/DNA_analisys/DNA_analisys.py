'''
DNA analys by Andres Parra
Scene:
A spy deleted important files from a computer. There were a few witnesses at the scene of the crime, but no one is sure who exactly the spy was.
Three possible suspects were apprehended based on surveillance video. Each suspect had a sample of DNA taken from them.
The computer's keyboard was also swabbed for DNA evidence and, luckily, one small DNA sample was successfully retrieved from the computer's keyboard.
Given the three suspects' DNA and the sample DNA retreived from the keyboard, it's up to you to figure out who the spy is!


Required methods:
1: Given a file, read the DNA for each suspect and save it as a string
2: Take a DNA string and  split it into codons
3: iterate through a suspect's codon list to see how many of their codons match the sample codons
4: Pick the right suspect to continue the investigation on.
'''

from time import sleep
sample_dna = ['GTA','GGG','CAC']

def read_dna(suspect_file):
#   Open the sustect files and save the dna string into a variable
    with open(suspect_file,'r') as file:
        suspect_dna = file.readline()
        print(len(suspect_dna))
    return suspect_dna

#Codons splitting
def codon_splitting(suspect_file):
    suspect_codons=[]
    for i in range(0, len(suspect_file), 3):
        suspect_codons.append(suspect_file[i:i+3])
    return suspect_codons

def analyze(suspect):
    match =0
    codons = codon_splitting(suspect)
    for codon in codons:
         if codon in sample_dna:
            match +=1
    return match

def is_guilty(suspect):
    #Calls the read_dna function to read the file of the suspect
    suspect_dna = read_dna(suspect)
    #Calls the analyze function to analyze the suspects DNA witht he sample DNA
    match = analyze(suspect_dna)
    #If the sample DNA matches the codons then we have our suspect. it has to match all 3 of the codons at least one time.
    if match >=3:
        print('Suspect is guilty. Matches found: %s, minimum matches to coincide are 3' %(match))
    else:
        print('Suspect not guilty.No enough matches found. Number of matches: %s' %(match))


print('Analysing suspect nr.1...')
sleep(2)
is_guilty('suspect1.txt')
sleep(2)
print('Analysing suspect nr.2:...')
sleep(2)
sleep(2)
is_guilty('suspect2.txt')
sleep(2)
print('Analysing suspect nr.2:...')
sleep(2)
is_guilty('suspect3.txt')