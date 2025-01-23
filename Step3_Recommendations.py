#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Analyze and recommend
accuracy_by_topic = questions.groupby('topic')['correct'].mean()
for topic, accuracy in accuracy_by_topic.items():
    if accuracy < 0.5:
        print(f"Focus on {topic}, accuracy: {accuracy:.2%}")


# In[2]:


import json
import pandas as pd

# Load data from JSON file
with open('current_quiz.json', 'r') as file:
    current_data = json.load(file)

# Convert to DataFrame
questions = pd.DataFrame(current_data['questions'])

# Step 3: Analyze and Recommend
accuracy_by_topic = questions.groupby('topic')['correct'].mean()

# Create recommendations based on performance
recommendations = {}
for topic, accuracy in accuracy_by_topic.items():
    if accuracy < 0.5:
        recommendations[topic] = f"Focus more on {topic} to improve. Try medium difficulty questions."
    else:
        recommendations[topic] = f"Great progress in {topic}! Keep practicing."

# Display recommendations
for topic, recommendation in recommendations.items():
    print(f"Topic: {topic} - {recommendation}")


# In[ ]:




