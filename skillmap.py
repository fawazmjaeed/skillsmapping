import pandas as pd
import plotly.express as px

# Load your CSV file
file_path = r"C:\Users\Fawaz\Documents\GitHub\skillmap-visualization\skillmap.csv"
#file_path = "https://github.com/fawazmjaeed/skillmap-visualization/blob/4cc9d6355769b05e53790b2042e5f32b305dd9e2/skillmap.csv"

df = pd.read_csv(file_path)

# Clean and split skills
df = df[df["Necessary"].notna() & (df["Necessary"].str.strip() != "")]
df["Natural"] = df["Natural"].apply(lambda x: [skill.strip() for skill in str(x).split(",") if skill.strip()])
df["Noticed"] = df["Noticed"].apply(lambda x: [skill.strip() for skill in str(x).split(",") if skill.strip()])

# Prepare sunburst data
sunburst_data = []
colors = {"Skill Mapping": "white", "Necessary": "orange", "Natural": "green", "Noticed": "yellow"}

sunburst_data.append({"Skill": "Skill Mapping", "Parent": "", "Category": "Skill Mapping"})

for _, row in df.iterrows():
    necessary = row["Necessary"].strip()
    sunburst_data.append({"Skill": necessary, "Parent": "Skill Mapping", "Category": "Necessary"})

    for nat in row["Natural"]:
        sunburst_data.append({"Skill": nat, "Parent": necessary, "Category": "Natural"})
    for noti in row["Noticed"]:
        sunburst_data.append({"Skill": noti, "Parent": necessary, "Category": "Noticed"})

df_sunburst = pd.DataFrame(sunburst_data)

# Create sunburst chart
fig = px.sunburst(
    df_sunburst,
    path=["Parent", "Skill"],
    color="Category",
    color_discrete_map=colors,
    title="Fawaz MAJEED - Skill Mapping Visualization",
    width=600,
    height=600
)

# Extract HTML chart only
plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

# Final full HTML with description and legend on the right
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Skill Mapping Sunburst</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            display: flex;
            height: 100vh;
            overflow: hidden;
        }}
        .chart-container {{
            flex: 2;
            padding: 20px;
            box-sizing: border-box;
        }}
        .side-panel {{
            flex: 1;
            padding: 20px;
            background-color: #f4f4f4;
            border-left: 2px solid #ccc;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .description {{
            margin-bottom: 20px;
        }}
        .legend {{
            display: flex;
            flex-direction: column;
        }}
        .legend span {{
            margin-bottom: 10px;
            padding: 8px 12px;
            border-radius: 4px;
            font-weight: bold;
            width: fit-content;
        }}
        .legend-orange {{ background-color: orange; }}
        .legend-green {{ background-color: green; color: white; }}
        .legend-yellow {{ background-color: yellow; }}
    </style>
</head>
<body>
    <div class="chart-container">
        {plot_html}
    </div>
    <div class="side-panel">
        <div class="description">
            <h2>How to Use</h2>
            <p>Click on any <strong>orange cell</strong> in the inner circle - the <strong>Necessary</strong>  skill sets.</p>
            <p>It will give you view on how that <strong>Necessary</strong> skill is backed by my <strong>Natural</strong> strengths and skills <strong>Noticed</strong> and appreciated by peers.</p> 
            <p> </p>
            <p><strong>Summary:</strong> I believe in a hybrid approach, leveraging my <strong>transferable skillsets</strong> to achieve real, measurable business results by choosing the right <strong>"WoW"</strong> [Way of Working] for every business context.</p>
        </div>
        <div class="legend">
            <span class="legend-orange">Necessary: Job-critical skill for Senior Manager</span>
            <span class="legend-green">Natural: My inherent strengths</span>
            <span class="legend-yellow">Noticed: Skills appreciated by peers</span>
        </div>
    </div>
</body>
</html>
"""


# Save output
output_path = r"C:\Users\Fawaz\Documents\GitHub\skillmap-visualization\fmskillmap.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_html)

# Create output html file in GitHub repository
#repo_path = "https://github.com/fawazmjaeed/skillmap-visualization.git"  # This is GitHub repository path
#output_path = os.path.join(repo_path, "skillmap.html")
#with open(output_path, "w", encoding="utf-8") as f:
#    f.write(full_html)



print(f"✅ Final interactive chart with legends saved to:\n{output_path}")

