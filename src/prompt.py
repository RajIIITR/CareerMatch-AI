## Prompt Template
input_prompt = """
Hey Act like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide best
assistance for improving their resumes. Assign the percentage Matching based on JD and 
the missing keywords with high accuracy
resume: {text}
description: {jd}

Also if you can guide the user what changes should be done in resume to improve the chances of getting selected but changes should be 
given on the basis strong verb, non repeating power words etc which you think are generally need to be accounted.

I want the response in multi line in having the structure
"Matching percentage" : "%" \n
"Missing keywords" : "" \n
"Profile Summary" : ""  \n
"Scope for Improvement" : ""    \n
"""