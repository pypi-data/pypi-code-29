import pytest
import fair_flow
from dot_tools import parse
from dot_tools.dot_graph import SimpleGraph

@pytest.fixture()
def say():
    return fair_flow.Say("id22", "The Say Activity")

@pytest.fixture()
def sing():
    return fair_flow.Sing("id33", "The Sing Activity")

@pytest.fixture()
def process():
    two = fair_flow.Say("id22", "Say")
    three = fair_flow.Sing("id33", "Sing")
    three.add_parent(two.id)
    four = fair_flow.Say("id44", "Say")
    four.add_parent(two.id)
    five = fair_flow.Sing("id55", "Sing")
    five.add_parent(two.id)
    ps = fair_flow.Process("Process_Two")
    ps.activities.append(two)
    ps.activities.append(three)
    ps.activities.append(four)
    ps.activities.append(five)
    return ps

@pytest.fixture()
def good_dot_src():
    str='''
    digraph one {
  urgent [ name = "Always_True" state = "WAITING" returned = "Any" fillcolor=WHITE style=filled shape=ellipse]
  send_text [ name = "Random_True_False" state = "WAITING" returned = "Any" fillcolor=WHITE style=filled shape=ellipse]
  send_email [ name = "Always_False" state = "WAITING" returned = "Any" fillcolor=WHITE style=filled shape=ellipse]
  end [ name = "Say" state = "WAITING" returned = "Any" fillcolor=WHITE style=filled shape=ellipse]
  error [ name = "Say" state = "WAITING" returned = "Any" fillcolor=WHITE style=filled shape=ellipse]
  urgent -> send_email [label="False"]
  urgent -> send_text [label="True"]
  send_text -> end [label="True"]
  send_email -> end [label="True"]
  send_text -> error [label="False"]
  send_email -> error [label="False"]
}
    '''
    return str

def test_dot_tools(process):
    runner = fair_flow.FlexibleJobRunner()
    job = process.createJob(111)
    runner.execute_job(job)
    tree = parse(job.to_dot())
    assert len(str(tree)) > 10
    g = SimpleGraph.build(tree.kid('Graph'))
    assert len(g.nodes) == 4
    assert len(g.edges) == 3
    assert g.nodes['id44']['state'] == 'COMPLETE'


def test_run_job(process):
    ps = process

    runner = fair_flow.FlexibleJobRunner()

    print("ps=" + str(ps))

    job = ps.createJob(111)
    runner.execute_job(job)
    tree = parse(job.to_dot())
    g = SimpleGraph.build(tree.kid('Graph'))
    for node in g.nodes:
        # print("Node -> "+str(node))
        assert g.nodes[node]['state'] == 'COMPLETE'

def test_to_dot(say):
    output = say.to_dot()
    print(output)
    assert len(output) > 50

def test_is_parent(say, sing):
    assert len(say.parents) == 0
    assert len(sing.parents) == 0
    sing.add_parent(say)
    say.returned=fair_flow.Activity.Returned.ANY
    assert len(sing.parents) == 1
    assert False == say.has_parent(sing, fair_flow.Activity.Returned.ANY)
    assert True  == sing.has_parent(say, fair_flow.Activity.Returned.ANY)

def test_is_parent_conditional(say, sing):
    assert len(say.parents) == 0
    assert len(sing.parents) == 0
    sing.add_parent(say)
    assert len(sing.parents) == 1
    say.returned=fair_flow.Activity.Returned.TRUE
    assert True  == sing.has_parent(say.id, fair_flow.Activity.Returned.TRUE)
    assert True  == sing.has_parent(say.id, fair_flow.Activity.Returned.ANY)


#def test_file_store(process):
#    name=process.id
#    data=process.to_dot()
#    store=fair_flow.file_dot_data_store()
#    # assert len(store.list() )==0
#    out=store.save(process)
#    loaded=store.load(name)
#    #TODO: implement equals
#    assert len(loaded.to_dot()) > 50 and len(process.to_dot()) > 50
#    assert len(store.list())>0
# #   assert store.delete(loaded.id)

def test_execute_with_context(process):
    com=fair_flow.Command()
    context={}
    context['first']=1
    com.command="answer=1"
    com.execute_command(context)
    assert context['answer'] == 1
    com.command = "answer=answer+answer"
    com.execute_command(context)
    assert context['answer'] == 2

def test_parse_conditional_parents_from_dot(good_dot_src):
    ps=fair_flow.Process.parse(good_dot_src)
    urgent=ps.find_activity_by_id('urgent')
    assert len(urgent.parents)==0
    urgent.returned="False"
    send=ps.find_activity_by_id('send_text')
    assert len(send.parents) == 1
    assert not send.has_parent(urgent.id, urgent.returned)
    urgent.returned="True"
    assert send.has_parent(urgent.id, urgent.returned)

    error=ps.find_activity_by_id('error')
    assert len(error.parents)==2
    send.returned="True"
    assert not error.has_parent(send.id, send.returned)
    send.returned="False"
    assert error.has_parent(send.id, send.returned)

def test_random_activities(good_dot_src):
    ps=fair_flow.Process.parse(good_dot_src)
    runner=fair_flow.create_runner()
    for x in range(1, 100):
        job=ps.createJob("888")
        runner.run(job)
        assert job.find_activity_by_id('urgent').returned == True
        assert job.find_activity_by_id('send_email').state == 'WAITING'
        assert job.find_activity_by_id('send_text').state == 'COMPLETE'
        assert (job.find_activity_by_id('send_text').returned == True
            or job.find_activity_by_id('error').state == 'COMPLETE')
        assert (job.find_activity_by_id('send_text').returned == False
            or job.find_activity_by_id('end').state == 'COMPLETE')

#def get_module_class_name_from_dot_name():
#    default="Say"
#    external="otherpackage.Say"
#    result = fair_flow.Activity.get_module_class_name_from_dot_name(default)
#    assert result[0] == "fair_flow" and result[1] == "Say"
#    result=fair_flow.Activity.get_module_class_name_from_dot_name(external)
#    assert result[0] == "otherpackage" and result[1]== "Say"
