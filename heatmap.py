"""
画省份热点图
需要在使用的python环境中安装三方库：
pip install pyecharts
下载地图：
pip install echarts-china-provinces-pypkg 
"""
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

# %%
def geo_heatmap(address, value) -> Geo:
    province_value = [list(z) for z in zip(address, value)]
    map = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "省热点图",    
            province_value,
            type_=ChartType.HEATMAP,   #地图类型
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  #设置是否显示标签
        .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_ = 1000),    
                title_opts=opts.TitleOpts(title="全国性侵事件热力图"),   #左上角标题
        )
    )
    return map

provinces = ["广东", "北京", "上海", "黑龙江", "湖南", "四川", "西藏"]  #这里直接写省份名就可以 Geo可以识别的
value = [300, 100, 2000, 800, 10000, 400, 5000]  #省份对应的性侵案件数量
province_heat = geo_heatmap(provinces, value)
province_heat.render(path="test_heatmap3.html") #保存为html文件 如果要保存为 png 等格式province_heat.render(path='test_heatmap.png')