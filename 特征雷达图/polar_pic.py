import data_visual
import data_opt





for now_time in ["商水县","太康县","扶沟县",'沈丘县','淮阳县','西华县','郸城县','项城市','鹿邑县']:
    file_dir = 'excelfile/周口市2020-11-25 10时.xls'
    newfile_dir = 'excelfile/周口市2020-11-25 10时.xlsx'
    name = data_opt.tezheng(file_dir,newfile_dir,now_time)
    data_visual.plot_radar(newfile_dir,now_time,name)