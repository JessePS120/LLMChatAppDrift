import os
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Using these so we know wher to write the output.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "analysis_results")

#Current weeks to analyze.
WEEKS = ["Week1", "Week2", "Week3"]
#Colors used by the bar graph.
COLORS = {"ChatGPT": "#2a78d6", "Claude": "#eb6834", "Gemini": "#1baf7a"}

#Loads the results from the results folders.
def load_results():
    frames = []
    for week in WEEKS:
        path = os.path.join(BASE_DIR, f"{week}_Results", "eval_summary.csv")
        df = pd.read_csv(path)
        df["Week"] = week
        frames.append(df)
    results = pd.concat(frames, ignore_index=True)

    #convert to True/False.
    results["PassedBase"] = results["Base"] == "pass"
    results["PassedPlus"] = results["Plus"] == "pass"
    return results

#Plots a bar graph of the model pass rates for each week.
def plot_pass_rates(df, column, ylabel, title, filename):
    summary = (df.groupby(["Week", "Model"])[column].mean() * 100).reset_index(name="rate")

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5.5))
    sns.barplot(data=summary, x="Week", y="rate", hue="Model", order=WEEKS, hue_order=["ChatGPT", "Claude", "Gemini"], palette=COLORS, ax=ax)

    ax.set_ylim(0, 100)
    ax.set_xlabel("")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    sns.despine()
    #The bar graph was not generating correctly without these parameters. 
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=3)

    fig.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

#Counts the lines of code in each generated solution file for each model. 
def count_lines_of_code(df):
    line_counts = []
    for week, model, filename in zip(df["Week"], df["Model"], df["File"]):
        path = os.path.join(BASE_DIR, f"{week}_Results", model, filename)
        count = 0
        with open(path) as python_file:
            for line in python_file:
                stripped = line.strip()
                #Avoid counting comments. 
                if stripped and not stripped.startswith("#"):
                    count += 1
        line_counts.append(count)
    df["LinesOfCode"] = line_counts
    return df

#Plots a bar graph of the average lines of code for each model and week.
def plot_average_loc(df):
    #Groupby then take the mean. 
    summary = df.groupby(["Week", "Model"])["LinesOfCode"].mean().reset_index(name="lines")

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5.5))
    sns.barplot(data=summary, x="Week", y="lines", hue="Model", order=WEEKS, hue_order=["ChatGPT", "Claude", "Gemini"], palette=COLORS, ax=ax)

    ax.set_xlabel("")
    ax.set_ylabel("Average lines of code")
    ax.set_title("Average lines of code by model/week")
    sns.despine()
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=3)

    fig.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "average_lines_by_week.png")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df = load_results()
    plot_pass_rates(df, "PassedBase", "Base tests passed(%)", "HumanEval Base pass rate by model/week", "base_pass_rate_by_week.png")
    plot_pass_rates(df, "PassedPlus", "Plus tests passed(%)", "HumanEval Plus pass rate by model/week", "plus_pass_rate_by_week.png")
    df = count_lines_of_code(df)
    plot_average_loc(df)

if __name__ == "__main__":
    main()
