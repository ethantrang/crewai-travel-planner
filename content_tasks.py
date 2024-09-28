from crewai import Task
from textwrap import dedent
from datetime import date

class ContentTasks:
  
    def capture_voice(self, agent, master_draft):
        return Task(
            description=dedent(f"""
                Analyze the provided master draft to capture the unique voice and common phrases that align with the creator's personality, audience, and brand identity.
                
                Your task:
                1. Review the master draft, including social media posts, videos, and articles if available.
                2. Identify recurring phrases, tone, and style in the draft.
                3. Define the voice characteristics that best represent the creator’s personality and brand.
                4. Phrases and sentence structures shouldn't be specific to the content of the draft, but more general to the creator.
                5. You can also include specific templatized sentences that the creator uses frequently.
                
                Inputs:
                - Master draft: {master_draft}
                
                Your final answer should be a report summarizing:
                - Common phrases
                - Tone and style of communication
                - Key characteristics of the voice that should be maintained across platforms.
            """),
            expected_output="A voice and style guide capturing common phrases, tone, and key voice characteristics.",
            agent=agent
        )

    def key_message_and_value(self, agent, master_draft):
        return Task(
            description=dedent(f"""
                Determine the key message in the master draft and the value this message offers to the target audience.
                
                Your task:
                1. Analyze the master draft and the creator’s goals.
                2. Identify the primary message consistently delivered in the draft (e.g., specific values, themes, or ideas).
                3. Define the core value this message provides to the audience (e.g., actionable insights, motivation, learning).
                
                Inputs:
                - Master draft: {master_draft}
                
                Your final answer should be a report summarizing:
                - The main message in the master draft.
                - The value this message provides to the audience.
            """),
            expected_output="A report outlining the main message and the value it offers to the audience.",
            agent=agent
        )

    def submessages_and_topics(self, agent, master_draft):
        return Task(
            description=dedent(f"""
                Identify supporting submessages and specific topics in the master draft that complement the main message.
                
                Your task:
                1. Review the main message in the master draft.
                2. Break down the main message into 3-5 supporting submessages or themes.
                3. Identify specific topics under each submessage that can be used for future content.
                
                Inputs:
                - Master draft: {master_draft}
                
                Your final answer should be a report summarizing:
                - 3-5 submessages that support the main message in the draft.
                - Specific content topics for each submessage.
            """),
            expected_output="A report with 3-5 submessages and related content topics under each.",
            agent=agent
        )

    def short_form_content(self, agent, voice, key_message_and_value, submessages_and_topics):
        return Task(
            description=dedent(f"""
                Using the voice, key message, and submessages identified from previous tasks, create short-form written content in the appropriate voice, following the AIDA framework.
                
                Your task:
                1. Develop a complete tweet (280 characters) that captures attention, generates interest, creates desire, and motivates action.
                2. Craft an attention-grabbing hook for the tweet.
                3. Ensure the message aligns with the voice, key message, and supporting submessages from the previous tasks.
                4. Do not use generic salesy language or questions. Be authentic and genuine.

                Inputs:
                - Voice: {voice}
                - Key Message: {key_message_and_value}
                - Submessages: {submessages_and_topics}
                
                Your final answer should include:
                - A complete tweet (280 characters)
                - An attention-grabbing hook
                - The tweet should follow the AIDA framework.
            """),
            expected_output="A tweet (280 characters) with an attention-grabbing hook, following the AIDA framework.",
            agent=agent,
        )

    def long_form_written_content(self, agent, voice, key_message_and_value, submessages_and_topics):
        return Task(
            description=dedent(f"""
                Using the voice, key message, and submessages identified from previous tasks, develop a 200-word LinkedIn post in the appropriate voice, following the AIDA framework.
                
                Your task:
                1. Craft an attention-grabbing hook for the post.
                2. Ensure the message aligns with the voice, key message, and submessages from the previous tasks.
                3. Structure the post to capture attention, generate interest, create desire, and drive action.
                4. Do not use generic salesy language or questions. Be authentic and genuine.

                Inputs:
                - Voice: {voice}
                - Key Message: {key_message_and_value}
                - Submessages: {submessages_and_topics}
                
                Your final answer should include:
                - A 200-word LinkedIn post
                - An attention-grabbing hook
                - The post should follow the AIDA framework.
            """),
            expected_output="A 200-word LinkedIn post with an attention-grabbing hook, following the AIDA framework.",
            agent=agent
        )

    def short_form_video_script(self, agent, voice, key_message_and_value, submessages_and_topics):
        return Task(
            description=dedent(f"""
                Using the voice, key message, and submessages identified from previous tasks, create a short-form video script draft (e.g., for TikTok or Instagram) following the AIDA framework.
                
                Your task:
                1. Write an attention-grabbing hook for the video.
                2. Develop 5-7 bullet points that outline the video’s story, aligning with the voice and key message.
                3. Include a clear sign-off and CTA (call-to-action).
                4. Do not use generic salesy language or questions. Be authentic and genuine.

                Inputs:
                - Voice: {voice}
                - Key Message: {key_message_and_value}
                - Submessages: {submessages_and_topics}
                
                Your final answer should include:
                - A video script with a hook, 5-7 bullet points, sign-off, and CTA.
            """),
            expected_output="A short-form video script with a hook, 5-7 bullet points, sign-off, and CTA",
            agent=agent
        )

    def long_form_video_script(self, agent, voice, key_message_and_value, submessages_and_topics):
        return Task(
            description=dedent(f"""
                Using the voice, key message, and submessages identified from previous tasks, create a long-form video script (e.g., for YouTube) that follows the AIDA framework.
                
                Your task:
                1. Develop a compelling title for the video.
                2. Write an attention-grabbing hook for the video.
                3. Break the video into 3-5 chapters, each with 3-5 bullet points that structure the story and align with the key message.
                4. Include a clear sign-off and CTA.
                5. Do not use generic salesy language or questions. Be authentic and genuine.

                Inputs:
                - Voice: {voice}
                - Key Message: {key_message_and_value}
                - Submessages: {submessages_and_topics}
                
                Your final answer should include:
                - A video title and thumbnail suggestion.
                - A script with a hook, 3-5 chapters, sign-off, and CTA.
            """),
            expected_output="A long-form video script with a title, thumbnail suggestion, hook, 3-5 chapters, sign-off, and CTA",
            agent=agent
        )
