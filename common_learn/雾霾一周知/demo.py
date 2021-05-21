import requests

session = requests.Session()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.68676847.1597301996; pgv_pvi=9568410624; RK=wuK12L3DSi; ptcz=dd84d3710047cd6b585989d5d1818380fa50beba31dd031a7653b39e94198afe; pgv_pvid=437031940; iip=0; eas_sid=p1y6v0S2O803w3q5c8S3l1D5q2; uin_cookie=o1419169425; ied_qq=o1419169425; LOLWebSet_AreaBindInfo_1419169425=%257B%2522areaid%2522%253A%252222%2522%252C%2522areaname%2522%253A%2522%25E5%25BD%25B1%25E6%25B5%2581%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221419169425%2522%252C%2522rolename%2522%253A%2522%25E6%2584%25A4%25E6%2580%2592%25E7%259A%2584%25E5%25B0%258F%25E8%25BD%25A6%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1419169425%257C22%257C1419169425*%257C%257C%257C%257C%2525E6%252584%2525A4%2525E6%252580%252592%2525E7%25259A%252584%2525E5%2525B0%25258F%2525E8%2525BD%2525A6*%257C%257C%257C1602833792%257C%2522%252C%2522md5str%2522%253A%2522766FA1A729E74198F76646429EF6726A%2522%252C%2522roleareaid%2522%253A%252222%2522%252C%2522sPartition%2522%253A%252222%2522%257D; o_cookie=1419169425; pac_uid=1_1419169425; tvfe_boss_uuid=7376104396887547; pt_sms_phone=156******09; ptui_loginuin=1419169425; rewardsn=; wxtokenkey=777; wxuin=239282603; devicetype=Windows10x64; version=63010043; lang=zh_CN; pass_ticket=7KNUMsyQK5ofOLF3F+/V2eUp+nL+Hdnq4prYIyGxb7uCUVkol/rEFkxhRrtXnThD; wap_sid2=CKvTjHISigF5X0hGY0dIbzhETGVWOThzNWlORS1OTUU0cDJ3Sm50aEwxTTl3WXhuQmR0TWlxeEpDVmYyaUlzWU5yVEZQMm9BV1BBbXBNWmxkNGlXVnZiU2Rrbk4xSDhodWlGdFFpdTNzSTRFSmE3VUhzdUZ0cG1JX2FRakVEQmsyamtQcTFyemJ5S3kwU0FBQX4wk/2rggY4DUCVTg==',
    'Host': 'mp.weixin.qq.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

url = 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzAxNjAwNTU2Mw==&scene=124&#wechat_redirect'
res = session.get(url,headers=headers).text
print(res)