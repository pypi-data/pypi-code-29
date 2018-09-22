#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 08 30 16:29:20 2018

@project: CHOP
@author : likw
@company: HuMan Inc.
"""

import os
import math
import json


Hans_L = 0x4E00
Hans_R = 0x9FD6


obs = []
states = ['B', 'M', 'E', 'S']
start_p = {
   'B' : 0.499999,
   'M' : 0.000001,
   'E' : 0.000001,
   'S' : 0.499999
   }
trans_p = {
   'B' : {'B': 0.000001, 'M': 0.299999, 'E':0.699999, 'S':0.000001},
   'M' : {'B': 0.000001, 'M': 0.000001, 'E':0.999997, 'S':0.000001},
   'E' : {'B': 0.499999, 'M': 0.000001, 'E':0.000001, 'S':0.499999},
   'S' : {'B': 0.499999, 'M': 0.000001, 'E':0.000001, 'S':0.499999}
   }
emit_p = {
   'B' : {},
   'M' : {},
   'E' : {},
   'S' : {}
   }


# initial
def initial():
    print("SMLA CUT")
    print("Version 0.1.1")
    print("Copyright 2017-2018 HuMan Ltd.,Co.")
    print("All Rights Reserved.")
    print("https://www.smart-lands.com/")
    print("")


# load emit probability of every Hans
def load_emit():
    emit = []
    sys_path = os.path.split(os.path.realpath(__file__))[0]
    emit_path = sys_path + "/data/emit/emit.json"
    print(":) Load emit file:", emit_path)
    f1 =open(emit_path,'r')
    emit = json.load(f1)
    print(":) Total Hans number:", len(emit))
    f1.close()
    return emit


# viterbi
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]

    # Initial Viterbi
    for st in states:
        V[0][st] = {"prob": vlog(start_p[st], emit_p[st][obs[0]]), "prev": None}
    # print(V)

    # Run Viterbi for words in obs
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            # 
            max_tr_prob = max( vlog(V[t-1][prev_st]["prob"], trans_p[prev_st][st]) for prev_st in states )
            # print(max_tr_prob)
            
            for prev_st in states:
                if vlog(V[t-1][prev_st]["prob"], trans_p[prev_st][st]) == max_tr_prob:
                    max_prob = vlog(max_tr_prob, emit_p[st][obs[t]])
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    
    # The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None

    # Get most probable state and its backtrack
    opt = []
    for st, data in V[-1].items():
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break

    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        # print(t)
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]

    #Results
    # for v in V:
    #     print(v)
    return(opt)
    print('The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob)


def vlog(a, b):
    c = a * b
    # c = math.pow(10, (math.log(a, 10) + math.log(b, 10)))
    # c = math.log(a, 10) + math.log(b, 10)
    return c


# gen emit
def emit_gen(user_input, emit):
    # clear obs and emit_p
    obs = []
    emit_p['B'] = {}
    emit_p['M'] = {}
    emit_p['E'] = {}
    emit_p['S'] = {}
    
    for char in user_input:
        char_hex = hex(ord(char))
        if int(char_hex, 16) >= Hans_L and int(char_hex, 16) <= Hans_R:
            # obs
            obs.append(char)
            # emit_p
            num = int(char_hex, 16) - Hans_L
            print(emit[num])
            # print(emit_sum)
            emit_p['B'][char] = emit[num][char]['B']
            emit_p['M'][char] = emit[num][char]['M']
            emit_p['E'][char] = emit[num][char]['E']
            emit_p['S'][char] = emit[num][char]['S']
    # print(obs)
    # print(emit_p)
    return(obs, emit_p)


# insert / to obs and opt
def insert(obs, opt):
    opt_num = 0
    pos_num = 0
    obs_out = obs
    opt_out = opt
    insert_position = []
    for opt_num in range(len(opt)):
        if opt[opt_num] == 'E' or opt[opt_num] == 'S':
            insert_position.append(opt_num)
    # print(insert_position)
    
    for position in insert_position:
        pos_num = pos_num + 1
        position = position + pos_num
        # print(position)
        opt_out.insert(position, '/')
        obs_out.insert(position, '/')
    
    return(opt_out, obs_out)


# user
def cut(user_input):
    
    emit = []
    # load emit.json
    emit = load_emit()

    # emit gen
    (obs, emit_p) = emit_gen(user_input, emit)
    
    # viterbi
    opt = viterbi(obs, states, start_p, trans_p, emit_p)
    # print(obs)
    # print(opt)
    
    # insert / to obs and opt
    (opt_out, obs_out) = insert(obs, opt)
    print(obs_out)
    print(opt_out)
    return obs_out, opt_out

