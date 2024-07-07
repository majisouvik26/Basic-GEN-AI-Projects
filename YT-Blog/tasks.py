from crewai import Task
from tools import yt_tool
from agents import blog_re, blog_wr


# researcher

re_task = Task(
    description=(
        "After identifying the video{topic} get detailed info about the video from the YouTube Channel"
    ),
    expected_output='An exceptionally comprehensive and exhaustive report on the topic covered in the video from the YouTube channel, spanning at least 3-5 paragraphs.',
    tools=[yt_tool],
    agent=blog_re,
)

# writer

wr_task = Task(
    description=(
        "fetch the info from the YouTube channel on the topic {topic}"
    ),
    expected_output='Summarize the info from the YouTube Video on the topic {topic} and write the content for the blog',
    tools=[yt_tool],
    agent=blog_wr,
    async_execution=False,
    output_file='new_blog.md'
)