#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Convert mock data to DataFrame for analysis
questions = pd.DataFrame(current_data['questions'])
print(questions)


# In[2]:


import json
import pandas as pd

# Load data from the JSON file (if you're using a file)
with open('current_quiz.json', 'r') as file:
    current_data = json.load(file)

# Alternatively, use mock data if you're not using a file
# current_data = {
#     'user_id': 123,
#     'quiz_id': 456,
#     'questions': [
#         {'id': 1, 'topic': 'Physics', 'difficulty': 'Medium', 'correct': False},
#         {'id': 2, 'topic': 'Chemistry', 'difficulty': 'Hard', 'correct': True}
#     ],
#     'score': 15,
#     'total_score': 20
# }

# Convert the 'questions' part of current_data to a DataFrame
questions = pd.DataFrame(current_data['questions'])

# Display the DataFrame
print(questions)


# In[3]:


# Group by topic and calculate the number of correct answers
topic_performance = questions.groupby('topic')['correct'].agg(['sum', 'count'])
topic_performance.rename(columns={'sum': 'correct', 'count': 'total'}, inplace=True)

# Display the performance by topic
print("Topic Performance:")
print(topic_performance)


# In[4]:


# Group by difficulty and calculate the number of correct answers
difficulty_performance = questions.groupby('difficulty')['correct'].agg(['sum', 'count'])
difficulty_performance.rename(columns={'sum': 'correct', 'count': 'total'}, inplace=True)

# Display the performance by difficulty
print("\nDifficulty Performance:")
print(difficulty_performance)


# In[5]:


# Calculate the overall score
overall_score = current_data['score']
total_score = current_data['total_score']
print(f"\nOverall Performance: {overall_score}/{total_score} correct")


# In[6]:


# Analyze the topic performance
topic_recommendations = {}
for topic, row in topic_performance.iterrows():
    if row['correct'] < row['total'] / 2:  # If less than half correct
        topic_recommendations[topic] = f"Focus more on {topic} to improve. Try medium difficulty questions."
    else:
        topic_recommendations[topic] = f"Great progress in {topic}! Keep practicing."

# Analyze the difficulty performance
difficulty_recommendations = {}
for difficulty, row in difficulty_performance.iterrows():
    if row['correct'] < row['total'] / 2:  # If less than half correct
        difficulty_recommendations[difficulty] = f"Practice more on {difficulty} questions to improve your score."
    else:
        difficulty_recommendations[difficulty] = f"You're doing well with {difficulty} questions. Keep it up!"

# Overall recommendations
overall_recommendation = "Keep practicing, stay consistent, and focus on areas where you need more improvement."

# Combine recommendations
all_recommendations = {
    "Topic Recommendations": topic_recommendations,
    "Difficulty Recommendations": difficulty_recommendations,
    "Overall Recommendation": overall_recommendation
}

# Print the recommendations
for section, recommendations in all_recommendations.items():
    print(section)
    for key, value in recommendations.items():
        print(f"- {key}: {value}")
    print("\n")


# In[7]:


import matplotlib.pyplot as plt

# Bar chart for topic performance
topic_performance['correct'].plot(kind='bar', title='Topic Performance')
plt.ylabel('Number of Correct Answers')
plt.show()

# Bar chart for difficulty performance
difficulty_performance['correct'].plot(kind='bar', title='Difficulty Performance')
plt.ylabel('Number of Correct Answers')
plt.show()


# In[8]:


import json
import pandas as pd

# Load data from JSON file
with open('current_quiz.json', 'r') as file:
    current_data = json.load(file)

# Convert to DataFrame
questions = pd.DataFrame(current_data['questions'])


# In[9]:


# Analyze the topic performance
topic_recommendations = {}
for topic, row in topic_performance.iterrows():
    if row['correct'] < row['total'] / 2:  # If less than half correct
        topic_recommendations[topic] = f"Focus more on {topic} to improve. Try medium difficulty questions."
    else:
        topic_recommendations[topic] = f"Great progress in {topic}! Keep practicing."

# Analyze the difficulty performance
difficulty_recommendations = {}
for difficulty, row in difficulty_performance.iterrows():
    if row['correct'] < row['total'] / 2:  # If less than half correct
        difficulty_recommendations[difficulty] = f"Practice more on {difficulty} questions to improve your score."
    else:
        difficulty_recommendations[difficulty] = f"You're doing well with {difficulty} questions. Keep it up!"

# Overall recommendations
overall_recommendation = "Keep practicing, stay consistent, and focus on areas where you need more improvement."

# Combine recommendations
all_recommendations = {
    "Topic Recommendations": topic_recommendations,
    "Difficulty Recommendations": difficulty_recommendations,
    "Overall Recommendation": overall_recommendation
}

# Print the recommendations
for section, recommendations in all_recommendations.items():
    print(section)
    for key, value in recommendations.items():
        print(f"- {key}: {value}")
    print("\n")


# In[10]:


# Analyze the topic performance
topic_recommendations = {}
for topic, row in topic_performance.iterrows():
    if row['correct'] < row['total'] / 2:  # If less than half correct
        topic_recommendations[topic] = f"Focus more on {topic} to improve. Try medium difficulty questions."
    else:
        topic_recommendations[topic] = f"Great progress in {topic}! Keep practicing."

# Analyze the difficulty performance
difficulty_recommendations = {}
for difficulty, row in difficulty_performance.iterrows():
    if row['correct'] < row['total'] / 2:  # If less than half correct
        difficulty_recommendations[difficulty] = f"Practice more on {difficulty} questions to improve your score."
    else:
        difficulty_recommendations[difficulty] = f"You're doing well with {difficulty} questions. Keep it up!"

# Overall recommendations
overall_recommendation = "Keep practicing, stay consistent, and focus on areas where you need more improvement."

# Combine recommendations
all_recommendations = {
    "Topic Recommendations": topic_recommendations,
    "Difficulty Recommendations": difficulty_recommendations,
    "Overall Recommendation": overall_recommendation
}

# Print the recommendations
for section, recommendations in all_recommendations.items():
    print(section)
    if isinstance(recommendations, dict):  # Check if it's a dictionary (for Topic and Difficulty)
        for key, value in recommendations.items():
            print(f"- {key}: {value}")
    else:  # If it's a string (Overall Recommendation)
        print(f"- {recommendations}")
    print("\n")


# In[ ]:




