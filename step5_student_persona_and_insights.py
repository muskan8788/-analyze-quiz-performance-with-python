#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd

# Load current quiz data (Step 1)
with open('current_quiz.json', 'r') as file:
    current_data = json.load(file)

# Convert to DataFrame
questions = pd.DataFrame(current_data['questions'])

# Analyze current quiz data (Step 2)
accuracy_by_topic = questions.groupby('topic')['correct'].mean()

# Load historical quiz data (Step 1)
with open('historical_quiz.json', 'r') as file:
    historical_data = json.load(file)

# Convert to DataFrame
historical_questions = pd.DataFrame(historical_data['questions'])

# Analyze historical performance trends (Step 2)
historical_performance = historical_questions.groupby('topic')['correct'].mean()

# Define student persona based on current and historical performance
student_persona = {}

# Persona based on current quiz performance
for topic, accuracy in accuracy_by_topic.items():
    if accuracy >= 0.8:
        student_persona[topic] = f"{topic} Expert"
    elif accuracy >= 0.5:
        student_persona[topic] = f"{topic} Enthusiast"
    else:
        student_persona[topic] = f"{topic} Learner"

# Persona based on historical trends (if available)
for topic, accuracy in historical_performance.items():
    if accuracy >= 0.8:
        student_persona[topic] += " (Consistent Performer)"
    elif accuracy < 0.5:
        student_persona[topic] += " (Needs Attention)"

# Print the student persona
print("Student Persona:")
for topic, persona in student_persona.items():
    print(f"{topic}: {persona}")


# In[2]:


print(historical_data)


# In[3]:


import json
import pandas as pd

# Load historical quiz data
with open('historical_quiz.json', 'r') as file:
    historical_data = json.load(file)

# Extract quizzes from historical data
quizzes = historical_data['quizzes']

# Prepare a list to store quiz performance data
quiz_performance_data = []

# Process each quiz
for quiz in quizzes:
    quiz_id = quiz['quiz_id']
    score = quiz['score']
    total_score = quiz['total_score']
    
    # Process each response in the quiz
    for question_id, response in quiz['responses'].items():
        quiz_performance_data.append({
            'quiz_id': quiz_id,
            'question_id': question_id,
            'selected_option': response['selected_option'],
            'correct': response['correct'],
            'score': score,
            'total_score': total_score
        })

# Convert the list of quiz performance data into a DataFrame
historical_questions = pd.DataFrame(quiz_performance_data)

# Check the structure of the DataFrame
print(historical_questions)

# Analyze performance (Step 2)
historical_performance = historical_questions.groupby('question_id')['correct'].mean()

# Print analysis results
print(historical_performance)


# In[ ]:




