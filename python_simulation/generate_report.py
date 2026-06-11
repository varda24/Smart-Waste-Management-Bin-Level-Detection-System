from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet

import pandas as pd
from datetime import datetime

pdf = SimpleDocTemplate(
    "reports/waste_monitoring_report.pdf"
)

styles = getSampleStyleSheet()

content = []

title = Paragraph(
    "Smart Waste Management Monitoring Report",
    styles["Title"]
)

content.append(title)
content.append(Spacer(1, 12))

content.append(
    Paragraph(
        f"Generated: {datetime.now()}",
        styles["Normal"]
    )
)

content.append(Spacer(1, 12))

df = pd.read_csv("data/bin_log.csv")

latest = df.iloc[-1]

content.append(
    Paragraph(
        f"Latest Distance: {latest['Distance']} cm",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Latest Fill Percentage: {latest['FillPercent']}%",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Current Status: {latest['Status']}",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        f"Alert Status: {latest['Alert']}",
        styles["Normal"]
    )
)

content.append(Spacer(1, 20))

content.append(
    Paragraph(
        f"Total Readings Logged: {len(df)}",
        styles["Normal"]
    )
)

pdf.build(content)

print("PDF Report Generated Successfully")