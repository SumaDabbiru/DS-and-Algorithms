#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:25:40 2020

@author: Suma Dabbiru

"""
def artifact_routine(n, artifacts, searched):
    grid_map = {}
    artifacts_pieces = {}
    artifacts_searched = {}
    artifact_id = 0

    for artifact in artifacts.split(","):
        artifact_id = artifact_id + 1
        artifacts_pieces[artifact_id] = 0
        artifacts_searched[artifact_id] = 0

        for spot in artifact.split(" "):
            if spot != "":
                artifacts_pieces[artifact_id] = artifacts_pieces[artifact_id] + 1
                grid_map[spot] = artifact_id

    for spot in searched.split(" "):
        if spot in grid_map:
            artifact_loop_id = grid_map[spot]
            artifacts_searched[artifact_loop_id] = artifacts_searched[artifact_loop_id] + 1



    complete = 0
    partial = 0

    for artifact_id in artifacts_pieces:
        if artifact_id in artifacts_searched:
            if artifacts_pieces[artifact_id] == artifacts_searched[artifact_id]:
                complete = complete + 1
            elif artifacts_searched[artifact_id] >= 1:
                partial = partial + 1


    return [complete,partial]




    
 

N=4
artifacts="1B 2C,2D 4D"
searched ="2B 2D 3D 4D 4A"
print(solution(N, artifacts, searched))
