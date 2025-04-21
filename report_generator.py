def generate_report(topic, objectives, summary):
    with open(f"{topic}_report.txt", "w") as f:
        f.write(f"Topic: {topic}\nObjectives: {objectives}\n\n{summary}")
    print(f"Report generated: {topic}_report.txt")
