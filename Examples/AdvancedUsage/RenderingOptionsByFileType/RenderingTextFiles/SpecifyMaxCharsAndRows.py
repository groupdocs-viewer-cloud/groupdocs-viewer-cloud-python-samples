# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render a text files using rows and pages restrictions
class SpecifyMaxCharsAndRows:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.txt"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.text_options = groupdocs_viewer_cloud.TextOptions()    
        view_options.render_options.text_options.max_chars_per_row = 100
        view_options.render_options.text_options.max_rows_per_page = 100

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("SpecifyMaxCharsAndRows completed: " + str(len(response.pages)))
