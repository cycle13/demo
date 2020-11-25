import data_visual
import data_opt






now_time = '2020-11-22'
file_dir = 'excelfile/淮阳县.xls'
newfile_dir = 'excelfile/淮阳县.xlsx'
name = data_opt.tezheng(file_dir,newfile_dir,now_time)



data_visual.plot_radar(newfile_dir,now_time,name)