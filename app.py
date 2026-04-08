from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# ===== LOAD & CLEAN DATA =====

df = pd.read_excel("lookup.xlsx", skiprows=4)

# Set first row as header
df.columns = df.iloc[0]


# Remove that header row from data
df = df[1:]


# Clean column names
df.columns = df.columns.str.strip()

# Select relevant columns
df = df[["Postcode (single space)", "Geographical ward name"]]

# Rename
df.columns = ["Postcode", "Ward"]

# Clean postcodes
df["Postcode"] = (
    df["Postcode"]
    .astype(str)
    .str.upper()
    .str.replace(" ", "", regex=False)
    .str.strip()
)


# Drop empty rows
df = df.dropna(subset=["Postcode", "Ward"])

# Remove duplicates
df = df.drop_duplicates(subset="Postcode")

# Create lookup dictionary
postcode_dict = dict(zip(df["Postcode"], df["Ward"]))


# ===== ROUTES =====

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/postcodes", methods=["GET"])
def get_postcodes():
    return jsonify(list(postcode_dict.keys()))

@app.route("/lookup", methods=["POST"])
def lookup():
    data = request.json
    postcodes = data.get("postcodes", [])

    results = []

    for p in postcodes:
        clean = p.upper().replace(" ", "").strip()

        ward = postcode_dict.get(clean)

        results.append({
            "postcode": p,
            "ward": ward if ward else "Not found"
        })

    return jsonify(results)


# ===== RUN =====
if __name__ == "__main__":
    app.run(debug=True)
