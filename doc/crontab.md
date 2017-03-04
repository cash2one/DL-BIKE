## bike station
# 北京
10 1 * * 6 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/beijing_app/beijing_beijing.py >> /var/log/cron_log/bikestation/beijing_beijing.log 2>&1 & )

# 南京
10 2 * * 6 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/nanjing_wechat/jiangsu_nanjing.py >> /var/log/cron_log/bikestation/jiangsu_nanjing.log 2>&1 & )

# 西安
10 3 * * 6 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/xian_app/shaanxi_xian.py >> /var/log/cron_log/bikestation/shaanxi_xian.log 2>&1 & )

# 福建三明
20 10 * * 1 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/fujian_sanming.py >> /var/log/cron_log/bikestation/fujian_sanming.log 2>&1 & )
# 河北邢台
40 10 * * 1 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/hebei_xingtai.py >> /var/log/cron_log/bikestation/hebei_xingtai.log 2>&1 & )
# 内蒙古巴彦淖尔
40 13 * * 1 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/neimenggu_bayannaoer.py >> /var/log/cron_log/bikestation/neimenggu_bayannaoer.log 2>&1 & )
# 山东青岛
10 13 * * 1 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/shandong_qingdao.py >> /var/log/cron_log/bikestation/shandong_qingdao.log 2>&1 & )
# 云南丽江
20 15 * * 1 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/yunnan_lijiang.py >> /var/log/cron_log/bikestation/yunnan_lijiang.log 2>&1 & )
# 浙江台州
10 16 * * 1 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/zhejiang_taizhou.py >> /var/log/cron_log/bikestation/zhejiang_taizhou.log 2>&1 & )
# 安徽滁州
10 11 * * 2 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/anhui_chuzhou.py >> /var/log/cron_log/bikestation/anhui_chuzhou.log 2>&1 & )
# 甘肃兰州
10 13 * * 2 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/gansu_lanzhou.py >> /var/log/cron_log/bikestation/gansu_lanzhou.log 2>&1 & )
# 河南信阳
20 12 * * 2 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/henan_xinyang.py >> /var/log/cron_log/bikestation/henan_xinyang.log 2>&1 & )
# 内蒙古通辽
10 15 * * 2 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/neimenggu_tongliao.py >> /var/log/cron_log/bikestation/neimenggu_tongliao.log 2>&1 & )
# 山东淄博
10 11 * * 3 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/shandong_zibo.py >> /var/log/cron_log/bikestation/shandong_zibo.log 2>&1 & )
# 浙江杭州
20 11 * * 3 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/zhejiang_hangzhou.py >> /var/log/cron_log/bikestation/zhejiang_hangzhou.log 2>&1 & )
# 安徽淮南
40 13 * * 3 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/anhui_huainan.py >> /var/log/cron_log/bikestation/anhui_huainan.log 2>&1 & )
# 广东梅州
40 15 * * 3 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/guangdong_meizhou.py >> /var/log/cron_log/bikestation/guangdong_meizhou.log 2>&1 & )
# 江苏连云港
40 17 * * 3 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/jiangsu_lianyungang.py >> /var/log/cron_log/bikestation/jiangsu_lianyungang.log 2>&1 & )
# 宁夏银川
40 13 * * 4 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/ningxia_yingchuan.py >> /var/log/cron_log/bikestation/ningxia_yingchuan.log 2>&1 & )
# 山西晋中
10 17 * * 5 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/shanxi_jinzhong.py >> /var/log/cron_log/bikestation/shanxi_jinzhong.log 2>&1 & )
# 浙江嘉兴
40 13 * * 5 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/zhejiang_jiaxing.py >> /var/log/cron_log/bikestation/zhejiang_jiaxing.log 2>&1 & )
# 安徽黄山
40 13 * * 6 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/anhui_huangshan.py >> /var/log/cron_log/bikestation/anhui_huangshan.log 2>&1 & )
# 广西柳州
40 15 * * 6 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/guangxi_liuzhou.py >> /var/log/cron_log/bikestation/guangxi_liuzhou.log 2>&1 & )
# 江西萍乡
10 18 * * 6 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/jiangxi_pingxiang.py >> /var/log/cron_log/bikestation/jiangxi_pingxiang.log 2>&1 & )
# 陕西渭南
23 19 * * 6 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/shaanxi_weinan.py >> /var/log/cron_log/bikestation/shaanxi_weinan.log 2>&1 & )
# 天津天津
28 9 * * 6 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/tianjin_tianjin.py >> /var/log/cron_log/bikestation/tianjin_tianjin.log 2>&1 & )
# 浙江金华
2 8 * * 6 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/zhejiang_jinhua.py >> /var/log/cron_log/bikestation/zhejiang_jinhua.log 2>&1 & )
# 福建泉州
2 16 * * 7 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/fujian_quanzhou.py >> /var/log/cron_log/bikestation/fujian_quanzhou.log 2>&1 & )
# 贵州六盘水
4 20 * * 7 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/guizhou_liupanshui.py >> /var/log/cron_log/bikestation/guizhou_liupanshui.log 2>&1 & )
# 辽宁大连
8 23 * * 7 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/liaoning_dalian.py >> /var/log/cron_log/bikestation/liaoning_dalian.log 2>&1 & )
# 山东临沂
4 14 * * 7 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/shandong_linyi.py >> /var/log/cron_log/bikestation/shandong_linyi.log 2>&1 & )
# 云南昆明
18 21 * * 7 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/yunnan_kunming.py >> /var/log/cron_log/bikestation/yunnan_kunming.log 2>&1 & )
# 浙江宁波
4 18 * * 7 ( source  ~/.bash_profile; /root/.pyenv/versions/bike-3.5.2/bin/python3 -u /home/www/bike/scripts/bikestation/dingda_app/zhejiang_ningbo.py >> /var/log/cron_log/bikestation/zhejiang_ningbo.log 2>&1 & )