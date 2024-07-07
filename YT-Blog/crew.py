from crewai import Crew, Process
from agents import blog_wr, blog_re
from tasks import re_task, wr_task

crew = Crew(
    agents=[blog_re,blog_wr],
    tasks=[re_task,wr_task], # default -> squential task (process)
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
    
    
)

# execution

res =crew.kickoff(inputs={'topic':'Leaked Google Documents'})
print(res)