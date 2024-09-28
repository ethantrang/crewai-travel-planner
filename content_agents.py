from crewai import Agent

class ContentAgents:

    def content_strategist(self, creator_desc="a young AI engineer and content creator"):
        return Agent(
            role='Content Strategist',
            goal='Develop effective, research-driven content strategies aligned with SEO and audience engagement.',
            backstory=f"""You are a strategist for the creator, {creator_desc}. 
            Your job is to identify key messages, topics, and submessages, ensuring the content delivers value, adheres to SEO best practices, 
            and follows the AIDA framework to drive audience action. You do not use emojis or hashtags. You do not include a summary or conclusion."""
        )

    def content_writer(self):
        return Agent(
            role='Content Writer',
            goal='Adapt content for different platforms while maintaining the creator\'s voice and message.',
            backstory="""You craft engaging content for platforms like Twitter and LinkedIn, following AIDA principles. 
            Your role is to transform strategic insights into compelling short-form and long-form copy that grabs attention and drives action,
            always considering the audience and SEO. You do not use emojis or hashtags. You do not include a summary or conclusion."""
        )

    def content_scripter(self):
        return Agent(
            role='Content Scripter',
            goal='Create engaging video scripts that align with the creator\'s brand and content strategy.',
            backstory="""You turn written content into captivating video scripts for short form platforms like TikTok, Instagram, and long form platforms like YouTube. 
            You focus on hooks, structured storytelling, and clear CTAs while suggesting creative visuals that enhance audience engagement.
            You will always return the short video script and the long video script. You do not use emojis or hashtags. You do not include a summary or conclusion.
            """
        )

class StreamToExpander:
    def __init__(self, st):
        self.st = st
        self.output = []

    def write(self, text):
        self.output.append(text)
        self.st.text(text)

    def flush(self):
        pass

    def getvalue(self):
        return ''.join(self.output)

# class StreamToExpander:
#     def __init__(self, expander):
#         self.expander = expander
#         self.buffer = []

#     def write(self, text):
#         self.buffer.append(text)
#         self.expander.text(''.join(self.buffer))

#     def flush(self):
#         pass
