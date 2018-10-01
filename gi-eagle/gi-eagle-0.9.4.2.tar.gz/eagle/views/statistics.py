from flask import render_template

from eagle.application import app
from eagle.core.wrap.sample import Sample
from eagle.views.common import sample_filename, available_samples


@app.route("/statistics")
def statistics():
    samples = [Sample(sample_filename(s)) for s in available_samples()]
#    samples = samples[0:1]

    attributes = set().union(*[list(s.attributes.keys()) for s in samples])
    attributes = [x for x in attributes if not x.startswith("_")]
    attributes = list(sorted(attributes))
    return render_template("statistics.html", samples=samples, attributes=attributes)
