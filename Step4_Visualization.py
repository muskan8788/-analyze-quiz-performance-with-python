#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

# Plot accuracy by topic
accuracy_by_topic.plot(kind='bar', color='skyblue')
plt.title("Accuracy by Topic")
plt.show()


# In[2]:


import matplotlib.pyplot as plt

# Plot accuracy by topic
accuracy_by_topic.plot(kind='bar', color='skyblue')
plt.title("Accuracy by Topic")
plt.show()


# In[3]:


import json
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data from JSON file (ensure the file is in the right location)
with open('current_quiz.json', 'r') as file:
    current_data = json.load(file)

# Step 2: Convert data to DataFrame
questions = pd.DataFrame(current_data['questions'])

# Step 3: Analyze the data (accuracy per topic)
accuracy_by_topic = questions.groupby('topic')['correct'].mean()

# Step 4: Visualization (plotting the accuracy by topic)
accuracy_by_topic.plot(kind='bar', color='skyblue')
plt.title("Accuracy by Topic")
plt.xlabel('Topic')
plt.ylabel('Average Accuracy')
plt.show()


# In[ ]:




