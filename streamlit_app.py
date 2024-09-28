from crewai import Crew
from content_agents import ContentAgents, StreamToExpander
from content_tasks import ContentTasks
import streamlit as st
import sys

st.set_page_config(
    page_title=f"Content AI Agent",
    page_icon="✍️",
)

st.markdown("""
    <style>
        [data-testid="stDecoration"] {
            display: none;
        }
    </style>""",
    unsafe_allow_html=True
)

if "master_draft" not in st.session_state:
    st.session_state.master_draft = None
if "result" not in st.session_state:
    st.session_state.result = None
if "agent_logs" not in st.session_state:
    st.session_state.agent_logs = None

class ContentCrew:
    def __init__(self, master_draft):
        self.master_draft = master_draft
        self.output_placeholder = st.empty()

    def run(self):
        agents = ContentAgents()
        tasks = ContentTasks()

        content_strategist = agents.content_strategist()
        content_writer = agents.content_writer()
        content_scripter = agents.content_scripter()

        # First Crew: Content Strategist Tasks
        capture_voice_task = tasks.capture_voice(content_strategist, self.master_draft)
        key_message_and_value_task = tasks.key_message_and_value(content_strategist, self.master_draft)
        submessages_and_topics_task = tasks.submessages_and_topics(content_strategist, self.master_draft)

        strategist_crew = Crew(
            agents=[content_strategist],
            tasks=[capture_voice_task, key_message_and_value_task, submessages_and_topics_task],
            verbose=True
        )

        strategist_result = strategist_crew.kickoff()

        # Extract outputs from the strategist tasks
        voice = capture_voice_task.output.raw
        key_message_and_value = key_message_and_value_task.output.raw
        submessages_and_topics = submessages_and_topics_task.output.raw

        # Second Crew: Writing Tasks
        short_form_content_task = tasks.short_form_content(content_writer, voice, key_message_and_value, submessages_and_topics)
        long_form_written_content_task = tasks.long_form_written_content(content_writer, voice, key_message_and_value, submessages_and_topics)

        writer_crew = Crew(
            agents=[content_writer],
            tasks=[short_form_content_task, long_form_written_content_task],
            verbose=True
        )

        writer_result = writer_crew.kickoff()

        # Third Crew: Video Scripting Tasks
        short_form_video_script_task = tasks.short_form_video_script(content_scripter, voice, key_message_and_value, submessages_and_topics)
        long_form_video_script_task = tasks.long_form_video_script(content_scripter, voice, key_message_and_value, submessages_and_topics)

        scripter_crew = Crew(
            agents=[content_scripter],
            tasks=[short_form_video_script_task, long_form_video_script_task],
            verbose=True
        )

        scripter_result = scripter_crew.kickoff()

        final_result = {
            "content_strategy": {
                "voice": capture_voice_task.output.raw,
                "key_message_and_value": key_message_and_value_task.output.raw,
                "submessages_and_topics": submessages_and_topics_task.output.raw
            },
            "written_content": {
                "short_form": short_form_content_task.output.raw,
                "long_form": long_form_written_content_task.output.raw
            },
            "video_scripts": {
                "short_form": short_form_video_script_task.output.raw,
                "long_form": long_form_video_script_task.output.raw
            }
        }

        self.output_placeholder.markdown(final_result)
        

        return final_result

with st.container(border=True):

    st.title("✍️ Content AI Agent")
    st.write("Let a dynamic team of agents strategize, write, and script your content. Built with crewAI.")
    st.text("")

st.write("**Agent inputs**")
with st.form("content_form"):
    master_draft = st.text_area(
        "**Master draft**",
        placeholder="Paste your draft here...",
        height=150
    )
    submitted = st.form_submit_button("▶️ Run Agent", use_container_width=True)

if submitted or st.session_state["agent_logs"]:
    if submitted:
        st.write("**Agent logs**")
        with st.status("🤖 **Running task...**", state="running", expanded=True) as status:
            log_output = StreamToExpander(st)
            sys.stdout = log_output
            content_crew = ContentCrew(master_draft)
            st.session_state["result"] = content_crew.run()
            status.update(label="Agent tasks complete", state="complete", expanded=False)
        
        # Store logs in session state
        st.session_state["agent_logs"] = log_output.getvalue()
    else:
        with st.container(border=True):
            with st.expander("**Logs**"):
                st.write(st.session_state["agent_logs"])

if st.session_state["result"]:
    st.write("**Agent outputs**")
    with st.container(border=True):
        
        with st.expander("🕵️ **Content Strategist** _returned an update_"):
            st.write("**Voice**\n" + st.session_state["result"]["content_strategy"]["voice"])
            st.write("**Key Message and Value**\n" + st.session_state["result"]["content_strategy"]["key_message_and_value"])
            st.write("**Submessages and Topics**\n" + st.session_state["result"]["content_strategy"]["submessages_and_topics"])
        with st.expander("👨‍🎨 **Content Writer** _returned an update_"):
            st.write("**Short Form Content**\n" + st.session_state["result"]["written_content"]["short_form"])
            st.write("**Long Form Content**\n" + st.session_state["result"]["written_content"]["long_form"])
        with st.expander("👨‍💻 **Content Scripter** _returned an update_"):
            st.write("**Short Form Video Script**\n" + st.session_state["result"]["video_scripts"]["short_form"])
            st.write("**Long Form Video Script**\n" + st.session_state["result"]["video_scripts"]["long_form"])
