def fetch_research_data(topic):
    sources = [
        f"https://simulatedsource.org/article-about-{topic}",
        f"https://example.com/{topic}-overview"
    ]
    return "\n".join([f"Content from {url}" for url in sources])
