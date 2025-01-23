#!/usr/bin/env python
# coding: utf-8

# In[3]:


from Step1_Setup import load_data
from Step2_Data_Analysis import analyze_data
from Step3_Recommendations import generate_recommendations
from Step4_Visualization import visualize_data
from step5_student_persona_and_insights import generate_persona

def main():
    # Step 1: Load and preprocess data
    current_data, historical_data = load_data()

    # Step 2: Analyze data
    analysis_results = analyze_data(current_data, historical_data)

    # Step 3: Generate recommendations
    recommendations = generate_recommendations(analysis_results)

    # Step 4: Visualize data
    visualize_data(analysis_results)

    # Step 5: Generate student persona and insights
    persona = generate_persona(analysis_results)

    # Print results
    print("Student Persona and Insights:")
    print(persona)
    print("\nRecommendations:")
    print(recommendations)

if __name__ == "__main__":
    main()


# In[5]:


from Step1_Setup import load_data
from Step2_Data_Analysis import analyze_data
from Step3_Recommendations import generate_recommendations
from Step4_Visualization import visualize_data
from step5_student_persona_and_insights import generate_persona

def main():
    # Step 1: Load and preprocess data
    current_data, historical_data = load_data()

    # Step 2: Analyze data
    analysis_results = analyze_data(current_data, historical_data)

    # Step 3: Generate recommendations
    recommendations = generate_recommendations(analysis_results)

    # Step 4: Visualize data
    visualize_data(analysis_results)

    # Step 5: Generate student persona and insights
    persona = generate_persona(analysis_results)

    # Print results
    print("Student Persona and Insights:")
    print(persona)
    print("\nRecommendations:")
    print(recommendations)

if __name__ == "__main__":
    main()


# In[6]:


from Step1_Setup import load_data
from Step2_Data_Analysis import analyze_data
from Step3_Recommendations import generate_recommendations
from Step4_Visualization import visualize_data
from step5_student_persona_and_insights import generate_persona

def main():
    # Step 1: Load and preprocess data
    current_data, historical_data = load_data()

    # Step 2: Analyze data
    analysis_results = analyze_data(current_data, historical_data)

    # Step 3: Generate recommendations
    recommendations = generate_recommendations(analysis_results)

    # Step 4: Visualize data
    visualize_data(analysis_results)

    # Step 5: Generate student persona and insights
    persona = generate_persona(analysis_results)

    # Print results
    print("Student Persona and Insights:")
    print(persona)
    print("\nRecommendations:")
    print(recommendations)

if __name__ == "__main__":
    main()


# In[7]:


import os
print(os.getcwd())


# In[8]:


import os
print(os.listdir())


# In[9]:


pip install nbconvert


# In[ ]:

from Step1_Setup import load_data
from Step2_Data_Analysis import analyze_data
from Step3_Recommendations import generate_recommendations
from Step4_Visualization import visualize_data
from step5_student_persona_and_insights import generate_persona

def main():
    # Step 1: Load and preprocess data
    current_data, historical_data = load_data()

    # Step 2: Analyze data
    analysis_results = analyze_data(current_data, historical_data)

    # Step 3: Generate recommendations
    recommendations = generate_recommendations(analysis_results)

    # Step 4: Visualize data
    visualize_data(analysis_results)

    # Step 5: Generate student persona and insights
    persona = generate_persona(analysis_results)

    # Print results
    print("Student Persona and Insights:")
    print(persona)
    print("\nRecommendations:")
    print(recommendations)

if __name__ == "__main__":
    main()



