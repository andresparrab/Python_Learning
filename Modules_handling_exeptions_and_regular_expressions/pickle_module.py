import pickle

'''it's useful just for anything that requires a lot of processing and ends with an object'''


# create a pickle
# example_dict = {1:'6',2:'2',3:'f'}
# pickle_out = open('dict.pickle', 'wb')
# pickle.dump(example_dict,pickle_out)
# pickle_out.close()

# Now we depickle, read the dic.pickle back to memory

pickle_in = open('dict.pickle','rb')
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[3])

