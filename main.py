from interaction import ask_user_preferences
from research import fetch_research_data
from summarizer import summarize_data
from report_generator import generate_report

if __name__ == "__main__":
    topic, objectives = ask_user_preferences()
    raw_data = fetch_research_data(topic)
    summary = summarize_data(raw_data, objectives)
    generate_report(topic, objectives, summary)
