from flask import Flask, render_template
app = Flask(__name__)

batches = ["243", "251", "252"]
sections = {
    "notes": ["TBA1", "TBA2", "TBA3"],
    "questions": ["C.T_Question", "Mid_Question", "Final_Question"],
    "study_materials": ["Slide_by_Faculty", "Book"],
    "other_materials": ["TBA1", "TBA2"],
    "TBA": []
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/batch<int:batch_id>")
def batch(batch_id):
    if str(batch_id) not in batches:
        return "Batch not found"
    return render_template(f"batch{batch_id}/index.html", batch_id=batch_id)

@app.route("/batch<int:batch_id>/<section>")
def section_page(batch_id, section):
    if str(batch_id) not in batches or section not in sections:
        return "Section not found"
    subs = sections[section]
    return render_template(f"batch{batch_id}/{section}.html", batch_id=batch_id, section=section, subs=subs)

@app.route("/batch<int:batch_id>/<section>/<sub>")
def subsection_page(batch_id, section, sub):
    if str(batch_id) not in batches:
        return "Invalid batch"
    return render_template(f"batch{batch_id}/{section}_{sub}.html", batch_id=batch_id, section=section, sub=sub)

if __name__ == "__main__":
    app.run(debug=True)
