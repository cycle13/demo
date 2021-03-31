"""
=====================================================================
Generating Reverse and Clipped Trajectories After Original Experiment
=====================================================================

In the example ``计算.py``, the basic PySPLIT procedure
for generating HYSPLIT trajectories was presented.  While generating
bulk trajectories (``pysplit.generate_bulktraj()``), the user may choose
to also output "clipped" trajectory files, which are copies of the original
trajectory files that contain only path information, and/or "reverse"
trajectory files, which are newly calculated trajectories launched from
the endpoint of the original trajectories in the opposite direction in time.

For large experiments, creating these extra files, particularly the
"reverse" trajectories, can significantly inflate the run time.  So,
instead of generating the complementary "reverse" and "clipped"
trajectories during the main trajectory generation, the user may choose
to generate these extras later and with a subset of trajectories.


Setup
-----

Below, we'll generate back trajectories from the University of Minnesota,
forgoing the "reverse" and "clipped" trajectories (``get_reverse=False``,
``get_clipped=False``).  For a detailed explanation of this call, see
``计算.py``.  Then, initialize a TrajectoryGroup.

"""
from __future__ import print_function
import pysplit
import matplotlib.pyplot as plt

pysplit.generate_bulktraj('umn', r'D:/Program Files/pycharm/后向轨迹/working',
                          r'D:/Program Files/pycharm/后向轨迹/HYSPLIT/umn_example', r'D:/Program Files/pycharm/后向轨迹/gdasdata', [2021],
                          range(2,2), [6, 15, 18, 21], [500], (37.82, 111.54),
                          -120, get_clipped=False,hysplit='../TrajStat/working/hyts_std.exe')

trajgroup = pysplit.make_trajectorygroup(r'D:/Program Files/pycharm/后向轨迹/HYSPLIT/umn_example/*')

"""
In the course of our analysis, we might decide that a subset of trajectories
is more appropriate for our purpose.  Let's create a new ``TrajectoryGroup``
with all the trajectories with a temperature at t=0 of 0 degrees C and greater.

"""
for traj in trajgroup:
    print(traj.data.Temperature_C[0])

warm_trajlist = [traj for traj in trajgroup if traj.data.Temperature_C[0] > 0.0]

warm_trajgroup = pysplit.TrajectoryGroup(warm_trajlist)

"""
The new ``TrajectoryGroup`` is much smaller:

"""
print(trajgroup.trajcount)
print(warm_trajgroup.trajcount)

"""
Generation
----------

Now we generate the reverse trajectories and create the clipped trajectory 
files.

In ``Trajectory.generate_reversetraj()``, the arguments are
the HYSPLIT working directory, and the meteorology file location.  The kwargs
indicate the interval between meteorology files ('monthly', 'semimonthly',
'weekly', 'daily'), the directory to store the reverse trajectories in, if 
some location other than the default (in a folder in the trajectory directory)
is desired; and the location of the hysplit executable.

In ``Trajectory.generate_clippedtraj()``, the kwarg is the storage
location for the clipped trajectory files, if some location other than the default
is desired.  We use the default locations for clipped and reverse trajectories
in this example.

If any clipped or reverse trajectories corresponding to the trajectories
in ``warm_trajgroup`` exist in the storage directories, they will be overwritten.

If the reverse and clipped directories don't exist, they will be
created. 

"""
for traj in warm_trajgroup:
    traj.generate_reversetraj(r'D:/Program Files/pycharm/后向轨迹/working', r'D:/Program Files/pycharm/后向轨迹/gdasdata',
                              meteo_interval='weekly',
                              hysplit="'../TrajStat/working/hyts_std.exe'")

    traj.generate_clippedtraj()

"""
Loading and Mapping Reverse Trajectories
----------------------------------------
Load the reverse trajectory data via ``Trajectory.load_reversetraj()``.

For details on the sample basic plotting procedure, see
``可视化1.py``.  The original trajectories are plotted in
gold and the reverse trajectories in maroon.  Ideally, the reverse
trajectories will overlay the original trajectories.

"""
for traj in warm_trajgroup:
    traj.load_reversetraj()
    
mapcorners =  [-150, 15, -50, 65]
standard_pm = None

testmap = pysplit.MapDesign(mapcorners, standard_pm)

bmap = testmap.make_basemap()

for traj in warm_trajgroup[::5]:
    bmap.plot(*traj.path.xy, c='#FFB71E', latlon=True, zorder=20)
    bmap.plot(*traj.path_r.xy, c='#5B0013', latlon=True, zorder=20)

