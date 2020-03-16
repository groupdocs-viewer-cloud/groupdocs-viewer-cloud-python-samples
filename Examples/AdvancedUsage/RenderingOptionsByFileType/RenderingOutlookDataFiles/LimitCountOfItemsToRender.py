# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to  render the items in an Outlook Data File by setting a maximum limit
class LimitCountOfItemsToRender:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.ost"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.outlook_options = groupdocs_viewer_cloud.OutlookOptions()    
        view_options.render_options.outlook_options.max_items_in_folder = 1000        

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("LimitCountOfItemsToRender completed: " + str(len(response.pages)))
