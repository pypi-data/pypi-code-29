# Copyright (c) 2016-2017 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Autogenerated python message buffer code.
Source: clad/audio/audioSwitchTypes.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/audio/audioSwitchTypes.clad
"""

from __future__ import absolute_import
from __future__ import print_function

def _modify_path():
  import inspect, os, sys
  search_paths = [
    '../..',
    '../../../../tools/message-buffers/support/python',
  ]
  currentpath = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))
  for search_path in search_paths:
    search_path = os.path.normpath(os.path.abspath(os.path.realpath(os.path.join(currentpath, search_path))))
    if search_path not in sys.path:
      sys.path.insert(0, search_path)
_modify_path()

import msgbuffers

Anki = msgbuffers.Namespace()
Anki.AudioMetaData = msgbuffers.Namespace()
Anki.AudioMetaData.SwitchState = msgbuffers.Namespace()

class Codelab__Music_Tiny_Orchestra(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                               = 0
  Tiny_Orchestra_Bass_Mode_1_Off        = 2773389205
  Tiny_Orchestra_Bass_Mode_1_On         = 4225872937
  Tiny_Orchestra_Bass_Mode_2_Off        = 3114422790
  Tiny_Orchestra_Bass_Mode_2_On         = 2510905384
  Tiny_Orchestra_Bass_Mode_3_Off        = 1797181875
  Tiny_Orchestra_Bass_Mode_3_On         = 36806655
  Tiny_Orchestra_Glock_Pluck_Mode_1_Off = 1674194378
  Tiny_Orchestra_Glock_Pluck_Mode_1_On  = 2421905196
  Tiny_Orchestra_Glock_Pluck_Mode_2_Off = 4210083577
  Tiny_Orchestra_Glock_Pluck_Mode_2_On  = 3631119949
  Tiny_Orchestra_Glock_Pluck_Mode_3_Off = 2569343836
  Tiny_Orchestra_Glock_Pluck_Mode_3_On  = 1273367574
  Tiny_Orchestra_Strings_Mode_1_Off     = 1597550140
  Tiny_Orchestra_Strings_Mode_1_On      = 2524543094
  Tiny_Orchestra_Strings_Mode_2_Off     = 104978871
  Tiny_Orchestra_Strings_Mode_2_On      = 1209427331
  Tiny_Orchestra_Strings_Mode_3_Off     = 702297514
  Tiny_Orchestra_Strings_Mode_3_On      = 3673080460

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra = Codelab__Music_Tiny_Orchestra
del Codelab__Music_Tiny_Orchestra


class Codelab__Music_Tiny_Orchestra_Bass(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                      = 0
  Tiny_Orchestra_Bass_Mode_1   = 4077279363
  Tiny_Orchestra_Bass_Mode_2   = 4077279360
  Tiny_Orchestra_Bass_Mode_3   = 4077279361
  Tiny_Orchestra_Bass_Mode_Off = 3450676341

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Bass = Codelab__Music_Tiny_Orchestra_Bass
del Codelab__Music_Tiny_Orchestra_Bass


class Codelab__Music_Tiny_Orchestra_Bass_Mode_1(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                        = 0
  Tiny_Orchestra_Bass_Mode_1_Off = 2773389205
  Tiny_Orchestra_Bass_Mode_1_On  = 4225872937

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Bass_Mode_1 = Codelab__Music_Tiny_Orchestra_Bass_Mode_1
del Codelab__Music_Tiny_Orchestra_Bass_Mode_1


class Codelab__Music_Tiny_Orchestra_Bass_Mode_2(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                        = 0
  Tiny_Orchestra_Bass_Mode_2_Off = 3114422790
  Tiny_Orchestra_Bass_Mode_2_On  = 2510905384

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Bass_Mode_2 = Codelab__Music_Tiny_Orchestra_Bass_Mode_2
del Codelab__Music_Tiny_Orchestra_Bass_Mode_2


class Codelab__Music_Tiny_Orchestra_Bass_Mode_3(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                        = 0
  Tiny_Orchestra_Bass_Mode_3_Off = 1797181875
  Tiny_Orchestra_Bass_Mode_3_On  = 36806655

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Bass_Mode_3 = Codelab__Music_Tiny_Orchestra_Bass_Mode_3
del Codelab__Music_Tiny_Orchestra_Bass_Mode_3


class Codelab__Music_Tiny_Orchestra_Glock_Pluck(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                             = 0
  Tiny_Orchestra_Glock_Pluck_Mode_1   = 1695515796
  Tiny_Orchestra_Glock_Pluck_Mode_2   = 1695515799
  Tiny_Orchestra_Glock_Pluck_Mode_3   = 1695515798
  Tiny_Orchestra_Glock_Pluck_Mode_Off = 2017008174

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Glock_Pluck = Codelab__Music_Tiny_Orchestra_Glock_Pluck
del Codelab__Music_Tiny_Orchestra_Glock_Pluck


class Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_1(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                               = 0
  Tiny_Orchestra_Glock_Pluck_Mode_1_Off = 1674194378
  Tiny_Orchestra_Glock_Pluck_Mode_1_On  = 2421905196

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_1 = Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_1
del Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_1


class Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_2(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                               = 0
  Tiny_Orchestra_Glock_Pluck_Mode_2_Off = 4210083577
  Tiny_Orchestra_Glock_Pluck_Mode_2_On  = 3631119949

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_2 = Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_2
del Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_2


class Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_3(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                               = 0
  Tiny_Orchestra_Glock_Pluck_Mode_3_Off = 2569343836
  Tiny_Orchestra_Glock_Pluck_Mode_3_On  = 1273367574

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_3 = Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_3
del Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_3


class Codelab__Music_Tiny_Orchestra_Strings(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                         = 0
  Tiny_Orchestra_Strings_Mode_1   = 1790990774
  Tiny_Orchestra_Strings_Mode_2   = 1790990773
  Tiny_Orchestra_Strings_Mode_3   = 1790990772
  Tiny_Orchestra_Strings_Mode_Off = 3180178332

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Strings = Codelab__Music_Tiny_Orchestra_Strings
del Codelab__Music_Tiny_Orchestra_Strings


class Codelab__Music_Tiny_Orchestra_Strings_Mode_1(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                           = 0
  Tiny_Orchestra_Strings_Mode_1_Off = 1597550140
  Tiny_Orchestra_Strings_Mode_1_On  = 2524543094

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Strings_Mode_1 = Codelab__Music_Tiny_Orchestra_Strings_Mode_1
del Codelab__Music_Tiny_Orchestra_Strings_Mode_1


class Codelab__Music_Tiny_Orchestra_Strings_Mode_2(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                           = 0
  Tiny_Orchestra_Strings_Mode_2_Off = 104978871
  Tiny_Orchestra_Strings_Mode_2_On  = 1209427331

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Strings_Mode_2 = Codelab__Music_Tiny_Orchestra_Strings_Mode_2
del Codelab__Music_Tiny_Orchestra_Strings_Mode_2


class Codelab__Music_Tiny_Orchestra_Strings_Mode_3(object):
  "Automatically-generated uint_32 enumeration."
  Invalid                           = 0
  Tiny_Orchestra_Strings_Mode_3_Off = 702297514
  Tiny_Orchestra_Strings_Mode_3_On  = 3673080460

Anki.AudioMetaData.SwitchState.Codelab__Music_Tiny_Orchestra_Strings_Mode_3 = Codelab__Music_Tiny_Orchestra_Strings_Mode_3
del Codelab__Music_Tiny_Orchestra_Strings_Mode_3


class Cozmo_Sings_100Bpm(object):
  "Automatically-generated uint_32 enumeration."
  Cozmo_Sings_Beautiful_Dreamer   = 366264019
  Cozmo_Sings_Beethovens_5Th      = 234196460
  Cozmo_Sings_Bingo               = 2671798574
  Cozmo_Sings_Buffalo_Gals        = 1616439696
  Cozmo_Sings_Camptown_Races      = 2068892721
  Cozmo_Sings_Can_Can_1           = 1565293210
  Cozmo_Sings_Can_Can_2           = 1565293209
  Cozmo_Sings_Farmer_In_The_Dell  = 3199213520
  Cozmo_Sings_Itsy_Bitsy_Spider   = 4216855774
  Cozmo_Sings_London_Bridge       = 1890869377
  Cozmo_Sings_Mountain_King       = 2556694018
  Cozmo_Sings_Muss_I_Denn         = 2520896685
  Cozmo_Sings_Pop_Goes_The_Weasel = 2629521585
  Cozmo_Sings_Row_Your_Boat       = 468566904
  Cozmo_Sings_Ta_Ra_Ra_Boom       = 2367266190
  Cozmo_Sings_Tisket_Tasket       = 2168319140
  Cozmo_Sings_Yellow_Rose         = 3186274273
  Invalid                         = 0

Anki.AudioMetaData.SwitchState.Cozmo_Sings_100Bpm = Cozmo_Sings_100Bpm
del Cozmo_Sings_100Bpm


class Cozmo_Sings_120Bpm(object):
  "Automatically-generated uint_32 enumeration."
  Cozmo_Sings_Cozmambo                = 885738211
  Cozmo_Sings_Entry_Of_The_Gladiators = 2101741982
  Cozmo_Sings_Hello_My_Baby           = 1653598059
  Cozmo_Sings_Hush_Little_Baby        = 4192423907
  Cozmo_Sings_La_Paloma               = 2263560367
  Cozmo_Sings_Moonlight_Bay           = 3990987963
  Cozmo_Sings_Ode_To_Joy              = 277478768
  Cozmo_Sings_Sakura                  = 1066913866
  Cozmo_Sings_Silvery_Moon            = 2709516065
  Cozmo_Sings_Toccata                 = 2295405948
  Cozmo_Sings_Turkey_In_The_Straw     = 222542119
  Cozmo_Sings_Twinkle_Twinkle         = 2925972690
  Cozmo_Sings_Wild_About_Harry        = 2245203260
  Invalid                             = 0

Anki.AudioMetaData.SwitchState.Cozmo_Sings_120Bpm = Cozmo_Sings_120Bpm
del Cozmo_Sings_120Bpm


class Cozmo_Sings_80Bpm(object):
  "Automatically-generated uint_32 enumeration."
  Cozmo_Sings_Aba_Daba                    = 2234458138
  Cozmo_Sings_Danny_Boy                   = 3740392146
  Cozmo_Sings_Farmer_In_The_Dell          = 3199213520
  Cozmo_Sings_Frere_Jacques               = 1503161152
  Cozmo_Sings_Habanera                    = 2657364191
  Cozmo_Sings_Mary_Had_A_Little_Lamb      = 4246470244
  Cozmo_Sings_Muffin_Man                  = 197233699
  Cozmo_Sings_Mulberry_Bush               = 2808835548
  Cozmo_Sings_Pachebel_Canon              = 553164015
  Cozmo_Sings_Take_Me_Out_To_The_Ballgame = 330639210
  Cozmo_Sings_Vivaldi_Spring              = 3538265926
  Cozmo_Sings_Water_Music                 = 583110970
  Cozmo_Sings_William_Tell                = 2911111070
  Cozmo_Sings_Yankee_Doodle               = 3906943052
  Invalid                                 = 0

Anki.AudioMetaData.SwitchState.Cozmo_Sings_80Bpm = Cozmo_Sings_80Bpm
del Cozmo_Sings_80Bpm


class Cozmo_Voice_Processing(object):
  "Automatically-generated uint_32 enumeration."
  Invalid     = 0
  Name        = 797654004
  Sentence    = 906532866
  Unprocessed = 860658140

Anki.AudioMetaData.SwitchState.Cozmo_Voice_Processing = Cozmo_Voice_Processing
del Cozmo_Voice_Processing


class External(object):
  "Automatically-generated uint_32 enumeration."
  External_Long    = 3001056757
  External_Maximum = 1931150551
  External_Medium  = 3619992510
  External_Short   = 1727626579
  Invalid          = 0

Anki.AudioMetaData.SwitchState.External = External
del External


class Freeplay_Mood(object):
  "Automatically-generated uint_32 enumeration."
  Arcade                = 1946377065
  Bored                 = 2890913445
  Busy                  = 1427625958
  Chill                 = 4294400669
  Cubeinteract          = 889740396
  Dancing               = 386094975
  Guard_Dog             = 1030326287
  Happy                 = 1427264549
  Hiking                = 296159617
  Invalid               = 0
  Neutral               = 670611050
  Neutral_Cubes_Stacked = 2172443987
  Neutral_Lift_Cube     = 1603627138
  Neutral_Request_Game  = 3496250545
  Nurture_Feeding       = 2320504975
  Nurture_Nirvana       = 3261805104
  Nurture_Repair        = 3081923682
  Nurture_Severe        = 1058497985
  Sleep                 = 3671647190

Anki.AudioMetaData.SwitchState.Freeplay_Mood = Freeplay_Mood
del Freeplay_Mood


class Gameplay_Round(object):
  "Automatically-generated uint_32 enumeration."
  Invalid  = 0
  Round_00 = 4039654994
  Round_01 = 4039654995
  Round_02 = 4039654992
  Round_03 = 4039654993
  Round_04 = 4039654998
  Round_05 = 4039654999
  Round_06 = 4039654996
  Round_07 = 4039654997
  Round_08 = 4039655002
  Round_09 = 4039655003
  Round_10 = 4056432581

Anki.AudioMetaData.SwitchState.Gameplay_Round = Gameplay_Round
del Gameplay_Round


class GenericSwitch(object):
  "Automatically-generated uint_32 enumeration."
  Invalid = 0

Anki.AudioMetaData.SwitchState.GenericSwitch = GenericSwitch
del GenericSwitch


class Mood(object):
  "Automatically-generated uint_32 enumeration."
  Invalid      = 0
  Mood_Happy   = 457607035
  Mood_Neutral = 3970296952
  Mood_Sad     = 777739821

Anki.AudioMetaData.SwitchState.Mood = Mood
del Mood


class Relationship(object):
  "Automatically-generated uint_32 enumeration."
  Invalid               = 0
  Realtionship_Bff      = 743952678
  Realtionship_Friend   = 1061927592
  Relationship_Stranger = 3087192196

Anki.AudioMetaData.SwitchState.Relationship = Relationship
del Relationship


class Sparked(object):
  "Automatically-generated uint_32 enumeration."
  Fun     = 982472036
  Invalid = 0
  Pyramid = 797712787
  Sneaky  = 468648200
  Workout = 1875882538

Anki.AudioMetaData.SwitchState.Sparked = Sparked
del Sparked


class SwitchGroupType(object):
  "Automatically-generated uint_32 enumeration."
  Codelab__Music_Tiny_Orchestra                    = 981129199
  Codelab__Music_Tiny_Orchestra_Bass               = 57798143
  Codelab__Music_Tiny_Orchestra_Bass_Mode_1        = 3356335735
  Codelab__Music_Tiny_Orchestra_Bass_Mode_2        = 3356335732
  Codelab__Music_Tiny_Orchestra_Bass_Mode_3        = 3356335733
  Codelab__Music_Tiny_Orchestra_Glock_Pluck        = 294713538
  Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_1 = 1120265808
  Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_2 = 1120265811
  Codelab__Music_Tiny_Orchestra_Glock_Pluck_Mode_3 = 1120265810
  Codelab__Music_Tiny_Orchestra_Strings            = 802212004
  Codelab__Music_Tiny_Orchestra_Strings_Mode_1     = 1004765386
  Codelab__Music_Tiny_Orchestra_Strings_Mode_2     = 1004765385
  Codelab__Music_Tiny_Orchestra_Strings_Mode_3     = 1004765384
  Cozmo_Sings_100Bpm                               = 3759662965
  Cozmo_Sings_120Bpm                               = 2987768599
  Cozmo_Sings_80Bpm                                = 3366294904
  Cozmo_Voice_Processing                           = 366280094
  External                                         = 1442075084
  Freeplay_Mood                                    = 2205807877
  Gameplay_Round                                   = 2536359484
  Invalid                                          = 0
  Mood                                             = 3128647864
  Relationship                                     = 3723222599
  Sparked                                          = 62349551
  World_Event                                      = 846944294

Anki.AudioMetaData.SwitchState.SwitchGroupType = SwitchGroupType
del SwitchGroupType


class World_Event(object):
  "Automatically-generated uint_32 enumeration."
  Cubes_Stacked = 2547007631
  Invalid       = 0
  Lift_Cube     = 3497001966
  Request_Game  = 2296204869

Anki.AudioMetaData.SwitchState.World_Event = World_Event
del World_Event


