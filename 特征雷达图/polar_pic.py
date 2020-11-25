import data_visual
import data_opt






now_time = '2020-11-22'
file_dir = '淮阳县.xls'
newfile_dir = '淮阳县.xlsx'
data_opt.tezheng(file_dir,newfile_dir,now_time)



data_visual.plot_radar(newfile_dir,now_time)