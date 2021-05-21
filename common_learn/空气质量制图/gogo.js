function getPostParamCode(method, city, type, startTime, endTime){
    var param = {};
    param.city = city;
    param.type = type;
    param.startTime = startTime;
    param.endTime = endTime;
    return getParam(method, param);
}