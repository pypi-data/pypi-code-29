"""
Spatially join misaligned polygons
"""

import os
import argparse
import numpy as np
import geopandas as gpd
import pandas as pd


class AreaWeightedJoin:

    def __init__(self, source_uri, source_uuid, target_uri, target_uuid):
        self.source_uri = source_uri
        self.source_uuid = source_uuid
        self.target_uri = target_uri
        self.target_uuid = target_uuid

    @property
    def source_gdf(self):
        return gpd.read_file(self.source_uri)

    @property
    def target_gdf(self):
        return gpd.read_file(self.target_uri)

    @staticmethod
    def gdf_to_file(gdf, output_filename):
        if gdf is not None:
            if os.path.exists(output_filename):
                os.remove(output_filename)
            gdf.to_file(driver="GeoJSON", filename=output_filename)

    def set_source_areas(self):
        try:
            uuids = self.source_gdf[self.source_uuid]
        except KeyError:
            print('The UUID is not present in source geographies.')
        areas = self.source_gdf['geometry'].area
        self.source_areas = dict(zip(uuids, areas))

    def join(self, variable, rate):
        if self.source_uuid not in self.source_gdf.columns:
            print('The UUID is not present in source geographies.')
        elif self.target_uuid not in self.target_gdf.columns:
            print('The UUID is not present in target geographies.')
        elif variable not in self.source_gdf.columns:
            print('The variable is not present in target geographies.')
        else:
            union = gpd.overlay(self.target_gdf, self.source_gdf, how='union')
            self.set_source_areas()
            proportions = {}
            for k, v in union.iterrows():
                if v[self.source_uuid] in self.source_areas.keys():
                    prop_value = v['geometry'].area / \
                        self.source_areas[v[self.source_uuid]]
                    prop_key = (v[self.target_uuid], v[self.source_uuid])
                    proportions[prop_key] = prop_value
            fields = [self.source_uuid, self.target_uuid, variable]
            union = pd.DataFrame(union)[fields]
            union = union.dropna(subset=[self.source_uuid])
            union['proportion'] = union.apply(
                lambda x: proportions[(x[1], x[0])], 1)
            union['value'] = union.apply(lambda x: x[3] * x[2], 1)
            union = union[[self.target_uuid, 'value', 'proportion']]
            self.unioned = union
            proportional_results = union.groupby(
                [self.target_uuid]).sum().reset_index()
            if rate:
                proportional_results[variable] = proportional_results[
                    'value'] / proportional_results['proportion']
            else:
                proportional_results[variable] = proportional_results['value']
            proportional_results = proportional_results[
                [self.target_uuid, variable]]
            self.aggregated = pd.merge(
                self.target_gdf, proportional_results, on=self.target_uuid)
            return self.aggregated


def main(source_uri, source_uuid, target_uri, target_uuid, variable, output_filename, rate):
    join_task = proportional_join(
        source_uri, source_uuid, target_uri, target_uuid)
    output_gdf = join_task.join(variable, rate)
    join_task.gdf_to_file(output_gdf, output_filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source_uri')
    parser.add_argument('source_uuid')
    parser.add_argument('target_uri')
    parser.add_argument('target_uuid')
    parser.add_argument('variable')
    parser.add_argument('output_filename')
    parser.add_argument('rate')
    args = parser.parse_args()
    main(args.source_uri, args.source_uuid, args.target_uri, args.target_uuid,
         args.variable, args.output_filename, args.rate)
