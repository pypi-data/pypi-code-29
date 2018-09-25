import os
import sys

from django.core.management.base import BaseCommand

INCLUDE_CODE = """{%% load static %%}            
<script src="{%% static '%(appname)s/tags/%(tag)s.tag' %%}" type="riot/tag"></script>
<script>

riot_context['%(tag)s'] = {};

</script>"""

TAG_CODE_EXAMPLE = """<%(tag)s>

    <!--
                                  SOME EXAMPLE CODE
                                  
        - just a button showing how to attach arguments to a method call in riotjs.
        - data-item-id will be available as e.target.dataset.itemId in the update_data method.
        - the value of the comment field will be read using the DOM.
        
     -->
     
    <h1>%(tag)s is working</h1> 
    <button class="btn btn-primary" data-item-id="42" onclick={update_data}>Comment</button>
    <input type="text" id="comment">
    
  <script>
    /* debugging: write this.opts to the console, which is the context we got when the app was mounted, 
                  ie. what is stored in the riot_context */
    
    console.log("%(tag)s was mounted and given this context:");
    console.log(this.opts);
    
    this.app_data = {};

    this.init = (function() {
        var params = {}
        axios.post('/api/get_some_data', params).then(function (response) { /* get_some_data = your api path */
            console.log(response.data);
            this.update({app_data: response.data}); /* data = whatever you return from api call */
        }.bind(this)).catch(function (error) {
            console.log(error);
        });
    });

    this.update_data = (function (e){
        var item_id = e.target.dataset.itemId;
        var comment = document.getElementById('comment').value;

        var data = { comment: comment, item_id: item_id };
        console.log(data);

        axios.post('/api/update_data', data).then(function (response) {
            console.log(response.data);
            this.update({app_data: response.data});
        }.bind(this)).catch(function (error) {
            console.log(error);
        });

        document.getElementById('comment').value = ''; /* blank the comment field after updating the server */
        document.getElementById('comment').focus();    /* set focus on the comment field */

    }).bind(this);

    this.init();

  </script>

  <style scoped>
  
  </style>
</%(tag)s>"""

TAG_CODE_CLEAN = """<%(tag)s>
  <h1>%(tag)s is working</h1>
  <script>
  </script>

  <style scoped>
  </style>
</%(tag)s>"""

class Command(BaseCommand):
    help = 'Creates boilerplate for a RiotJS tag'

    def add_arguments(self, parser):
        parser.add_argument('appname', type=str)
        parser.add_argument('tag', nargs='+', type=str)
        parser.add_argument('--example_code', default=False, action="store_true", dest="example")

    def handle(self, *args, **options):
        from django.conf import settings
        appname = options['appname']
        tags = options['tag']
        example_code = options['example']

        if not appname in settings.INSTALLED_APPS:
            self.stderr.write(self.style.ERROR('App "%s" not found.' % appname))

        app_folder = os.path.join(os.getcwd(), appname)
        if not os.path.exists(app_folder):
            self.stderr.write(self.style.ERROR("App folder '%s' for app '%s' not found." % (app_folder, appname)))

        tags_home = None
        templates_folder = None
        try:
            tags_home = os.path.join(app_folder, 'static', appname, 'tags')
            if not os.path.exists(tags_home):
                os.makedirs(tags_home)

            templates_folder = os.path.join(app_folder, 'templates', appname, 'include', 'tags')
            if not os.path.exists(templates_folder):
                os.makedirs(templates_folder)

        except Exception as ex:
            self.stderr.write(self.style.ERROR("Error creating target folders for app '%s'. Exception: %s" % (appname, ex)))
            sys.exit(1)

        for tag in tags:
            context = {'appname': appname, 'tag': tag}
            tag_ = os.path.join(tags_home, '%s.tag' % tag)
            if os.path.exists(tag_):
                self.stderr.write(self.style.ERROR("Tag %s allready exists." % tag))
                sys.exit(1)
            tag_template = example_code and TAG_CODE_EXAMPLE or TAG_CODE_CLEAN
            open(tag_, 'w').write(tag_template % {'tag': tag})

            include_template = os.path.join(templates_folder, '%s_tag.html' % tag)
            open(include_template, 'w').write(INCLUDE_CODE % context)

        self.stdout.write(self.style.SUCCESS('Successfully created tags for %s' % appname))
        self.stdout.write("""
        
Now add this to your template:

{%% block riot_tags %%}""" % context)
        for tag in tags:
            self.stdout.write("""{%% include '%(appname)s/include/tags/%(tag)s_tag.html' %%}""" % {'appname': appname, 'tag': tag})
        self.stdout.write("""{% endblock riot_tags %}
        
And use your tags somewhere in the template, like so:
        
        """)
        for tag in tags:
            self.stdout.write("<%s></%s>" % (tag, tag))

        self.stdout.write("\nTo add context to your tags edit the files in the %s/templates/include/tags-folder" % appname)
