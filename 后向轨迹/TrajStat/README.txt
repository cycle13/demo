
TrajStat plugin for MeteoInfo Java Edition

INTRODUCTION

  TrajStat is a free software plugin of MeteoInfo with some trajectory statistics functions.
  The trajectory calculation module of HYSPLIT (http://www.arl.noaa.gov/ready/hysplit4.html)
  was included in TrajStat as an external process to calculate trajectories. Monthly trajectories
  could be calculated in TrajStat, and the trajectories could be converted to GIS (Geographic Information System)
  line shape file. Cluster analysis function is included in the software. Measurement data could be added to the
  corresponding trajectories, so the trajectories could be selected according to the measurement data. 
  The software also can do PSCF (Potential Source Contribution Function) and CWT (Concentration Weighted Trajectory)
  analysis which is useful to identify pollution sources spatially for long-term environment measurement.

  It requires that Java 6 be installed on your computer. See the
  Java.com website for a free download of Java if you do not have it
  already installed.
  
  Publication:
  Wang, Y.Q., Zhang, X.Y. and Draxler, R., 2009. TrajStat: GIS-based software that uses various trajectory 
  statistical analysis methods to identify potential sources from long-term air pollution measurement data. 
  Environmental Modelling & Software, 24: 938-939.


DOWNLOADING

  The current version of TrajStat, along with other information about the
  application, may always be found at

  http://www.meteothinker.com/


INSTALLING AND RUNNING THE "STANDARD" TRAJSTAT PLUGIN

  The complete TrajStat Java package should, after uncompression, include
  the following items:
  
  - TrajStat plugin library file called "TrajStat.jar".
  - Default TrajStat project file called "default.mip".
  - Trajectory calculation files in a folder called "working".
  - Sample data files in a folder called "sample".
  - Legend sample files in a folder called "legend".
  - Support data files for trajectory calculation in a folder called "bdyfiles".
  - This README file.
  
  Copy the unzipped TrajStat folder into the "plugins" folder of MeteoInfo installation path. 
  Start the MeteoInfo program and open Plugin Manager dialog, then press "Update List" button 
  to add TrajStat plugin in the plugin list. The plugin can be loaded in Plugin Manager dialog 
  or by pressing the plugin sub-menu under "Plugin" menu. "TrajStat" menu will be added after 
  the plugin is loaded, and all functions are included under the menu..


HELP AND OTHER DOCUMENTATION

  More details about TrajStat are available at:
  
    http://www.meteothinker.com/


CONTACT

  TrajStat was written by Dr. Yaqiang Wang. 
  Please send bug reports, etc., to:
  
  Yaqiang Wang
  yaqiang.wang@gmail.com
  Chinese Academy of Meteorological Sciences
  46 Zhong-Guan-Cun South Avenue, Beijing, China


ACKNOWLEDGMENTS

  TrajStat uses following Java classes and libraries:
  
  MeteoInfo: Available at http://www.meteothinker.com/
  JFreeChart: Available at http://www.jfree.org/jfreechart/
  JavaHelp: Available at https://javahelp.java.net/