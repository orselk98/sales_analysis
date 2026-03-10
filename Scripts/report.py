import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

#==================================================
#Load and prepare data
#===================================================
df =pd.read_csv("Data/raw/ecommerce_sales_data.csv")
df['Order Date']=pd.to_datetime(df['Order Date'])

#Calculate Key Metrics

total_sales=df['Sales'].sum()
total_profit=df['Profit'].sum()
total_transactions=len(df)
avg_sale=df['Sales'].mean()
overall_margin=total_profit/total_sales

date_min=df['Order Date'].min().strftime('%B %Y')
date_max=df['Order Date'].max().strftime('%B %Y')

#Build the PDF

doc=SimpleDocTemplate(
    "Output/sales_analysis_report.pdf",
    pagesize=letter,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch
)

styles=getSampleStyleSheet()

#Custom Styles
title_style=ParagraphStyle(
    'CustomTitle',
    parent=styles['Title'],
    fontSize=28,
    spaceAfter=30
)

heading_style=ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading1'],
    fontSize=18,
    spaceBefore=20,
    spaceAfter=12

)

body_style=ParagraphStyle(
    'CustomBody',
    paretn=styles['Normal'],
    fontSize=11,
    leading=16,
    spaceAfter=8
)

#This list holds all the content in order
story=[]


#Page 1 :Title

story.append(Spacer(1,2*inch))
story.append(Paragraph("E-Commerce Sales Analysis Report", title_style))
story.append(Spacer(1,20))
story.append(Paragraph(f"Period : {date_min} to {date_max}",body_style))
story.append(Paragraph(f"Total Transactions: {total_transactions:,}", body_style))
story.append(Paragraph("Prepared using Python, Pandas, and Matplotlib", body_style))
story.append(PageBreak())


# PAGE 2: EXECUTIVE SUMMARY

story.append(Paragraph("Executive Summary", heading_style))
story.append(Paragraph(
    f"This report analyzes {total_transactions:,} e-commerce transactions from "
    f"{date_min} to {date_max}. Total sales reached ${total_sales:,.0f} with "
    f"total profit of ${total_profit:,.0f}, yielding an overall profit margin "
    f"of {overall_margin:.1%}.",
    body_style
))

# Key findings
story.append(Spacer(1, 12))
story.append(Paragraph("Key Findings:", styles['Heading2']))

findings = [
    "Electronics is the top-selling category at $5.3M, followed by Accessories at $4.2M.",
    "Profit margins are consistent across all categories (approximately 17%).",
    "Sales are evenly distributed across all four regions.",
    "Sales grew 16% from 2022 to 2023, then declined 4% in 2024.",
    "Office category has fewer transactions but comparable average sale values."
]

for finding in findings:
    story.append(Paragraph(f"- {finding}", body_style))



# PAGE 3: SALES BY CATEGORY

story.append(Paragraph("Sales by Category", heading_style))

# Create summary table
cat_data = df.groupby('Category')[['Sales', 'Profit']].sum()
cat_data['Margin'] = cat_data['Profit'] / cat_data['Sales']

table_data = [['Category', 'Total Sales', 'Total Profit', 'Margin']]
for cat in cat_data.index:
    table_data.append([
        cat,
        f"${cat_data.loc[cat, 'Sales']:,.0f}",
        f"${cat_data.loc[cat, 'Profit']:,.0f}",
        f"{cat_data.loc[cat, 'Margin']:.1%}"
    ])

t = Table(table_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf0f1')])
]))

story.append(t)
story.append(Spacer(1, 20))

# Add chart
story.append(Image("Output/category_sales.png", width=4*inch, height=2.8*inch))
story.append(PageBreak())

# ============================================
# PAGE 4: SALES BY REGION
# ============================================
story.append(Paragraph("Sales by Region", heading_style))

reg_data = df.groupby('Region')[['Sales', 'Profit']].sum()
reg_data['Margin'] = reg_data['Profit'] / reg_data['Sales']

table_data = [['Region', 'Total Sales', 'Total Profit', 'Margin']]
for reg in reg_data.index:
    table_data.append([
        reg,
        f"${reg_data.loc[reg, 'Sales']:,.0f}",
        f"${reg_data.loc[reg, 'Profit']:,.0f}",
        f"{reg_data.loc[reg, 'Margin']:.1%}"
    ])

t = Table(table_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf0f1')])
]))

story.append(t)
story.append(Spacer(1, 20))
story.append(Image("Output/region_sales.png", width=5*inch, height=3.5*inch))
story.append(PageBreak())


# ============================================
# PAGE 5: TIME TRENDS
# ============================================
story.append(Paragraph("Sales Trends Over Time", heading_style))

yearly = df.groupby(df['Order Date'].dt.year)['Sales'].sum()
story.append(Paragraph(
    f"Annual sales grew from ${yearly.iloc[0]:,.0f} in 2022 to "
    f"${yearly.iloc[1]:,.0f} in 2023 (a {((yearly.iloc[1] - yearly.iloc[0]) / yearly.iloc[0]):.0%} increase), "
    f"then declined to ${yearly.iloc[2]:,.0f} in 2024.",
    body_style
))

story.append(Spacer(1, 20))
story.append(Image("Output/monthly_sales_trend.png", width=6*inch, height=3.5*inch))
story.append(PageBreak())


# ============================================
# PAGE 6: PROFITABILITY HEATMAP
# ============================================
story.append(Paragraph("Profitability Analysis", heading_style))
story.append(Paragraph(
    "The heatmap below shows profit distribution across categories and regions. "
    "Darker colors indicate higher profit. Electronics in the West region generates "
    "the highest profit, while Office in the North generates the least.",
    body_style
))
story.append(Spacer(1, 20))
story.append(Image("Output/profit_heatmap.png", width=5.5*inch, height=4*inch))


# ============================================
# PAGE 7: CONCLUSIONS
# ============================================
story.append(Paragraph("Conclusions and Recommendations", heading_style))

conclusions = [
    "Electronics drives the most revenue and should remain the primary focus for inventory and marketing investment.",
    "All categories maintain similar profit margins (~17%), suggesting consistent pricing strategy across the business.",
    "Regional performance is balanced, indicating no region-specific issues requiring intervention.",
    "The sales dip in 2024 warrants investigation into potential causes such as market conditions or competitive pressure.",
    "Office category shows strong average transaction values despite low volume. Targeted campaigns could increase transaction frequency."
]

for i, conclusion in enumerate(conclusions, 1):
    story.append(Paragraph(f"{i}. {conclusion}", body_style))
    story.append(Spacer(1, 6))

# ============================================
# BUILD THE PDF
# ============================================
doc.build(story)
print("Report generated: Output/sales_analysis_report.pdf")