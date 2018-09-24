#!/usr/bin/python
import sys, os, copy, time, random
from dot_tools import parse
from dot_tools.dot_graph import SimpleGraph
#from flask import Flask, jsonify, request
#import fair_bpm_test

#app = Flask(__name__)

class O(object):
  def __init__(i, **adds): i.__dict__.update(adds)


class Pretty(O):
    def __repr__(i):
        return i.__class__.__name__ + kv(i.__dict__)

def kv(d):
    return '(' + ', '.join(['%s: %s' % (k, d[k])
                              for k in sorted(d.keys())
                              if k[0] != "_"]) + ')'


class Activity(Pretty):
    # Not convinced inner classes is a good way to do this.
    class State(Pretty):
        WAITING='WAITING'
        READY='READY'
        COMPLETE='COMPLETE'
        ERROR = 'ERROR'

    class Returned(Pretty):
        TRUE=True
        FALSE=False
        ANY='Any'
        ERROR='ERROR' # Do we need this?

    def __init__(self, id=-1, name='unknown'):
        def __init__(self, id=-1, name='unknown'):
            O.__init__(self, id=-1, name=name)
        self.id = id
        self.name = name
        self.parents=[]
        self.state=Activity.State.WAITING
        self.returned=self.Returned.ANY
        # Optional command to eval on the jobs "context"
        self.command=""

    def to_dot(self):
        # http://www.graphviz.org/doc/info/index.html
        c= self.__class__
        dot = '  {} [ name = "{}" state = "{}" returned = "{}" fillcolor={} style=filled shape=ellipse] \n'\
            .format( self.id, self.name, self.state, self.returned, self.calculate_color())
        for p in self.parents:
            dot = dot + '{} -> {} [label={}]\n'.format(p[0], self.id, p[1])
        return dot

    def calculate_color(self):
        return {
            Activity.State.WAITING:  'GREY',
            Activity.State.READY:    'YELLOW',
            Activity.State.COMPLETE: 'GREEN',
            Activity.State.ERROR:    'RED'
        }.get(self.state, 'RED')


    def has_parent(self, aid, ret_val):
        if isinstance(aid, Activity):
            aid=aid.id
        for p in self.parents:
            if p[0] is aid \
                    and (str(p[1]) == str(ret_val) or str(p[1]) == str(Activity.Returned.ANY)):
                return True
        return False

    # Add an Activity for ANY condition,
    # Or add an id of an activity for ANY condition
    # Or add a [Activity, condition]
    # Or add a [id, condition]
    def add_parent(self, parent):
        # Check for a list.  if so, add the first and second items as parent.
        if type(parent) is list:
            if type(parent[0]) is Activity:
                parent[0]=parent[0].id
            # Check for string
            if type(parent[0]) is str:
                self.parents.append([parent[0], parent[1] ] )
                return
        # Check for a string.  If so, assume ANY Returned
        if type(parent) is str:
            self.parents.append([parent, Activity.Returned.ANY])
            return
        # Check for activity, assume ANY
        if isinstance(parent, Activity):
            self.add_parent(parent.id)
            return
            # Need to raise error if we ever load here, or inthe outer 'else' from here
        raise TypeError("Parent in add_parent must be string, Activity, or list of activit and condition")

    def execute_command(self, context):
        if self.command and self.command != "":
            exec(self.command, context)
            print("execute_command context="+str(context))

    def execute(self, context):
        raise TypeError("Activity.execute should always be overridden, but is being invoked directly. id="+self.id+" name="+self.name)


    @classmethod
    def parse_from_dot(cls, id, fields):
        #print("About to check for fields. name in "+str(fields))
        if fields['name'] is None:
            return "Nope"
        module_name, class_name = Activity.get_module_class_name_from_dot_name(fields['name'])
        #import pdb; pdb.set_trace()
        tmp_cls=getattr(sys.modules[module_name], class_name)
        act=tmp_cls(id)
        # If this gets complicated, use this solution https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
        for key in fields:
            # Parents are a list.  Returned is a bool
            if key == 'parents':
                act.parents=eval(str(fields[key]))
            else:
                act.__setattr__(str(key), str(fields[key]))
        return act

    @classmethod
    def get_module_class_name_from_dot_name(self, name):
        # TODO Learn more about modules and sub modules."
        count=name.split(".")
        if len(count) > 1:
            mod = name[:name.rfind('.')]
            cls = name[name.rfind('.')+1:]
            return mod, cls
        else:
            return __name__ , name

class Say(Activity):
    def execute(self, context=None):
        print("In Say " +self.name)


class Always_True(Activity):
    def execute(self, context=None):
        print("In always_true " +self.name)
        self.returned = True

class Always_False(Activity):
    def execute(self, context=None):
        print("In always_false " +self.name)
        self.returned = False

class Random_True_False(Activity):
    def execute(self, context=None):
        self.returned=[True, False][random.randint(0, 1)]
        print("In Random_True_False " +self.name +" value = "+str(self.returned) )

class Sing(Activity):
    def execute(self, context=None):
        print("In Sing "+ self.name)

class Command(Activity):
    def execute(self, context=None):
        print("In command for name "+ self.name)
        print("Pre-run for command should have already run.  no-op execute "+ self.command)


class Process(Pretty):
    def __init__(self, id):
        def __init__(self, id=-1 ):
            O.__init__(self, id=-1)
        self.id = id
        self.activities=[]
        self.context={}

    def to_dot(self):
        dot= 'digraph {} '.format(self.id) + "{"
        for act in self.activities:
            dot = dot + act.to_dot()
        dot = dot + '}\n'
        return dot

    def createJob(self, id):
        job = Job(id, self)
        return job

    def find_activity_by_id(self, id):
        for act in self.activities:
            if act.id == id:
                return act
        return None

    @classmethod
    def parse_to_simple_graph(cls, dot):
        tree = parse(dot)
        g = SimpleGraph.build(tree.kid('Graph'))
        return g

    @classmethod
    def parse(cls, dot):
        tree = parse(dot)
        id=tree.kid('Graph').children[1].label
        g = SimpleGraph.build(tree.kid('Graph'))
        ps=Process(id)
        for node in g.nodes:
            #print("About to parse node "+str(node))
            ps.activities.append(Activity.parse_from_dot(node, g.nodes[node]))
        for edge in g.edges:
            parent=ps.find_activity_by_id(edge[0])
            child=ps.find_activity_by_id(edge[1])
            if edge[2]:
                child.add_parent([parent.id, edge[2]])
            else:
                child.add_parent(parent.id)

        return ps


class Job(Process):
    def __init__(self, id, process):
        self.id=time.time()
        self.process=process
        self.activities=[]
        self.context = copy.deepcopy(process.context)
        # Note:  Job adds self to context because it's the instance of the Process for this particular run.
        self.context['job']=self
        for act in process.activities:
            tmp=copy.deepcopy(act)
            self.activities.append(tmp)

    def get_first_activity(self):
        for act in self.activities:
            if len(act.parents) == 0:
                return act
        raise Exception("Can't find first activity")

    def find_children(self, activity):
        children=[]
        aid=activity.id
        for act in self.activities:
            if act.state != Activity.State.COMPLETE and act.has_parent(aid, activity.returned):
                children.append(act)
        return children

class FlexibleJobRunner(Pretty):
    def execute_job(self, job):
        self.set_all_parentless_activity_to_ready(job)
        while self.has_ready_activities(job):
            act = self.find_ready_activity(job)
            job.context['me']=act
            act.execute_command(job.context)
            act.execute(job.context)
            act.state=Activity.State.COMPLETE
            nextReady = job.find_children(act)
            for nr in nextReady:
                nr.state = Activity.State.READY

    def set_all_parentless_activity_to_ready(self, job):
        for act in job.activities:
            if len(act.parents) == 0:
                act.state=Activity.State.READY

    def has_ready_activities(self, job):
        for act in job.activities:
            if act.state == Activity.State.READY:
                return True
        return False

    def find_ready_activity(self, job):
        for act in job.activities:
            if act.state == Activity.State.READY:
                return act

class dot_data_store(Pretty):

    def save(self, dot):
        pass

    def load(self, id):
        pass

    def delete(self, id):
        pass

    def list(self):
        pass

#class file_dot_data_store(dot_data_store):
#    store_dir=""
#    extention=".dot"
#
#    def filename_from_id(self, id):
#        filename = self.store_dir + os.sep + id + self.extention
#        return filename
#
#    def __init__(self, dir=os.getcwd()+os.sep+"dot_archive"):
#        self.store_dir=dir
#        if not os.path.exists(self.store_dir):
#            os.makedirs(self.store_dir)
#        if not os.access(self.store_dir, os.W_OK):
#            raise IOError("Can't write to archive directory "+self.store_dir)
#
#    def save(self, dot):
#        filename=self.filename_from_id(dot.id)
#        with open(filename, 'w') as f:
#            f.write(dot.to_dot() )
#            return dot
#
#    def load(self, id):
#        filename = self.filename_from_id(id)
#        with open(filename) as f:
#            dot=f.read()
#        ps= Process.parse(dot)
#        return ps
#
#    def delete(self, id):
#        filename = self.filename_from_id(id)
#        os.remove(filename)
#        return True
#
#    def list(self):
#        cont=os.listdir(self.store_dir)
#        return cont

class create_runner(Pretty):
    def __init__(self):
        self.runner=FlexibleJobRunner()

    def run(self, job):
        result = self.runner.execute_job(job)
        return result

# @app.route("/run/", methods = ['POST'])
# def dot_run():
#     file = request.data
#     ps = Process.parse(file)
#     runner = FlexibleJobRunner()
#     filename="JOB-"+time.strftime("%Y-%m-%d_%H_%M_%S")
#     job = ps.createJob(111, filename)
#     runner.execute_job(job)
#     return job.to_dot()
#
#
# @app.route("/dot/<string:id>/", methods = ['GET', 'POST', 'DELETE'])
# @app.route("/dot/", defaults={'id': None} , methods = ['GET'])
# def dot_edit(id=None):
#     if request.method == 'GET':
#         if id == None:
#             list=store.list()
#             page=jsonify(list)
#             return page
#
#         file=store.load(id)
#         return file.to_dot()
#     if request.method == 'POST':
#         file=request.data
#         ps = Process.parse(file)
#         store.save(ps)
#         return ps.to_dot()
#     if request.method == 'DELETE':
#         store.delete(str(id))
#         return "Ok"
#
#
# class FeedDog(Activity):
#     def execute(self):
#         print("Starting feed dog")
#         # Put feed dog code here
#
# store=file_dot_data_store()
#
# if __name__ == '__main__':
#     print("Starting")
#     ps = fair_bpm_test.process()
#     #fair_bpm_test.test_parse_conditional_parents_from_dot(fair_bpm_test.good_dot_src())
#     src=fair_bpm_test.chore_dot()
#     fair_bpm_test.test_chores(src)
#     # fair_bpm_test.test_execute_with_context(ps)
#     # fair_bpm_test.get_module_class_name_from_dot_name()
#
#     # src=fair_bpm_test.good_dot_src()
#     # fair_bpm_test.test_random_activities(src)
#
#     # say=fair_bpm_test.say()
#     # sing=fair_bpm_test.sing()
#     # fair_bpm_test.test_is_parent_conditional(say, sing)
#
#     #fair_bpm_test.test_execute_with_context(ps)
#     #fair_bpm_test.test_parse_activity_from_dot()
#     #app.run(debug=True)
#     # import fair_bpm_test
#     # ps = fair_bpm_test.process()
#     # fair_bpm_test.test_parse_activity_from_dot()
#     # fair_bpm_test.test_file_store(ps)
#
