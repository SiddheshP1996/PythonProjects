""""""
import pickle

"""
Pickling Iris

go to UCI ML repository
to download the iris dataset use requests module
write a code to write-binary the pickle file data
write a code to read-binary the pickle file data
"""

import requests
import pickle

data = requests.get("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv").text
# print(data)

# l1 = data.split("\n")
# print(l1)

l2 = [item.split(",") for item in data.split("\n") if len(item) != 0]
# print(l2)

with open("myIris.pkl", "wb") as f:
    pickle.dump(l2, f)

# To read the above pickle file, you can use this below code

# import pickle
#
# with open("myIris.pkl", "rb") as f:
#     print(pickle.load(f))

