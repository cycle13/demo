import data_visual
import data_opt
from datetime import datetime
import datetime as datatime
import pandas as pd
# import datetime
from flask import Flask,render_template,request, send_from_directory,make_response
from werkzeug.utils import secure_filename
import os
import json


app = Flask(__name__)


def area_hour_acc_data(start_date_time,end_date_time,area_name,name1,namell,name2):
    ls = []
    # area_name = '淮阳县'
    # start_date_time = '2021-01-01 02:00:00'
    # end_date_time = '2021-01-02 04:00:00'
    start_date_time1 = datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    end_date_time1 = datetime.strptime(end_date_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    date_times = pd.date_range(start_date_time1, end_date_time1,freq='D')
    for date_time in date_times:
        date_time = datetime.strptime(date_time.strftime("%Y-%m-%d"),"%Y-%m-%d")
        my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d'), '2050-01-01')
        result = my_datatime[0].strftime('%Y-%m-%d')
        start_date = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
        end_date = (my_datatime[0] + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
        file_dir = 'static/uploads/{}.xls'.format(name1)
        file_cen_dir = 'static/uploads/{}cen.xls'.format(name1)
        newfile_dir = 'static/uploads/{}end.xls'.format(name1)
        newfile_acc_dir = 'static/uploads/{}acc.xls'.format(name1)
        df1 = pd.read_excel(file_dir,sheet_name='Sheet1')
        df1.index = df1['时间']
        df1 = df1[start_date:end_date]
        if datetime.strptime(end_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                date_time.strftime('%Y-%m-%d') + ' 23:00:00', '%Y-%m-%d %H:%M:%S'):
            if datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                    date_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'):
                my_datatime = pd.date_range(start_date_time,
                                            date_time.strftime('%Y-%m-%d') + ' 23:00:00', freq='h')
            else:
                my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d %H:%M:%S'),
                                            date_time.strftime('%Y-%m-%d') + ' 23:00:00', freq='h')
        else:
            if datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                    date_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'):
                my_datatime = pd.date_range(start_date_time,
                                            end_date_time, freq='h')
            else:
                my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d %H:%M:%S'), end_date_time, freq='h')
        df2 = pd.read_excel(file_dir, sheet_name='Sheet2')
        df2.index = df2['时间']
        df4 = df2[my_datatime[0].strftime('%Y-%m-%d %H:%M:%S'):my_datatime[-1].strftime('%Y-%m-%d %H:%M:%S')]
        df4.to_excel(newfile_acc_dir)
        for i in my_datatime:
            j = i.strftime('%Y-%m-%d %H:%M:%S')
            k = i.strftime('%Y-%m-%d %H%M%S')
            df3 = df2[j:j]
            df = df1.append(df3)
            df.to_excel(file_cen_dir, index=False)
            name = data_opt.tezheng_area(file_cen_dir, newfile_dir, i,area_name)
            k = k.replace(' ','_')
            data_visual.plot_radar_time(newfile_dir, k, name[0],namell,name2)
            ls.append(name2+k+'.png')
    return ls


# 滚动计算每一小时的时间累计特征雷达图
def time_hour_acc_data(start_date_time,end_date_time,name1,namell,name2):
    ls = []
    # start_date_time = '2021-02-10 13:00:00'
    # end_date_time = '2021-02-13 04:00:00'
    print(start_date_time,end_date_time)
    start_date_time1 = datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    end_date_time1 = datetime.strptime(end_date_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    date_times = pd.date_range(start_date_time1, end_date_time1, freq='D')
    for date_time in date_times:
        print(date_time)
        date_time = datetime.strptime(date_time.strftime("%Y-%m-%d"), "%Y-%m-%d")
        my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d'), '2050-01-01')
        result = my_datatime[0].strftime('%Y-%m-%d')
        start_date = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
        end_date = (my_datatime[0] + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
        file_dir = 'static/uploads/{}.xls'.format(name1)
        file_cen_dir = 'static/uploads/{}cen.xls'.format(name1)
        newfile_dir = 'static/uploads/{}end.xls'.format(name1)
        newfile_acc_dir = 'static/uploads/{}acc.xls'.format(name1)
        df1 = pd.read_excel(file_dir,sheet_name='Sheet1')
        df1.index = df1['时间']
        df1 = df1[start_date:end_date]
        if datetime.strptime(end_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                date_time.strftime('%Y-%m-%d') + ' 23:00:00', '%Y-%m-%d %H:%M:%S'):
            if datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                    date_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'):
                my_datatime = pd.date_range(start_date_time,
                                            date_time.strftime('%Y-%m-%d') + ' 23:00:00', freq='h')
            else:
                my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d %H:%M:%S'),
                                            date_time.strftime('%Y-%m-%d') + ' 23:00:00', freq='h')
        else:
            if datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                    date_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'):
                my_datatime = pd.date_range(start_date_time,
                                            end_date_time, freq='h')
            else:
                my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d %H:%M:%S'), end_date_time, freq='h')
        df2 = pd.read_excel(file_dir, sheet_name='Sheet2')
        df2.index = df2['时间']
        df4 = df2[my_datatime[0].strftime('%Y-%m-%d %H:%M:%S'):my_datatime[-1].strftime('%Y-%m-%d %H:%M:%S')]
        df4.to_excel(newfile_acc_dir)
        for i in my_datatime:
            j = i.strftime('%Y-%m-%d %H:%M:%S')
            k = i.strftime('%Y-%m-%d %H%M%S')
            df3 = df2[j:j]
            df = df1.append(df3)
            df.to_excel(file_cen_dir, index=False)
            name = data_opt.tezheng_hour(file_cen_dir, newfile_dir, i)
            k = k.replace(' ', '_')
            data_visual.plot_radar_time_hour(newfile_dir, k, name[0],namell,name2)
            ls.append(name2+k+'.png')
    return ls

# 滚动计算每一天的特征雷达图
def time_roll_data(start_time,stop_time,name1,namell,name2):
    ls = []
    my_datatime = pd.date_range(start_time, stop_time)
    for result in my_datatime:
        print(result)
        yestoday = (result + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
        file_dir = 'static/uploads/{}.xls'.format(name1)
        file_cen_dir = 'static/uploads/{}cen.xls'.format(name1)
        newfile_dir = 'static/uploads/{}end.xls'.format(name1)
        df = pd.read_excel(file_dir)
        df.index = df['时间']
        df = df[yestoday:result.strftime('%Y-%m-%d')]
        df.to_excel(file_cen_dir,index=False)
        name = data_opt.tezheng(file_cen_dir,newfile_dir,result.strftime('%Y-%m-%d'))
        data_visual.plot_radar_time(newfile_dir,result.strftime('%Y-%m-%d'),name[0],namell)
        ls.append(name2+result.strftime('%Y-%m-%d')+'.png')
    return ls


# 滚动计算每一天的区域特征雷达图
def area_roll_data(start_time,stop_time,area_name,name1,namell,name2):
    ls = []
    # start_time = '2020-01-11'
    # stop_time = '2020-12-31'
    # area_name = '淮阳县'
    my_datatime = pd.date_range(start_time, stop_time)
    for result in my_datatime:
        print(result)
        yestoday = (result + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
        file_dir = 'static/uploads/{}.xls'.format(name1)
        file_cen_dir = 'static/uploads/{}cen.xls'.format(name1)
        newfile_dir = 'static/uploads/{}end.xls'.format(name1)
        df = pd.read_excel(file_dir)
        df.index = df['时间']
        df = df[yestoday:result.strftime('%Y-%m-%d')]
        df.to_excel(file_cen_dir)
        name = data_opt.tezheng_area(file_cen_dir,newfile_dir,result.strftime('%Y-%m-%d'),area_name)
        data_visual.plot_radar_time(newfile_dir,result.strftime('%Y-%m-%d'),name[0],namell,name2)
        ls.append(name2+result.strftime('%Y-%m-%d')+'.png')
    return ls


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        mold = request.form.get('mold')
        basepath = '/root/wyj/api_make/tezhengleida/'  # 当前文件所在路径
        namel = datatime.datetime.now().strftime('%Y%m%d%H%M%S')
        namell = datatime.datetime.now().strftime('%Y%m%d')
        name = f.filename.split('.')[0]
        upload_path = os.path.join(basepath, r'static/uploads',secure_filename(namel+name+'.xls'))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        if mold=='0':
            start_time = request.form.get("start_time")
            stop_time = request.form.get("stop_time")
            if not os.path.exists('image_file/{}/'.format(namell)):
                os.makedirs('image_file/{}/'.format(namell))
            l = time_roll_data(start_time,stop_time,namel+name,namell,namel)
            return json.dumps(l).encode('utf-8')
        elif mold=='1':
            start_time = request.form.get("start_time")
            stop_time = request.form.get("stop_time")
            if not os.path.exists('image_file/{}/'.format(namell)):
                os.makedirs('image_file/{}/'.format(namell))
            area_name= request.form.get("area_name")
            l = area_roll_data(start_time,stop_time,area_name,namel+name,namell,namel)
            return json.dumps(l).encode('utf-8')
        elif mold=='3':
            start_time = request.form.get("start_time")
            stop_time = request.form.get("stop_time")
            if not os.path.exists('image_file/{}/'.format(namell)):
                os.makedirs('image_file/{}/'.format(namell))
            area_name = request.form.get("area_name")
            l = area_hour_acc_data(start_time,stop_time,area_name,namel+name,namell,namel)
            return json.dumps(l).encode('utf-8')
        elif mold=='2':
            start_time = request.form.get("start_time")
            stop_time = request.form.get("stop_time")
            if not os.path.exists('image_file/{}/'.format(namell)):
                os.makedirs('image_file/{}/'.format(namell))
            l = time_hour_acc_data(start_time,stop_time,namel+name,namell,namel)
            return json.dumps(l).encode('utf-8')
        else:
            return 'error'
    return render_template('demo.html')



@app.route('/download/<file_name>', methods=['GET'])
def download_file(file_name):
    namell = datatime.datetime.now().strftime('%Y%m%d')
    directory = r'/root/wyj/api_make/tezhengleida/image_file/'+namell+'/'
    print(directory)
    try:
        response = make_response(
            send_from_directory(directory, file_name, as_attachment=True))
        return response
    except Exception as e:
        pass



if __name__ == '__main__':
    app.run()
    #app.run(debug=True,host='0.0.0.0', port=2088)

