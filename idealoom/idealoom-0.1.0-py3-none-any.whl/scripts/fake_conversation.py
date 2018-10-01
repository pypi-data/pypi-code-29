#!/usr/bin/env python
import argparse
import re
from datetime import timedelta
import pdb
import uuid

from pyramid.paster import get_appsettings, bootstrap
import transaction

from assembl.lib.sqla import configure_engine
from assembl.lib.zmqlib import configure_zmq
from assembl.lib.model_watcher import configure_model_watcher
from assembl.lib.config import set_config
from assembl.lib.parsedatetime import parse_datetime

pattern = re.compile(r'^(\d+)\.\s+(\w+):(\d*)\s+(.*)')


def add_posts(discussion_id, fileobj, lang, start_date, subject, extract_creator):
    from assembl.models import (
        Post, AgentProfile, LangString, Discussion, Extract, TextFragmentIdentifier)
    discussion = Discussion.get(discussion_id)
    db = discussion.db
    lines = []
    profiles = {}
    posts_by_id = {}
    for line in fileobj:
        line = line.strip()
        if not line:
            continue
        parts = pattern.match(line)
        assert parts, "pattern issue in " + line
        lines.append(parts.groups())

    def get_creator(name):
        if name not in profiles:
            author = db.query(
                AgentProfile).filter_by(name=name).first()
            assert author
            profiles[name] = author
        return profiles[name]

    def generate_message_id():
        # Create a local message_id with uuid1 and hostname
        return uuid.uuid1().hex + "_idealoom@" + settings['public_hostname']

    extract_creator = get_creator(extract_creator
        ).create_agent_status_in_discussion(discussion)

    last_post = None
    roots = []
    for (id, creator, target, content) in lines:
        creator = get_creator(creator
            ).create_agent_status_in_discussion(discussion)

        if target == '0':
            parent = None
        elif target:
            parent = posts_by_id[target]
        else:
            parent = last_post
        content, extracts = find_extracts(content)
        body = LangString.create(value=content, locale_code=lang)
        post = Post(dagent_creator=creator, parent=parent,
                 subject=LangString.create(
                     value=subject, locale_code=lang),
                 body=body, creation_date=start_date,
                 discussion=discussion,
                 message_id=generate_message_id())
        db.add(post)
        db.flush()
        for i, (start, end, extract) in enumerate(extracts):
            extract = Extract(
                discussion=discussion, content=post,
                creation_date=post.creation_date+timedelta(days=1, minutes=i),
                creator_dagent=extract_creator, owner_dagent=extract_creator)
            db.add(extract)
            xpath = TextFragmentIdentifier.generate_post_xpath(post)
            tfi = TextFragmentIdentifier(
                body=extract, offset_start=start, offset_end=end,
                xpath_start=xpath, xpath_end=xpath)
            db.add(tfi)
        posts_by_id[id] = post
        if not parent:
            roots.append(post)
        last_post = post
        start_date += timedelta(seconds=90)
    for post in roots:
        post._set_ancestry('')

extract_re = re.compile(r'^([^\[]*)\[([^\]]*)\](.*)')


types = {
    '*': ('InclusionRelation', 'GenericIdeaNode'),
    '?': ('InclusionRelation', 'Issue'),
    '!': ('PositionRespondsToIssue', 'Position'),
    '+': ('ArgumentSupportsIdea', 'Argument'),
    '-': ('ArgumentOpposesIdea', 'Argument'),
}


def find_extracts(text):
    extracts = []
    g = extract_re.match(text)
    while g:
        before, extract_text, after = g.groups()
        extracts.append((len(before), len(before)+len(extract_text), extract_text))
        text = before + extract_text + after
        g = extract_re.match(text)
    return text, extracts


def add_ideas(discussion_id, fileobj, start_date):
    from assembl.models import Idea, IdeaLink, Discussion, LangString
    discussion = Discussion.get(discussion_id)
    db = discussion.db
    tr = discussion.translation_service()
    ancestors = [discussion.root_idea]
    orders = [0]
    for line in fileobj:
        line = line.rstrip()
        if not line:
            continue
        level = 1 + len(line) - len(line.lstrip('\t'))
        assert level < len(ancestors) + 1
        while len(ancestors) > level:
            ancestors.pop()
            orders.pop()
        parent = ancestors[-1]
        order = orders[-1]
        type_code, rest = line.lstrip('\t').split(' ', 1)
        link_type, idea_type = types[type_code]
        line = rest.split("|", 1)
        if len(line) == 1:
            line.append(None)
        title, description = line
        locale, _ = tr.identify(title)
        title = LangString.create(title.strip(), locale)
        if description:
            locale, _ = tr.identify(description)
            description = LangString.create(description.strip(), locale)
        idea = Idea(discussion=discussion, title=title,
                    description=description, creation_date=start_date)
        idea.rdf_type = idea_type
        start_date += timedelta(hours=1)
        orders[-1] += 1
        db.add(idea)
        link = IdeaLink(source=parent, target=idea, order=order)
        link.rdf_type = link_type
        db.add(link)
        ancestors.append(idea)
        orders.append(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read a conversation.')
    parser.add_argument('--discussion_id', '-d', type=int,
                        help='ID of target discussion')
    parser.add_argument('--configuration', '-c', type=str)
    parser.add_argument('--post_file', '-p', type=argparse.FileType('r'))
    parser.add_argument('--idea_file', '-i', type=argparse.FileType('r'))
    parser.add_argument('--extract_creator', '-e', type=str)
    parser.add_argument('--lang', '-l', default='en')
    parser.add_argument('--start_date', type=str,
                        default='2016-09-01T12:00Z')
    parser.add_argument('--subject', '-s', type=str)
    args = parser.parse_args()
    start_date = parse_datetime(args.start_date)
    env = bootstrap(args.configuration)
    settings = get_appsettings(args.configuration, 'idealoom')
    set_config(settings)
    configure_zmq(settings['changes_socket'], False)
    configure_model_watcher(env['registry'], 'idealoom')
    engine = configure_engine(settings, True)
    try:
        if args.post_file:
            with transaction.manager:
                add_posts(args.discussion_id, args.post_file, args.lang,
                          start_date, args.subject, args.extract_creator)
        if args.idea_file:
            with transaction.manager:
                add_ideas(args.discussion_id, args.idea_file, start_date)
    except Exception as e:
        print(e)
        pdb.post_mortem()
