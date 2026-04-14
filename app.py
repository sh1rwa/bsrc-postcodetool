from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

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

@app.route("/single_lookup", methods=["GET"])
def single_lookup():
    postcode = request.args.get("postcode", "").strip().upper()

    if not postcode:
        return {"error": "No postcode provided"}, 400

    clean = postcode.replace(" ", "")

    ward = postcode_dict.get(clean, "Not found")

    # Format for output
    if len(clean) > 3:
        formatted = clean[:-3] + " " + clean[-3:]
    else:
        formatted = postcode

    return {
        "postcode": formatted,
        "ward": ward
    }


# ===== RUN =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
