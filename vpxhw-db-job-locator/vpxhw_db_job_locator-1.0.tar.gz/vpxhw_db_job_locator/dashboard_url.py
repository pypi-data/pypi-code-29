from jinja2 import Template

url_template='''http://go/vpxhw-quality?{{jobIds}}

{% if encoder %}
  Choose {% for e in encoder %}
  {{ e }}{% endfor %}
  in encoder selection box (top one on the left)
{% endif %}
{% if model_name %}
  Pick '{{model_name}}' in tags filter (second one from the top)
{% endif %}
'''

class DashboardUrl(object):

  _encoder=[]
  _model_name=None

  def add_single_job(self, commit, encoder, usecase, test_suite, model_name):
    self._encoder.append(' '.join((encoder, usecase,)))
    self._model_name=model_name
  
  def add_latest_job(self, encoder, usecase, test_suite, model_name=None):
    pass

  def get_dashboard_url(self):
    template=Template(url_template)
    return template.render({'jobIds':'', 'encoder':self._encoder, 'model_name': self._model_name})
