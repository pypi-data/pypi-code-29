#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# Import flask dependencies
from flask import Blueprint, render_template, request, jsonify, current_app as app

import anybadge

# Define a blueprint
badger = Blueprint('badger', __name__, url_prefix='/')

################################################################################
# home blueprint functions
################################################################################


@badger.route('badge', methods=['GET'])
def generate():
    rettype = request.args.get('type', default="html")
    name = request.args.get('name', default="-")
    percent = request.args.get('percent', default="0")

    # Define thresholds: <2=red, <4=orange <8=yellow <10=green
    thresholds = {20: 'red',
                  40: 'orange',
                  60: 'yellow',
                  100: 'green'}

    badge = anybadge.Badge(name, percent, thresholds=thresholds)

    if rettype == 'json':
        return jsonify(svg=badge.badge_svg_text)
    else:
        return badge.badge_svg_text
