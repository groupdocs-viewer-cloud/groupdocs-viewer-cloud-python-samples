# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to specify encoding when rendering documents
class SpecifyEncoding:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/shift_jis_encoded.txt"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()        
        view_options.render_options.default_encoding = "shift_jis"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("SpecifyEncoding completed: " + str(len(response.pages)))
