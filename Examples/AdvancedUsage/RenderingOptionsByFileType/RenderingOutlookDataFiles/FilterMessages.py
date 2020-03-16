# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render Outlook Data File with filtering the rendered messages
class FilterMessages:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.ost"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.outlook_options = groupdocs_viewer_cloud.OutlookOptions()    
        view_options.render_options.outlook_options.text_filter = "Microsoft"
        view_options.render_options.outlook_options.address_filter = "susan"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("FilterMessages completed: " + str(len(response.pages)))
