# -*- coding: utf-8 -*-
import pandas as pd

class Output_Objects(object):
    def __init__(self, parent):
        self.parent = parent
        self.node_df = self.get_node_df()
        self.cluster_df = self.get_cluster_df()
        self.progress_df = self.get_progress_df()
        self.summary_df = self.get_summary_df()
        self.final_slinks_df = self.get_final_slinks_df()
        self.final_nlinks_df = self.get_final_nlinks_df()

    def get_summary_df(self):
        ## working 11/04
        nodes = self.parent.sg.nodes
        nlinks = self.parent.sg.nlinks
        slinks = self.parent.sg.slinks
        final_slinks = self.parent.sg.slinks_final
        cluster_pairs = self.parent.sg.nlinks_final
        clusters = self.parent.pg.clusters
        lines = self.parent.pg.progress
        cv = self.parent.critical_value
        dic = dict(
            nodes=len(nodes),
            npair=len(nlinks),
            slink=len(slinks),
            final_cpair=len(cluster_pairs),
            final_slink=len(final_slinks),
            clusterno=len(clusters),
            progressno=len(lines),
            critical_value=cv)
        df_summary = pd.DataFrame.from_dict(dict(attribute=dic))
        return df_summary

    def get_node_df(self):
        nodes = self.parent.sg.nodes
        ii = []#[c.idd for c in nodes]
        xx = []#[c.xcor for c in nodes]
        yy = []#[c.ycor for c in nodes]
        tt = []#[c.time for c in nodes]
        cl = []#[c.cluster_id for c in nodes]
        ch = []#[c.chain_id for c in nodes]
        nc = []#[len(c.incoming) for c in nodes]
        ou = []#[len(c.outgoing) for c in nodes]
        ne = []#[len(c.neighbors) for c in nodes]
        for n in nodes:
            ii.append(n.idd)
            xx.append(n.xcor)
            yy.append(n.ycor)
            tt.append(n.time)
            cl.append(n.cluster_id)
            ch.append(n.chain_id)
            nc.append(len(n.incoming))
            ou.append(len(n.outgoing))
            ne.append(len(n.neighbors))

        df_nodes = pd.DataFrame.from_dict({'node_id':ii, 'xx':xx, 'yy':yy, 'time':tt, 'cluster_id':cl, 'chain_id':ch, 'in_size':nc, 'out_size':ou, 'neig_size':ne})
        df_nodes = df_nodes[['node_id', 'xx', 'yy', 'time', 'cluster_id', 'chain_id', 'in_size', 'out_size', 'neig_size']]
        #self.node_df = df_nodes
        return df_nodes

    def get_cluster_df(self):
        clusters = self.parent.pg.clusters
        xx = []#[c.xcor for c in clusters]
        yy = []#[c.ycor for c in clusters]
        ss = []#[c.cluster_size for c in clusters]
        tt = []#[c.time_median for c in clusters]
        t0 = []#[c.time_start for c in clusters]
        t1 = []#[c.time_stop for c in clusters]
        cl = []#[c.cluster_id for c in clusters]
        ch = []#[c.chain_id for c in clusters]
        bvr = []
        ins = []
        ous = []
        for c in clusters:
            xx.append(c.xcor)
            yy.append(c.ycor)
            ss.append(c.cluster_size)
            tt.append(c.time_median)
            t0.append(c.time_start)
            t1.append(c.time_stop)
            cl.append(c.cluster_id)
            ch.append(c.chain_id)
            bvr.append(c.behaviors)
            ins.append(len(c.incomings))
            ous.append(len(c.outgoings))
        df_clusters = pd.DataFrame.from_dict({'cluster_id':cl, 'chain_id':ch, 'xx':xx, 'yy':yy, 'cluster_size':ss, 'time_median':tt, 'time_start':t0, 'time_stop':t1, 'behaviors':bvr, 'in_count':ins, 'out_count':ous})
        df_clusters = df_clusters[['cluster_id', 'chain_id', 'xx', 'yy', 'cluster_size', 'time_median', 'time_start', 'time_stop', 'behaviors', 'in_count', 'out_count']]
        #self.cluster_df = df_clusters
        return df_clusters

    def get_progress_df(self):
        #progress = self.pg.progress
        lines = self.parent.pg.progress
        ii = 0
        lines_dict = {}
        for line in lines:
            i0 = line.origin.cluster_id
            i1 = line.destination.cluster_id
            s0 = line.origin.cluster_size
            s1 = line.destination.cluster_size
            x0 = line.origin.xcor
            x1 = line.destination.xcor
            y0 = line.origin.ycor
            y1 = line.destination.ycor
            z0 = line.origin.time_start
            z1 = line.destination.time_stop
            clid = line.destination.cluster_id
            chid = line.destination.chain_id
            op = line.ori_pos
            no_SL = line.no_slink
            lines_dict[ii] = {'id0':i0, 'id1':i1, 'clid':clid, 'chid':chid, 'size0':s0, 'size1':s1, 'x0':x0, 'x1':x1, 'y0':y0, 'y1':y1, 't0':z0, 't1':z1, 'op':op, 'no_SL':no_SL}
            ii=ii+1
        if len(lines)<=0:
            lines_dict[ii] = {'id0':'-', 'id1':'-', 'clid':'-', 'chid':'-', 'size0':'-', 'size1':'-', 'x0':'-', 'x1':'-', 'y0':'-', 'y1':'-',
            't0':'-',  't1':'-',  'op':'-', 'no_SL':'-'}
        df_progress = pd.DataFrame.from_dict(lines_dict, orient='index')
        df_progress = df_progress[['id0','id1','clid','chid','size0','size1','x0','x1','y0','y1','t0','t1','op','no_SL']]
        #self.progress_df = df_progress
        return df_progress

    def get_final_slinks_df(self):
        final_slinks = self.parent.sg.slinks_final
        final_dict = {}
        i = 0
        if len(final_slinks)>0:
            for sl in final_slinks:
                oo = sl.origin
                dd = sl.destination
                sldic = dict(
                    ooid = oo.idd,
                    ddid = dd.idd,
                    srisk = sl.spatial_risk,
                    trisk = sl.temporal_risk,
                    crisk = sl.combine_risk,
                    opossi = sl.ori_possibility,
                    oxcor = oo.xcor,
                    oycor = oo.ycor,
                    otime = oo.time,
                    dxcor = dd.xcor,
                    dycor = dd.ycor,
                    dtime = dd.time,
                    clid = dd.cluster_id,
                    chid = dd.chain_id,
                )
                final_dict[i] = sldic
                i+=1
        else:
            sldic = dict(
                ooid = '-',
                ddid = '-',
                srisk = '-',
                trisk = '-',
                crisk = '-',
                opossi = '-',
                oxcor = '-',
                oycor = '-',
                otime = '-',
                dxcor = '-',
                dycor = '-',
                dtime = '-',
                clid = '-',
                chid = '-',
            )
            final_dict[i] = sldic
        f_sls = pd.DataFrame.from_dict(final_dict, orient='index')
        f_sls = f_sls[['ooid','ddid','clid','chid','srisk','trisk','crisk','opossi','oxcor','oycor','otime','dxcor','dycor','dtime']]
        return f_sls

    def get_final_nlinks_df(self):
        cluster_pairs = self.parent.sg.nlinks_final
        final_dict = {}
        i = 0
        if len(cluster_pairs)>0:
            for cp in cluster_pairs:
                n1 = cp.one
                n2 = cp.two
                cpdic = dict(
                    n1_id = n1.idd,
                    n2_id = n2.idd,
                    clid = n1.cluster_id,
                    chid = n1.chain_id,
                    max_cop = cp.max_cop,
                    n1x = n1.xcor,
                    n1y = n1.ycor,
                    n2x = n2.xcor,
                    n2y = n2.ycor,
                    n1t = n1.time,
                    n2t = n2.time,
                )
                final_dict[i] = cpdic
                i+=1
        else:
            cpdic = dict(
                n1_id = '-',
                n2_id = '-',
                clid = '-',
                chid = '-',
                max_cop = '-',
                n1x = '-',
                n1y = '-',
                n2x = '-',
                n2y = '-',
                n1t = '-',
                n2t = '-',
            )
            final_dict[i] = cpdic
        f_nps = pd.DataFrame.from_dict(final_dict, orient='index')
        f_nps = f_nps[['n1_id', 'n2_id', 'clid', 'chid', 'max_cop','n1x','n1y','n2x','n2y', 'n1t', 'n2t']]
        return f_nps
