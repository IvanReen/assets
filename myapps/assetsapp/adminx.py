from myexts import xadmin as admin
from xadmin import views
# Register your models here.
from myapps.assetsapp import models
from myapps.assetsapp import asset_handler


class BaseSettings:  # 设置admin的站点样式
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = 'CMDB运维管理'
    site_footer = '西安小城Py爱好者2<h4>联系方式：18127655676</h4>'
    menu_style = 'accordion'
    # global_search_models = (Tag,)
    apps_label_title = {
        'assetsapp': '资产管理系统'   # 应用名：'应用标题'
    }
    apps_icons = {
        'assetsapp': 'glyphicon glyphicon-book'
    }
    # 子标签前面加个标志
    # global_models_icon = {
    #     models.Tag: 'glyphicon glyphicon-tags'
    # }


admin.site.register(views.BaseAdminView, BaseSettings)
admin.site.register(views.CommAdminView, GlobalSettings)


class NewAssetAdmin():
    list_display = ['asset_type', 'sn', 'model', 'manufacturer', 'c_time', 'm_time']
    list_filter = ['asset_type', 'manufacturer', 'c_time']
    search_fields = ('sn',)

    actions = ['approve_selected_new_assets']

    def approve_selected_new_assets(self, request, queryset):
        # 获得被打钩的checkbox对应的资产
        selected = request.POST.get('_selected_action')
        success_upline_number = 0
        for asset_id in selected:
            obj = asset_handler.ApproveAsset(request, asset_id)
            ret = obj.asset_upline()
            if ret:
                success_upline_number += 1
        # 顶部绿色提示信息
        self.message_user(request, f"成功批准  {success_upline_number}  条新资产上线！")
    approve_selected_new_assets.short_description = "批准选择的新资产"

class AssetAdmin():
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', "m_time"]


admin.site.register(models.Asset, AssetAdmin)
admin.site.register(models.Server)
admin.site.register(models.StorageDevice)
admin.site.register(models.SecurityDevice)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Contract)
admin.site.register(models.CPU)
admin.site.register(models.Disk)
admin.site.register(models.EventLog)
admin.site.register(models.IDC)
admin.site.register(models.Manufacturer)
admin.site.register(models.NetworkDevice)
admin.site.register(models.NIC)
admin.site.register(models.RAM)
admin.site.register(models.Software)
admin.site.register(models.Tag)
admin.site.register(models.NewAssetApprovalZone, NewAssetAdmin)

