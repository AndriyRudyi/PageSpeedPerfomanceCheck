import csv
import os

class Reporter:

    def __init__(self,report_path):
        self.report_path = report_path
        self.results = []

    def add_result(self, page_url, status, load_time):
        self.results.append({
            "Page URL": page_url,
            "Status": status,
            "Page Load Time (ms)": load_time
        })
    def save_report(self):
        os.makedirs(os.path.dirname(self.report_path), exist_ok=True)

        with open(self.report_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Page URL", "Status", "Page Load Time (ms)"])
            writer.writeheader()
            for result in self.results:
                writer.writerow(result)

    def save_report(self):
        os.makedirs(os.path.dirname(self.report_path), exist_ok=True)

        with open(self.report_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Page URL", "Status", "Page Load Time (ms)", "Color"])

            for result in self.results:
                color = "green" if result["Status"] == "Passed" else "red"
                writer.writerow([result["Page URL"], result["Status"], result["Page Load Time (ms)"], color])
